from api.models import admin, user, event
from django.http import HttpResponse
from django.contrib.auth.hashers import *
import json, re, time, random

class account:
	def create_account(self, request):
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
	def login(self, request):
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

	def logout(self, request):
		if 'admin' not in request.session:
			response = {'success': False, 'message': 'You are not logged in.'}
		else:
			request.session.flush()
			response = {'success': True, 'message': 'You have been logged out.'}

		return HttpResponse(json.dumps(response), content_type="application/json")

class event_management:
	def generate_key(self):
		length = 6
		chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
		return ''.join(random.choice(chars) for i in range(length))

	def add_event(self, request):
		if (request.method != 'POST') or not all(x in request.POST for x in ['title','value','key']):
			return HttpResponse()

		title = request.POST['title']
		val = request.POST['value']
		key = request.POST['key']

		try:
			repeat_title = True
			event.objects.get(title=title)
		except:
			repeat_title = False

		try:
			value = int(val)
		except:
			value = False

		if len(title) == 0 or len(val) == 0:
			response = {'success': False, 'message': 'All fields must be filled out.'}
		elif repeat_title:
			response = {'success': False, 'message': 'Pick a unique title!'}
		elif not(value):
			response = {'success': False, 'message': 'The value must be an integer!'}
		elif len(key) > 10:
			response = {'success': False, 'message': 'The key must be less than 10 characters'}
		elif re.search('[ -~]{1,40}', title).group() != title and re.search('[ -~]{1,40}', key).group() != key:
			response = {'success': False, 'message': 'DONT ACT LIKE YOU DIDNT KNOW THAT YOU ENTERED IN INVALID CHARACTERS TO TRY TO BREAK THE SITE!!'}
		else:
			try:
				e = event(title=title, value=value, code=key)
				e.save()

				response = {'success': True, 'message': 'Event creation successful!'}
			except:
				response = {'success': False, 'message': 'Error! Please try again in a couple seconds'}

		return HttpResponse(json.dumps(response), content_type="application/json")
