from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Representative(models.Model):
	name = models.CharField(max_length=50)
	nacionality = models.CharField(max_length=20)
	
class Player(models.Model):
	name = models.CharField(max_length=50)
	bornDate = models.DateField()
	nacionality = models.CharField(max_length=50)
	position = models.CharField(max_length=20)
	representative = models.ForeignKey(Representative)
	def __unicode__(self):
		return self.name+ " - "+self.position

class Team(models.Model):
	name = models.CharField(max_length=50)
	foundationYear = models.IntegerField()
	players = models.ManyToManyField(Player)
	def __unicode__(self):
		return self.name

class League(models.Model):
	name = models.CharField(max_length=50)
	teams = models.ManyToManyField(Team)
	def __unicode__(self):
		return self.name+" - "+self.description
