from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import generic
from django.db.models import Q
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import *
from .models import *


class Home(generic.ListView):
    template_name = 'myblog/index.html'
    context_object_name = 'posts_categories'

    def get_queryset(self):
        return [Category.objects.filter(parent=None),
                Post.objects.filter(is_active=True, is_confirmed=True).order_by('-pub_date')]


def view_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    categories = Category.objects.filter(parent=None)
    return render(request, 'myblog/view_post.html', {'post': post, 'categories': categories})


def post_by_category(request, category_id):
    posts = Post.objects.filter(Q(is_active=True, is_confirmed=True, category=category_id) |
                                Q(is_active=True, is_confirmed=True, category__parent=category_id))
    category_name = Category.objects.get(pk=category_id).name
    return render(request, 'myblog/by_category.html', {'posts': posts, 'name': category_name})


def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            for i in post_form:
                print(i)
            return HttpResponseRedirect(reverse('myblog:home'))
    else:
        post_form = PostForm()

    return render(request, 'myblog/add_post.html', {"form": post_form})


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'tag')


@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
