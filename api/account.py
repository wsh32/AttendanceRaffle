from api.models import user
from django.http import HttpResponse
from django import forms
from django.contrib.auth.hashers import *
import json, re

def new_user(username, password, name, email):
	try:
		account = user(username=username, password=password, name=name, email=email)
		account.save()

		return True
	except:
		return False

def create_account(request):
	if (request.method != 'POST') or not all(x in request.POST for x in ['username', 'password', 'confirm', 'name', 'email']):
		return HttpResponse()

	f = forms.EmailField()
	username = request.POST['username']
	password = request.POST['password']
	confirm = request.POST['confirm']
	name = request.POST['name']

	try:
		email = f.clean(request.POST['email'])
	except:
		email = False

	try:
		repeat_user = True
		user.objects.get(username=username)
	except:
		repeat_user = False
	try:
		repeat_name = True
		user.objects.get(name=name)
	except:
		repeat_name = False
	try:
		repeat_email = True
		user.objects.get(email=email)
	except:
		repeat_email = False

	if len(username) == 0 or len(password) == 0 or len(name) == 0 or len(email) == 0:
		response = {'success': False, 'message': 'All fields must be filled out.'}
	elif repeat_name:
		response = {'success': False, 'message': 'One person. One account.'}
	elif repeat_user:
		response = {'success': False, 'message': 'Someone beat you to that username.'}
	elif not email:
		response = {'success': False, 'message': 'That is not a valid email!'}
	elif re.search('[ -~]{1,40}', username).group() != username or re.search('[ -~]{1,40}', name).group() != name:
		response = {'success': False, 'message': 'DONT ACT LIKE YOU DIDNT KNOW THAT YOU ENTERED IN INVALID CHARACTERS TO TRY TO BREAK THE SITE!!'}
	elif password != confirm:
		response = {'success': False, 'message': 'If you cannot repeat your password you should change it.'}
	else:
		success = new_user(username, make_password(password), name, email)

		if success:
			response = {'success': True, 'message': 'Registration successful!'}
		else:
			response = {'success': False, 'message': 'Error. Try again in a few seconds.'}

	return HttpResponse(json.dumps(response), content_type="application/json")
