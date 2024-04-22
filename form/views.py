from django.shortcuts import render, redirect
from django.contrib import messages

from .blog_form import BlogForm
from .models import Blog


def BlogList(request):
    context = {"blogs": Blog.objects.all()}
    return render(request, "home.html", context)


def BlogCreate(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your blog has been created!")
        else:
            messages.warning(request, "Something wrong!")
    return redirect("/")
