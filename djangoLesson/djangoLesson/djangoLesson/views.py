from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

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