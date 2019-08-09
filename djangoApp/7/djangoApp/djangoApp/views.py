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
