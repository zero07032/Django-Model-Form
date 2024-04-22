from django.shortcuts import render, redirect


def BlogList(request):
    context = {}
    return render(request, "home.html", context)


def BlogCreate(request):
    return redirect("/")
