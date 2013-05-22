from django.contrib import admin
from studienverwaltung.models import *

class StudienArtAdmin(admin.ModelAdmin):
    list_display = ['bezeichnung']

class StudieAdmin(admin.ModelAdmin):
    list_display = ['bezeichnung', 'studienart', 'beschreibung', 'datum', 'freigegeben']
    list_filter = ['datum']

admin.site.register(StudienArt, StudienArtAdmin)
admin.site.register(Studie, StudieAdmin)