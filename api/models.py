from django.db import models

# Create your models here.
class user(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50, unique=True)
	password = models.TextField()
	name = models.CharField(max_length=50, unique=True)
	email = models.EmailField()
	points = models.IntegerField()

class event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    code = models.CharField(max_length=10, unique=True)
    value = models.IntegerField()
    expired = models.IntegerField()

class attendance(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    event = models.IntegerField()

    class Meta:
        unique_together = ('user', 'event')
