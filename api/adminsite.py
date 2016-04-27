from api.models import admin, user, event
from django.http import HttpResponse
from django.contrib.auth.hashers import *
import json, re, time, random

class account:
	def create_account(request):
		if (request.method != 'POST') or not all(x in request.POST for x in ['username', 'password', 'confirm']):
			return HttpResponse()

		username = request.POST['username']
		password = request.POST['password']
		confirm = request.POST['confirm']

		try:
			repeat_user = True
			admin.objects.get(username=username)
		except:
			repeat_user = False

		if len(username) == 0 or len(password) == 0:
			response = {'success': False, 'message': 'All fields must be filled out.'}
		elif repeat_user:
			response = {'success': False, 'message': 'Someone beat you to that username.'}
		elif re.search('[ -~]{1,40}', username).group() != username:
			response = {'success': False, 'message': 'DONT ACT LIKE YOU DIDNT KNOW THAT YOU ENTERED IN INVALID CHARACTERS TO TRY TO BREAK THE SITE!!'}
		elif password != confirm:
			response = {'success': False, 'message': 'If you cannot repeat your password you should change it.'}
		else:
			try:
				account = admin(user=username, password=make_password(password))
				account.save()

				response = {'success': True, 'message': 'Registration successful!'}
			except:
				response = {'success': False, 'message': 'Error. Try again in a few seconds.'}

		return HttpResponse(json.dumps(response), content_type="application/json")

class auth:
	def login(request):
		if (request.method != 'POST') or not all(x in request.POST for x in ['username', 'password']):
			return HttpResponse()

		if 'admin' in request.session:
			response = {'success': False, 'message': 'You are already logged in.'}
			return HttpResponse(json.dumps(response), content_type="application/json")

		try:
			m = admin.objects.get(user=request.POST['username'])
		except:
			m = False

		if hasattr(m, 'password') and check_password(request.POST['password'], m.password):
			request.session['admin'] = m.id
			response = {'success': True, 'message': 'You have logged in.'}
		else:
			response = {'success': False, 'message': 'Log in failed.'}
			time.sleep(0.5) # Prevent brute-forcing.

		return HttpResponse(json.dumps(response), content_type="application/json")

	def logout(request):
		if 'admin' not in request.session:
			response = {'success': False, 'message': 'You are not logged in.'}
		else:
			request.session.flush()
			response = {'success': True, 'message': 'You have been logged out.'}

		return HttpResponse(json.dumps(response), content_type="application/json")

class event_management:
	def generate_key():
		length = 6
		chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
		return ''.join(random.choice(chars) for i in range(length))

	def add_event(request):
		if (request.method != 'POST') or not all(x in request.POST for x in ['title','value']):
			return HttpResponse()

		title = request.POST['title']
		value = request.POST['value']

		try:
			repeat_title = False
			event.objects.get(title=title)
		except:
			repeat_title = True

		try:
			value = int(value)
		except:
			value = False

		if len(title) == 0 or len(value) == 0:
			response = {'success': False, 'message': 'All fields must be filled out.'}
		elif repeat_title:
			response = {'success': False, 'message': 'Pick a unique title!'}
		elif not(value):
			response = {'success': False, 'message': 'The value must be an integer!'}
		elif re.search('[ -~]{1,40}', title).group() != title:
			response = {'success': False, 'message': 'DONT ACT LIKE YOU DIDNT KNOW THAT YOU ENTERED IN INVALID CHARACTERS TO TRY TO BREAK THE SITE!!'}
		else:
			try:
				key = generate_key()
				e = event(title=title, value=value, key=key)
				e.save()

				response = {'success': True, 'message': 'Event creation successful! You key is: ' + key}
			except:
				response = {'success': False, 'messsage': 'Error! Please try again in a couple seconds'}
