from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include

def index(request):
	return HttpResponse('<p>Hello world news</p>')
# Create your views here.
