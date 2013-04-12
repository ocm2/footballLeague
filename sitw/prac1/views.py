from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from models import *

def mainpage(request):	
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Football League App',
		'contentbody': 'Managing non legal funding since 2013',
		})

	return general(request, template, variables)

def general(request, template, variables):
	variables['user'] = request.user
	if template == 'list':
		template = get_template('listPages/list.html')

	output = template.render(variables)
	return HttpResponse(output)


def representativesList(request):
	representatives = Representative.objects.all()
	variables = Context({
		'title': 'List of Representatives',
		'titlehead': 'List of Representatives',
		'items': representatives,
		'route': '/representative/',
	})

	return general(request, 'list', variables)

def representativeModel(request, idaux):
	representative = Representative.objects.get(id = idaux)
	template = get_template('modelPages/representative.html')
	variables = Context({
		'title': 'Information of Representative',
		'titlehead': 'Information of Representative',
		'rep': representative,
	})

	return general(request, template, variables)

def playersList(request):
	players = Player.objects.all()
	variables = Context({
		'title': 'List of Players',
		'titlehead': 'List of Players',
		'items': players,	
		'route': '/player/',
	})

	return general(request, 'list', variables)

def playerModel(request, idaux):
	player = Player.objects.get(id = idaux)
	template = get_template('modelPages/player.html')
	variables = Context({
		'title': 'Information of Player',
		'titlehead': 'Information of Player',
		'player': player,
	})

	return general(request, template, variables)	

def stadiumsList(request):
	stadiums = Stadium.objects.all()
	variables = Context({
		'title': 'List of Stadiums',
		'titlehead': 'List of Stadiums',
		'items': stadiums,	
		'route': '/stadium/',
	})

	return general(request, 'list', variables)

def stadiumModel(request, idaux):
	stadium = Stadium.objects.get(id = idaux)
	template = get_template('modelPages/stadium.html')
	variables = Context({
		'title': 'Information of Stadium',
		'titlehead': 'Information of Stadium',
		'stadium': stadium,
	})

	return general(request, template, variables)

def coachsList(request):
	coachs = Coach.objects.all()
	variables = Context({
		'title': 'List of Coachs',
		'titlehead': 'List of Coachs',
		'items': coachs,	
		'route': '/coach/',
	})

	return general(request, 'list', variables)

def coachModel(request, idaux):
	coach = Coach.objects.get(id = idaux)
	template = get_template('modelPages/coach.html')
	variables = Context({
		'title': 'Information of Coach',
		'titlehead': 'Information of Coach',
		'coach': coach,
	})

	return general(request, template, variables)

def teamsList(request):
	teams = Team.objects.all()
	variables = Context({
		'title': 'List of Teams',
		'titlehead': 'List of Teams',
		'items': teams,	
		'route': '/team/',
	})

	return general(request, 'list', variables)	

def teamModel(request, idaux):
	team = Team.objects.get(id = idaux)
	template = get_template('modelPages/team.html')
	variables = Context({
		'title': 'Information of Team',
		'titlehead': 'Information of Team',
		'team': team,
	})

	return general(request, template, variables)

def leaguesList(request):
	leagues = League.objects.all()
	variables = Context({
		'title': 'List of Leagues',
		'titlehead': 'List of Leagues',
		'items': leagues,	
		'route': '/league/',
	})

	return general(request, 'list', variables)	

def leagueModel(request, idaux):
	league = League.objects.get(id = idaux)
	template = get_template('modelPages/league.html')
	variables = Context({
		'title': 'Information of League',
		'titlehead': 'Information of League',
		'league': league,
	})
	return general(request, template, variables)

def refereesList(request):
	referees = Referee.objects.all()
	variables = Context({
		'title': 'List of Referees',
		'titlehead': 'List of Referees',
		'items': referees,	
		'route': '/referee/',
	})

	return general(request, 'list', variables)

def refereeModel(request, idaux):
	referee = Referee.objects.get(id = idaux)
	template = get_template('modelPages/referee.html')
	variables = Context({
		'title': 'Information of Referee',
		'titlehead': 'Information of Referee',
		'ref': referee,
	})

	return general(request, template, variables)	

def matchesList(request):
	matches = Match.objects.all()
	template = get_template('listPages/matcheslist.html')
	variables = Context({
		'title': 'List of Matches',
		'titlehead': 'List of Matches',
		'items': matches,
	})

	return general(request, template, variables)	

def matchModel(request, idaux):
	match = Match.objects.get(id = idaux)
	template = get_template('modelPages/match.html')
	variables = Context({	
		'title': 'Information of Match: ',
		'titlehead': 'Information of Match: ',
		'match': match,
	})

	return general(request, template, variables)	
	
			
