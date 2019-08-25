"""djangoLesson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('dapp/', include('dapp.urls')),
    path('hoge/', views.hoge),
    path('fuga/', views.fuga),
    path('crud/', views.crud),
    path('page1/', views.page1),
    path('puge/<value>', views.puge),
    path('search', views.search),
    path('post_form', views.post_form),
    path('postSend', views.postSend),
    path('post_form_image', views.post_form_image),
    path('imageUpload', views.imageUpload),
    path('dic', views.dic),
    path('escape', views.escape),
    path('sample_if', views.sample_if),
    path('sample_for', views.sample_for),
    path('sample_comment', views.sample_comment),
    path('sample_index', views.sample_index),
    path('design_index', views.design_index),
    path('design_profile', views.design_profile),
    path('design_diary_form', views.design_diary_form),
    path('design_diary_post', views.design_diary_post),
    path('admin/', admin.site.urls),
]