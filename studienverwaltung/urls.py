from django.conf.urls import patterns, url
from studienverwaltung import views

urlpatterns = patterns('studienverwaltung.views',
    url(r'^$', views.index, name='index'),

#-----------------Studienverwaltung------------------
    #-----------------------Show--------------------------
    url(r'^showStudie/$', views.showStudie, name='showStudie'),
    url(r'^showStudieArt/$', views.showStudieArt, name='showStudieArt'),
    #-----------------------Insert------------------------
    url(r'^createStudieArtForm/$', views.addStudieart, name='createStudieArtForm'),
    url(r'^createStudieForm/$', views.addStudie, name='createStudieForm'),
    #-----------------------delete------------------------
    url(r'^editStudie/deleteStudie/(?P<sID>\d+)/$', views.deleteToggleStudie, name='deleteToggleStudie'),
    #-----------------------edit------------------------
    url(r'^editStudie/$', views.editStudie, name='editStudie'),
    url(r'^editStudie/(?P<sID>\d+)/$', views.editStudieForm, name='editStudieForm'),
)
