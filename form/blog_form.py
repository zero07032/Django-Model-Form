from django import forms

from .models import Blog
from django.core.exceptions import ValidationError


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "description", "image"]
