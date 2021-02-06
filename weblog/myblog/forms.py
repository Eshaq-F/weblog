from django import forms
from dal import autocomplete
from django.forms import modelformset_factory, NumberInput
from django.core.exceptions import ValidationError
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "tag", "content", "category", "image"]
