__author__ = 'Nico'
from django.contrib import admin
from opverwaltung.models import OperationsArt, Seite, Tumorstadium,Operation, Operateur, Assistent

class OperationAdmin(admin.ModelAdmin):
    list_display = ['oID', 'art']

class OperationsArtAdmin(admin.ModelAdmin):
    list_display = ['bezeichnung']

class SeiteAdmin(admin.ModelAdmin):
    list_display = ['bezeichnung']

class TumorstadiumAdmin(admin.ModelAdmin):
    list_display = ['tID','bezeichnung']

class OperateurAdmin(admin.ModelAdmin):
    list_display = ['operateur']

class AssistentAdmin(admin.ModelAdmin):
    list_display = ['assistent']

admin.site.register(Operation, OperationAdmin)
admin.site.register(OperationsArt, OperationsArtAdmin)
admin.site.register(Seite, SeiteAdmin)
admin.site.register(Tumorstadium, TumorstadiumAdmin)
admin.site.register(Operateur, OperateurAdmin)
admin.site.register(Assistent, AssistentAdmin)