from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "image"]
        tag = forms.SelectMultiple()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


def set_choices():
    authors = User.objects.filter(groups__name='نويسندگان')
    choices = list()
    for author in authors:
        choice = (author, str(author.get_full_name()))
        choices.append(choice)
    return choices


class PostSearchForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=2, label="عنوان")
    content = forms.CharField(max_length=50, label="متن")
    author = forms.ChoiceField(choices=set_choices, label="نويسنده مطلب")
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple,
                                          label="برچسب")
