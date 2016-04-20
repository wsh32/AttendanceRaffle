from django.shortcuts import render
from api.stats import get_points, get_name, get_events

def home(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'login.html')

def register(request):
	return render(request, 'register.html')

def account(request):
	return render(request, 'account.html', {'points': get_points(request), 'name': get_name(request), 'events': get_events(request)})

def submit(request):
	return render(request, 'submit.html')
