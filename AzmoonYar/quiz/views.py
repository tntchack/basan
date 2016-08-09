from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test(request):
    html = "<h1>this is a test</h1>"
    return HttpResponse(html)