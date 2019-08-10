from django.shortcuts import render, redirect
from .models import Feed
from .forms import FeedForm

def index(request):
  feeds = Feed.objects.all()
  return render(request, 'index.html', {'feeds': feeds})

def form(request):
  form = FeedForm()
  return render(request, 'form.html', {'form': form})

def post(request):
  if request.method != 'POST':
    return redirect(to="/form")
  form = FeedForm(request.POST)
  if form.is_valid():
    feed = Feed.objects.create(title=request.POST['title'], description=request.POST['description'], href=request.POST['href'])
    feed.save()
    return redirect(to="/")
  else:
    return redirect(to="/form")

def search(request):
  try:
    feed = Feed.objects.get(title=request.GET["q"])
    return render(request, 'result.html', {'feeds': [feed]})
  except:
    return render(request, 'result.html', {'feeds': []})

def delete(request):
  if request.method == 'POST' and request.POST['id']:
    feed = Feed.objects.get(id=request.POST['id'])
    feed.delete()
    return redirect(to="/")

def page_post(request):
  if request.method == 'POST' and request.POST['title'] and request.POST['href'] and request.POST['description']:
    feed = Feed.objects.get(id=request.POST['id'])
    page = Page.objects.create(
      title=request.POST['title'],
      description=request.POST['description'],
      href=request.POST['href'],
      feed=Feed
    )
    page.save()
  return redirect(to="/")