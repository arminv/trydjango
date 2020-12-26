# We import `HttpResponse` so we can pass it a string and it will render it as HTML
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")  # string of HTML code
