from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

# kadai1
def djangoDayo(request):
  return HttpResponse("Django Dayo")

# kadai2
def koge(request, value):
  return render(request, 'koge.html', {'description': value})

def profile_form(requset):
  return render(requset, 'profile_form.html')

def postProfile(request):
  if request.POST['name'] and request.POST['age'] and request.POST['profile']:
    return render(request, 'profile_display.html', {'name': request.POST['name'], 'age': request.POST['age'], 'profile': request.POST['profile']})
  else:
    return render(request, 'error.html')