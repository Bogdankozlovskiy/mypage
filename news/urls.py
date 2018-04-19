from django.contrib import admin
from django.urls import path, include,re_path
from . import views
from django.views.generic import ListView,DetailView
from news.models import Artic
import re

urlpatterns = [
    re_path(r'^$',ListView.as_view(queryset=Artic.objects.all().order_by("-date")[:20],template_name="news/posts.html")),
    re_path(r'^(?P<pk>\d+)$',DetailView.as_view(model=Artic,template_name="news/post.html"))
]