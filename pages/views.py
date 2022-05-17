from django.shortcuts import render, HttpResponse

# Create your views here.

def home_page_view(request):
    return HttpResponse("Hello World")
