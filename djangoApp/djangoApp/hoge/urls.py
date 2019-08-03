from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('foo', views.foo),
  path('woo', views.woo),
]
