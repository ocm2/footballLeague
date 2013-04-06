from django.conf.urls import patterns, include, url
from prac1.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', mainpage, name='home'),
	url(r'^representativeslist/$', representativeslist, name='List of Representative'),
	url(r'^playerslist/$', playerslist, name='List of Players'),
	url(r'^stadiumslist/$', stadiumslist, name='List of Stadiums'),
	url(r'^coachslist/$', coachslist, name='List of Coachs'),
	url(r'^teamslist/$', teamslist, name='List of Teams'),
	url(r'^leagueslist/$', leagueslist, name='List of Leagues'),
	url(r'^refereeslist/$', refereeslist, name='List of Referees'),
	url(r'^matcheslist/$', matcheslist, name='List of Matches'),

	#url(r'^user/(\w+)/$', userpage),
	#url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^$', 'prova.views.home', name='home'),
    # url(r'^prova/', include('prova.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
