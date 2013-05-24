__author__ = 'Nico'

from django.conf.urls import patterns, url

urlpatterns = patterns('patientenverwaltung.views',

    # ex: /patientenverwaltung/
    url(r'^$', 'index', name='index'),

    url(r'^admin/$', 'admin', name='admin'),

    url(r'^erstellenPatient/$', 'addPatient', name='addPatient'),
    url(r'^erstellenPLZ/$', 'addPLZ', name='addPLZ'),
    url(r'^erstellenHausarzt/$', 'addHausarzt', name='addHausarzt'),
    url(r'^erstellenPatientenArt/$', 'addPatientenArt', name='addPatientenArt'),
    url(r'^erstellenEigenschaft/$', 'addEigenschaft', name='addEigenschaft'),
    url(r'^erstellenZusatzID/$', 'addZusatzID', name='addZusatzID'),

    url(r'^anzeigePatient/$', 'showPatient', name='showPatient'),
    url(r'^anzeigePatient_admin/$', 'showPatientAdmin', name='showPatientAdmin'),
    url(r'^anzeigePLZ/$', 'showPLZ', name='showPLZ'),
    url(r'^anzeigeHausarzt/$', 'showHausarzt', name='showHausarzt'),
    url(r'^anzeigePatientenArt/$', 'showPatientenArt', name='showPatientenArt'),
    url(r'^anzeigeEigenschaft/$', 'showEigenschaft', name='showEigenschaft'),
    url(r'^anzeigeZusatzID/$', 'showZusatzID', name='showZusatzID'),

    url(r'^editPatient/(?P<patient_id>\d+)/$', 'editPatient', name='editPatient'),
    url(r'^editPLZ/(?P<plz_id>\d+)/$', 'editPLZ', name='editPLZ'),
    url(r'^editHausarzt/(?P<arzt_id>\d+)/$', 'editHausarzt', name='editHausarzt'),
    url(r'^editPatientenArt/(?P<art_id>[a-z A-Z]+)/$', 'editPatientenArt', name='editPatientenArt'),
    url(r'^editEigenschaft/(?P<eig_id>[a-z A-Z]+)/$', 'editEigenschaft', name='editEigenschaft'),
    url(r'^editZusatzID/(?P<zus_id>\d+)/$', 'editZusatzID', name='editZusatzID'),

    url(r'^togglePatient/(?P<patient_id>\d+)/$', 'deleteTogglePatient', name='deleteTogglePatient'),

    url(r'^deletePLZ/(?P<plz_id>\d+)/$', 'deletePLZ', name='deletePLZ'),
    url(r'^deleteArzt/(?P<arzt_id>\d+)/$', 'deleteHausarzt', name='deleteHausarzt'),
    url(r'^deletePatientenArt/(?P<art_id>[a-z A-Z]+)/$', 'deletePatientenArt', name='deletePatientenArt'),
    url(r'^deleteEigenschaft/(?P<eig_id>[a-z A-Z]+)/$', 'deleteEigenschaft', name='deleteEigenschaft'),
    url(r'^deleteZusatzID/(?P<zus_id>\d+)/$', 'deleteZusatzID', name='deleteZusatzID'),

)