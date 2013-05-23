__author__ = 'momo'
from django.conf.urls import patterns, url

urlpatterns = patterns('benutzerverwaltung.views',

    url(r'^$', 'loginView', name='loginView'),
    url(r'^logout/$','logoutView', name='logoutView'),
    url(r'^loginFault/$','loginFault', name='loginFault'),
    url(r'^loginSuccess/$','loginSuccess', name='loginSuccess'),
)