from django.http import HttpResponse
from django.shortcuts import render

# 課題1
def djangoDayo(request):
  return HttpResponse("Django Dayo")

# 課題2
def koge(request, value):
  return render(request, 'koge.html', {'description': value})