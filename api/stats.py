from api.models import user, event, attendance

def get_points(request):
	try:
		return user.objects.get(id=request.session['userid']).points
	except:
		return False

def get_name(request):
	try:
		return user.objects.get(id=request.session['userid']).name
	except:
		return False

def get_events(request):
    attendances = []
    for i in attendance.objects.all():
        if i.user == request.session['userid']:
            attendances.append(i)

    events = []
    for i in attendances:
        events.append(event.objects.get(id=i.event))
    return events
