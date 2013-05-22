__author__ = 'Nico'

from django.conf.urls import patterns, url

urlpatterns = patterns('opverwaltung.views',

    # ex: /studienverwaltung/
    url(r'^$', 'index', name='index'),

    # ex: /studienverwaltung/...
    url(r'^erstellenSeite/$', 'addSeite', name='addSeite'),
    url(r'^erstellenOp/$', 'addOp', name='addOP'),
    url(r'^erstellenOpArt/$', 'addOpArt', name='addOpArt'),
    url(r'^erstellenTumor/$', 'addTumor', name='addTumor'),

    url(r'^anzeigeOp/$', 'showOp', name='showOP'),
    url(r'^anzeigeTumor/$', 'showTumor', name='showTumor'),
    url(r'^anzeigeSeite/$', 'showSeite', name='showSeite'),
    url(r'^anzeigeOpArt/$', 'showOpArt', name='showOPart'),

    url(r'^editOp/(?P<operation_id>\d+)/$', 'editOp', name='editOp'),
    url(r'^editOpArt/(?P<operation_id>\d+)/$', 'editOpArt', name='editOpArt'),
    url(r'^editSeite/(?P<operation_id>\d+)/$', 'editSeite', name='editSeite'),
    url(r'^editTumor/(?P<operation_id>\d+)/$', 'editTumor', name='editTumor'),
)