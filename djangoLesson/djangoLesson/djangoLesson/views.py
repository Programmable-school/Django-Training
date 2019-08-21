from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from hashlib import md5
from random import random

# def index(request):
#   return HttpResponse("Hello World")
def index(request):
  return render(request, 'index.html', {'title': 'Hello World'})

def hoge(request):
  return HttpResponse("hoge")

def fuga(request):
  return HttpResponse("fuga")

@csrf_exempt
def crud(request):
  if request.method == 'POST':
    return HttpResponse('POST')
  elif request.method == 'GET':
    return HttpResponse('GET')
  elif request.method == 'PUT':
    return HttpResponse('PUT')
  elif request.method == 'DELETE':
    return HttpResponse('DELETE')
  else:
    return HttpResponse('Unknown')

def page1(request):
  return HttpResponse("""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="/static/style.css" />
      </head>
      <body>
        <h1>Page 1</h1>
      </body>
    </html>
  """)

def puge(request, value):
  return render(request, 'puge.html', {'title': value})

def search(request):
  q = request.GET.get('q')
  return HttpResponse(q)

def post_form(requset):
  return render(requset, 'post_form.html')

def postSend(request):
  if request.POST['name'] and request.POST['age']:
    return render(request, 'post_display.html', {'name': request.POST['name'], 'age': request.POST['age']})
  else:
    return render(request, 'error.html')

def post_form_image(request):
  return render(request, 'post_form_image.html')

def imageUpload(request):
  if request.method == 'POST' and request.FILES['image'] and (request.FILES['image'].content_type == "image/png" or request.FILES['image'].content_type == "image/jpeg"):
    # 画像の拡張子
    extension = ".jpg"
    if request.FILES['image'].content_type == "image/png":
      extension = ".png"

    # ファイル名
    filename = md5(request.FILES['image'].name.encode('utf-8')).hexdigest() + extension

    # ファイルパス
    filepath = 'static/' + filename

    # 画像データを image へ書き写す
    image = open(filepath, 'wb')
    for chunk in request.FILES['image'].chunks():
      image.write(chunk)
    return render(request, 'post_display_image.html', {'filepath': filepath})
  else:
    return HttpResponseRedirect('/post_form_image')

def dic(request):
  return render(request, 'dic.html', {'obj': {'title': 'hoge'}})

def escape(request):
  return render(request, 'escape.html', {'unescaped': '<script>alert(\'hoge\')</script>'})

def sample_if(request):
  return render(request, 'sample_if.html', {'random': random()})

def sample_for(request):
  return render(request, 'sample_for.html', {'list': ['Hoge', 'Fuga', 'Foo']})

def sample_comment(request):
  return render(request, 'sample_comment.html')

def sample_index(request):
  return render(request, 'sample_index.html', {'title': 'タイトル', 'message': 'メッセージ'})