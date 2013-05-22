__author__ = 'Nico'

from django.conf.urls import patterns, url

urlpatterns = patterns('laborwertverwaltung.views',

    # ex: /studienverwaltung/
    url(r'^$', 'index', name='index'),

    url(r'^admin/$', 'admin', name='admin'),

    url(r'^erstellenLaborwert/$', 'addLaborwert', name='addLaborwert'),
    url(r'^erstellenLaborwertAdmin/$', 'addLaborwert_admin', name='addLaborwert_admin'),
    url(r'^erstellenLaborwerttyp/$', 'addLaborwerttyp', name='addLaborwerttyp'),
    url(r'^erstellenEinheit/$', 'addEinheit', name='addEinheit'),
    url(r'^erstellenWertigkeit/$', 'addWertigkeit', name='addWertigkeit'),
    url(r'^erstellenMaleMinMax/$', 'addMaleMinMax', name='addMaleMinMax'),
    url(r'^erstellenFemaleMinMax/$', 'addFemaleMinMax', name='addFemaleMinMax'),

    url(r'^anzeigeLaborwert/$', 'showLaborwert', name='showLaborwert'),
    url(r'^anzeigeLaborwert_admin/$', 'showLaborwert_admin', name='showLaborwert_admin'),
    url(r'^anzeigeLaborwerttyp/$', 'showLaborwerttyp', name='showLaborwerttyp'),
    url(r'^anzeigeEinheit/$', 'showEinheit', name='showEinheit'),
    url(r'^anzeigeWertigkeit/$', 'showWertigkeit', name='showWertigkeit'),
    url(r'^anzeigeMaleMinMax/$', 'showMaleMinMax', name='showMaleMinMax'),
    url(r'^anzeigeFemaleMinMax/$', 'showFemaleMinMax', name='showMinMax'),

    url(r'^toggleLaborwert/(?P<laborwert_id>\d+)/$', 'deleteToggleLaborwert', name='deleteToggleLaborwert'),

    url(r'^editLaborwert/(?P<laborwert_id>\d+)/$', 'editLaborwert', name='editLaborwert'),
    url(r'^editLaborwerttyp/(?P<laborwerttyp_id>\d+)/$', 'editLaborwerttyp', name='editLaborwerttyp'),
    url(r'^editEinheit/(?P<einheit_id>[a-z]+)/$', 'editEinheit', name='editEinheit'),
    url(r'^editWertigkeit/(?P<wertigkeit_id>\d+)/$', 'editWertigkeit', name='editWertigkeit'),
    url(r'^editMinMax/(?P<male_id>\d+)/$', 'editMaleMinMax', name='editMaleMinMax'),
    url(r'^editMinMax/(?P<female_id>\d+)/$', 'editFemaleMinMax', name='editFemaleMinMax'),
)