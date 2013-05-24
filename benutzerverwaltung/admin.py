from django.contrib import admin
from benutzerverwaltung.models import *


class GruppeAdmin(admin.ModelAdmin):
    list_display = ['name']

class TabellenBerechtigungAdmin(admin.ModelAdmin):
    list_display = ['tabelle', 'perm']

class BerechtigungAdmin(admin.ModelAdmin):
    list_display = ['grpID', 'tbID']

class BerechtigungBeschreibungAdmin(admin.ModelAdmin):
    list_display = ['berechtigung', 'name']

class UserGruppeAdmin(admin.ModelAdmin):
    list_display = ['grpID']


admin.site.register(Gruppe, GruppeAdmin)
admin.site.register(Tabelle_Berechtigung, TabellenBerechtigungAdmin)
admin.site.register(Gruppe_Berechtigung, BerechtigungAdmin)
admin.site.register(Berechtigung_Beschreibung, BerechtigungBeschreibungAdmin)