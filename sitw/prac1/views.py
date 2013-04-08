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

def representativesList(request):
	representatives = Representative.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Representatives',
		'items': representatives,
	})
	output = template.render(variables)
	return HttpResponse(output)

def playersList(request):
	players = Player.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Players',
		'items': players,
	})
	output = template.render(variables)
	return HttpResponse(output)

def stadiumsList(request):
	stadiums = Stadium.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Stadiums',
		'items': stadiums,
	})
	output = template.render(variables)
	return HttpResponse(output)

def coachsList(request):
	coachs = Coach.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Coachs',
		'items': coachs,
	})
	output = template.render(variables)
	return HttpResponse(output)


def teamsList(request):
	teams = Team.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Teams',
		'items': teams,
	})
	output = template.render(variables)
	return HttpResponse(output)	

def leaguesList(request):
	leagues = League.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Leagues',
		'items': leagues,
	})
	output = template.render(variables)
	return HttpResponse(output)	

def refereesList(request):
	referees = Referee.objects.all()
	template = get_template('listPages/list.html')
	variables = Context({
		'title': 'List of Referees',
		'items': referees,
	})
	output = template.render(variables)
	return HttpResponse(output)

def matchesList(request):
	matches = Match.objects.all()
	template = get_template('listPages/matcheslist.html')
	variables = Context({
		'title': 'List of Matches',
		'items': matches,
	})
	output = template.render(variables)
	return HttpResponse(output)	

def teamModel(request):
	team = 
	template = get_template('modelPages/team.html')
	variables = Context({
		'title': 'Team',
		'team' = team,
	})
	output = template.render(variables)
	return HttpResponse(output)			
