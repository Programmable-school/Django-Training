from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello World")

def hoge(request):
  return HttpResponse("hoge")

def fuga(request):
  return HttpResponse("fuga")