from django.shortcuts import render
from django.http import HttpResponse
# def hello(request):
#     return HttpResponse("<h1>Welcome to Gautam Yadav</h1>")


def hello(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "index.html")