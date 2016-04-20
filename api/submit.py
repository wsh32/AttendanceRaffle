from api.models import user, event, attendance
import json, re, time
from django.http import HttpResponse
from django import forms

def new_submission(user, event):
    try:
        submission = attendance(user=user, event=event)
        submission.save()

        return True
    except:
        return False

def submit(request):
    if(request.method != 'POST') or not all(x in request.POST for x in ['code']):
        return HttpResponse()

    if 'userid' not in request.session:
        response = {'success': False, 'message': 'You must be logged in!'}
        return HttpResponse(json.dumps(response), content_type="application/json")

    try:
        correct = True
        e = event.objects.get(code=request.POST['code'])
    except:
        correct = False

    if not correct:
        response = {'success': False, 'message': 'Invalid code!'}
    elif not new_submission(request.session['userid'], e.id):
        response = {'success': False, 'message': 'This code was already submitted!'}
    else:

        u = user.objects.get(id=request.session['userid'])
        u.points += e.value
        u.save()

        response = {'success': True, 'message': 'Thank you for attending '  + e.title + '! {+' + str(e.value) + ' points}'}

    return HttpResponse(json.dumps(response), content_type="application/json")
