from django.contrib import admin

from .models import user, event, attendance

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('id','username','password','name','email')

class eventAdmin(admin.ModelAdmin):
    list_display = ('id','title','value','expired')

class attendanceAdmin(admin.ModelAdmin):
    list_display = ('id','user','event')

admin.site.register(user, userAdmin)
admin.site.register(event, eventAdmin)
admin.site.register(attendance, attendanceAdmin)
