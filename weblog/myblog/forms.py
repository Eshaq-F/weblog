from django import forms
from django.forms import modelformset_factory, NumberInput
from django.core.exceptions import ValidationError
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image", "tag", "category"]
