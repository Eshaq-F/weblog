from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.postgres.search import SearchVector
from django.views import generic
from .forms import *
from .models import *
from .validators import check_tag_form


class Home(generic.ListView):
    template_name = 'myblog/index.html'
    context_object_name = 'posts_categories'

    def get_queryset(self):
        return [Category.objects.filter(parent=None),
                Post.objects.filter(is_active=True, is_confirmed=True).order_by('-pub_date'),
                Tag.objects.all()]


def view_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post, is_confirmed=True).order_by('date_time')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('myblog:view_post', args=(post_id,)))
    else:
        comment_form = CommentForm()
    return render(request, 'myblog/view_post.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


def post_by_category(request, category_id):
    posts = Post.objects.filter(Q(is_active=True, is_confirmed=True, category=category_id) |
                                Q(is_active=True, is_confirmed=True, category__parent=category_id))
    category_name = Category.objects.get(pk=category_id).name
    return render(request, 'myblog/by_category.html', {'posts': posts, 'name': category_name})


def post_by_tag(request, tag_id):
    posts = Post.objects.filter(tag=tag_id)
    tags = Tag.objects.all()
    return render(request, 'myblog/by_tag.html', {"posts": posts, "tags": tags})


def add_post(request):
    tags = Tag.objects.all()
    add_tags = list()
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        print(post_form.errors)
        for tag in request.POST.getlist('tag'):
            if tag.isdigit():
                t = Tag.objects.get(pk=tag)
                add_tags.append(t)
            else:
                if check_tag_form(tag):
                    t = Tag.objects.create(label=tag)
                    add_tags.append(t)
                else:

                    return render(request, 'myblog/add_post.html', {"form": post_form, "tags": tags})

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag.add(*add_tags)
            post_form.save_m2m()
            return HttpResponseRedirect(reverse('myblog:home'))
    else:
        post_form = PostForm()

    return render(request, 'myblog/add_post.html', {"form": post_form, "tags": tags})


def simple_search(request):
    public_cat = Category.objects.filter(parent=None)
    if request.method == 'POST':
        key_word = request.POST.get('simple-search')
        posts = Post.objects.annotate(search=SearchVector('title', 'content', 'author__first_name',
                                                          'author__last_name')).filter(search=key_word)
        return render(request, 'myblog/search_results.html', {'public_categories': public_cat, 'posts': posts})
    else:
        return render(request, 'myblog/search_results.html', {'public_categories': public_cat, 'empty': True})


def advanced_search(request):
    public_cat = Category.objects.filter(parent=None)
    if request.method == 'POST':
        form = PostSearchForm(request.POST)
        if form.is_valid():
            posts = Post.objects.annotate(search=SearchVector('content')) \
                .filter(search=form.cleaned_data["content"], title=form.cleaned_data["title"],
                        tag__in=form.cleaned_data["tags"],
                        author=User.objects.get(username=form.cleaned_data['author']))
            return render(request, 'myblog/search_results.html', {'public_categories': public_cat, 'posts': posts})
        else:
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        return render(request, 'myblog/search_results.html', {'public_categories': public_cat, 'empty': True})
