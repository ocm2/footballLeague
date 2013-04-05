from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
	playerName = models.CharField(max_length=50)
	bornDate = models.DateField()
	nacionality = models.CharField(max_length=50)
	position = models.CharField(max_length=20)
	def __unicode__(self):
		return self.playerName+ " - "+self.position

class Team(models.Model):
	teamName = models.CharField(max_length=50)
	foundationYear = models.IntegerField()
	players = models.ManyToManyField(Player)
	def __unicode__(self):
		return self.teamName

class League(models.Model):
	creationDate = models.DateTimeField()
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=100)
	teams = models.ManyToManyField(Team)
	def __unicode__(self):
		return self.name+" - "+self.description
