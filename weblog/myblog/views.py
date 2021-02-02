from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import *
from .models import *


def home(request):
    return render(request, 'myblog/index.html')


def view_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'myblog/view_post.html', {'post': post})


def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            return HttpResponseRedirect(reverse('myblog:index'))
    else:
        post_form = PostForm()

    return render(request, 'myblog/add_post.html', {"form": post_form})
