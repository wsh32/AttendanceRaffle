from django.contrib import admin

from .models import user, event, attendance
from .models import admin as superuser

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('id','username','points','name','email')

class eventAdmin(admin.ModelAdmin):
    list_display = ('id','title','code','value')

class attendanceAdmin(admin.ModelAdmin):
    list_display = ('id','user','event')

class adminAdmin(admin.ModelAdmin):
    list_display = ('id','user','password')

admin.site.register(user, userAdmin)
admin.site.register(event, eventAdmin)
admin.site.register(attendance, attendanceAdmin)
admin.site.register(superuser, adminAdmin)
