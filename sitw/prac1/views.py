from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from models import *

def mainpage(request):	
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Football League App',
		'pagetitle': 'Welcome to the Football League App',
		'contentbody': 'Managing non legal funding since 2013',
		'user': request.user,
		})
	output = template.render(variables)
	return HttpResponse(output)

def representativeslist(request):
	representatives = Representative.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Representatives',
		'items': representatives,
	})
	output = template.render(variables)
	return HttpResponse(output)

def playerslist(request):
	players = Player.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Players',
		'items': players,
	})
	output = template.render(variables)
	return HttpResponse(output)

def stadiumslist(request):
	stadiums = Stadium.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Stadiums',
		'items': stadiums,
	})
	output = template.render(variables)
	return HttpResponse(output)

def coachslist(request):
	coachs = Coach.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Coachs',
		'items': coachs,
	})
	output = template.render(variables)
	return HttpResponse(output)


def teamslist(request):
	teams = Team.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Teams',
		'items': teams,
	})
	output = template.render(variables)
	return HttpResponse(output)	

def leagueslist(request):
	leagues = League.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Leagues',
		'items': leagues,
	})
	output = template.render(variables)
	return HttpResponse(output)	

def refereeslist(request):
	referees = Referee.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Referees',
		'items': referees,
	})
	output = template.render(variables)
	return HttpResponse(output)	

	
