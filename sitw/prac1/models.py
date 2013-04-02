from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class League(models.Model):
	creationDate = models.DateTimeField()
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=100)
	def __unicode__(self):
		return self.name+" - "+self.description

class Team(models.Model):
	teamName = models.CharField(max_length=50)
	foundationYear = models.IntegerField()
	def __unicode__(self):
		return self.teamName
