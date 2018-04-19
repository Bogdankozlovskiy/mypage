from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include

def index(request):
	return render(request,'main/homepage.html')
	
def contact(request):
	return render(request,'main/basic.html',{'values':['если вопросы','123456423']})

# Create your views here.
