from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
import sqlite3
from models import League

def mainpage(request):
	leagues = League.objects.all()
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Football League App',
		'pagetitle': 'Welcome to the Football League App',
		'contentbody': 'Managing non legal funding since 2013',
		'user': request.user,
		'leagues': leagues,
		})
	output = template.render(variables)
	return HttpResponse(output)
