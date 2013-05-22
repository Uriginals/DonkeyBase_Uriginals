from django.contrib import admin
from benutzerverwaltung.models import *

class BenutzerAdmin(admin.ModelAdmin):
    list_display = ['benutzername', 'password']

class BerechtigungBeschreibungAdmin(admin.ModelAdmin):
    list_display = ['berechtigung', 'name']

class GruppeAdmin(admin.ModelAdmin):
    list_display = ['grpID', 'name']

class TabellenBerechtigungAdmin(admin.ModelAdmin):
    list_display = ['tbID', 'tabellen', 'perm']

class BerechtigungAdmin(admin.ModelAdmin):
    list_display = ['grpID', 'tbID']

admin.site.register(Benutzer, BenutzerAdmin)
admin.site.register(BerechtigungBeschreibung, BerechtigungBeschreibungAdmin)
admin.site.register(Gruppe, GruppeAdmin)
admin.site.register(TabellenBerechtigung, TabellenBerechtigungAdmin)
admin.site.register(Berechtigung, BerechtigungAdmin)