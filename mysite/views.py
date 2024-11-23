# I created this flie-Abhay
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Abhay bhai")

def about(request):
    return HttpResponse("About Abhay bhai")

def txt(request):
    return HttpResponse(url("mysite\one.txt"))