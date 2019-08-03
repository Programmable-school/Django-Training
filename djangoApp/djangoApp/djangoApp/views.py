from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from hashlib import md5

def index(request):
  return render(request, 'index.html', {'title': 'Hello World'})

def hoge(request):
  if request.method == 'POST':
    return HttpResponse("Hoge")
  elif request.method == 'GET':
    return HttpResponse("hoge")
  else:
    return HttpResponse("Foo")

def fuga(request, foo):
  return render(request, 'index.html', {'title': foo})

def search(request):
  q = request.GET.get('q')
  return HttpResponse(q)

def render_form(request):
  return render(request, 'login.html')

def login(request):
  if request.POST['username'] and request.POST['email']:
    return render(request, 'check.html', {
      "email": request.POST['username'],
      "username": request.POST['email']})
  else:
    return render(request, 'error.html')

def form(request):
  return render(request, 'form.html')

def upload(request):
  if request.method == 'POST' and request.FILES['image'] and \
    (request.FILES['image'] == "image/png" or request.FILES['image'].content_type == "image/jpeg"):
    extension = ".jpg"
    if request.FILES['image'].content_type == "image/png":
      extension = ".png"
    print(request.FILES['image'].name)
    filepath = 'static/' + md5(request.FILES['image'].name.encode('utf-8')).hexdigest() + extension
    image = open(filepath, 'wb')
    for chunk in request.FILES['image'].chunks():
      image.write(chunk)
    return render(request, 'result.html', {'filepath': filepath, 'name': 'Hoge'})
  else:
    return HttpResponseRedirect('/form')