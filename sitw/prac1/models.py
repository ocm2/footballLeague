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
	constructionYear = models.IntegerField()
	capacity = models.IntegerField()
	def __unicode__(self):
		return self.name

class Coach(models.Model):
	name = models.CharField(max_length=50)	
        nacionality = models.CharField(max_length=50)
	age = models.IntegerField()
	def __unicode__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=50)
	foundationYear = models.IntegerField()
	players = models.ManyToManyField(Player)
	stadium = models.ForeignKey(Stadium)
	coach = models.ForeignKey(Coach)
	def __unicode__(self):
		return self.name


class League(models.Model):
	name = models.CharField(max_length=50)
	teams = models.ManyToManyField(Team)
	def __unicode__(self):
		return self.name

class Referee(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	def __unicode__(self):
		return self.name

class Match(models.Model):
	day = models.CharField(max_length=10) #Jornada
	numOfMatch = models.CharField(max_length=10) #numero de partit dins la jornada 
	teams = models.ManyToManyField(Team)
	result = models.CharField(max_length=5)
	stadium = models.ForeignKey(Stadium)
	referee = models.ForeignKey(Referee)
	def __unicode__(self):
		return self.day+" - "+ self.numOfMatch
