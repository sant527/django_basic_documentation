from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def articles(request):
	return render(request, 'articles/main_page/articles.html')
