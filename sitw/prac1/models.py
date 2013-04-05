from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Representative(models.Model):
	name = models.CharField(max_length=50)
	nacionality = models.CharField(max_length=20)
	def __unicode__(self):
		return self.name
	
class Player(models.Model):
	name = models.CharField(max_length=50)
	bornDate = models.DateField()
	nacionality = models.CharField(max_length=50)
	position = models.CharField(max_length=20)
	representative = models.ForeignKey(Representative)
	def __unicode__(self):
		return self.name+ " - "+self.position

class Stadium(models.Model):
	name = models.CharField(max_length=50)
	constructionDate = models.DateField()
	capacity = models.IntegerField()
	def __unicode__(self):
		return self.name

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

class Referee(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	def __unicode__(self):
		return self.name

class Match(models.Model):
	matchId = models.IntegerField() 
	teams = models.ManyToManyField(Team)
	result = models.CharField(max_length=5)
	def __unicode__(self):
		return self.matchId
