# We import `HttpResponse` so we can pass it a string and it will render it as HTML
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # Note we can see the request object:
    print(request)
    # Note we can see the user who is sending the request:
    print(request.user)
    # return HttpResponse("<h1>Hello World!</h1>")  # string of HTML code
    # Note, we can instead return a template - it takes 3 args: 1) request 2) Template Name 3) Context:
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")  # string of HTML code
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")  # string of HTML code
    return render(request, "about.html", {})


def sociak_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")  # string of HTML code
