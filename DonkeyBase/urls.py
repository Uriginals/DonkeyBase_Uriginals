from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DonkeyBase.views.home', name='home'),
    # url(r'^DonkeyBase/', include('DonkeyBase.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^studienverwaltung/', include('studienverwaltung.urls', namespace="studienverwaltung")),
    url(r'^patientenverwaltung/', include('patientenverwaltung.urls', namespace="patientenverwaltung")),
    url(r'^opverwaltung/', include('opverwaltung.urls', namespace="opverwaltung")),
    url(r'^laborwertverwaltung/', include('laborwertverwaltung.urls', namespace="laborwertverwaltung")),
    url(r'^benutzerverwaltung/', include('benutzerverwaltung.urls', namespace="benutzerverwaltung")),
)
