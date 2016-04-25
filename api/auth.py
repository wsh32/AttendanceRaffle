from api.models import user
import json, time
from django.http import HttpResponse
from django.contrib.auth.hashers import *

def login(request):
	if (request.method != 'POST') or not all(x in request.POST for x in ['username', 'password']):
		return HttpResponse()

	if 'userid' in request.session:
		response = {'success': False, 'message': 'You are already logged in.'}
		return HttpResponse(json.dumps(response), content_type="application/json")

	try:
		m = user.objects.get(username=request.POST['username'])
	except:
		m = False

	if hasattr(m, 'password') and check_password(request.POST['password'], m.password):
		request.session['userid'] = m.id
		response = {'success': True, 'message': 'You have logged in.'}
	else:
		response = {'success': False, 'message': 'Log in failed.'}
		time.sleep(0.5) # Prevent brute-forcing.

	return HttpResponse(json.dumps(response), content_type="application/json")

def logout(request):
	'''Handles logout requests. Accepts no post parameters'''

	if 'userid' not in request.session:
		response = {'success': False, 'message': 'You are not logged in.'}
	else:
		request.session.flush()
		response = {'success': True, 'message': 'You have been logged out.'}

	return HttpResponse(json.dumps(response), content_type="application/json")
