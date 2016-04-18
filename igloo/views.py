from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'home.html')

def logout(request):
	return render(request, 'home.html')

def register(request):
	return render(request, 'home.html')

def account(request):
	return render(request, 'home.html')
