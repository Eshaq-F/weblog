from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import generic
from django.db.models import Q
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
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
    comments = Comment.objects.filter(post=post, is_confirmed=True)
    print(comments)
    categories = Category.objects.filter(parent=None)
    return render(request, 'myblog/view_post.html', {'post': post, 'categories': categories, 'comments': comments})


def post_by_category(request, category_id):
    posts = Post.objects.filter(Q(is_active=True, is_confirmed=True, category=category_id) |
                                Q(is_active=True, is_confirmed=True, category__parent=category_id))
    category_name = Category.objects.get(pk=category_id).name
    return render(request, 'myblog/by_category.html', {'posts': posts, 'name': category_name})


def post_by_tag(request, tag_id):
    # tag = Tag.objects.filter(id=tag_id)
    posts = Post.objects.filter(tag=tag_id)
    return render(request, 'myblog/by_tag.html', {"posts": posts})


def add_post(request):
    tags = Tag.objects.all()
    add_tags = list()
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
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


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LikeCommentLog
#         fields = ('id', 'comment', 'like_or_dislike')


@api_view(['GET', 'POST'])
def post_collection(request):
    # if request.method == 'GET':
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)
    if request.method == 'POST':
        comment = Comment.objects.get(pk=int(request.data['id']))
        action = request.data['id']
        print(action)
        # if serializer.is_valid():
        #     serializer.user = request.user
        return Response(status=200)
