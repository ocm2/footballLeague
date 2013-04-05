from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from models import League,Team,Player

def mainpage(request):
	leagues = League.objects.all()
	teams = Team.objects.all()
	players = Player.objects.all()
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Football League App',
		'pagetitle': 'Welcome to the Football League App',
		'contentbody': 'Managing non legal funding since 2013',
		'user': request.user,
		'leagues': leagues,
		'teams': teams,
		'players': players,
		})
	output = template.render(variables)
	return HttpResponse(output)
