from django.contrib import admin
from inscription.models import Joueur
from inscription.models import Tournoi
from inscription.models import Participant

# Register your models here.
class JoueurAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'nom', 'num_commande', 'infos')
    search_fields = ['pseudo','num_commande']

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('titre_tournoi', 'pseudo')
    search_fields = ['pseudo']

class TournoiAdmin(admin.ModelAdmin):
    list_display = ('jeu', 'date', 'nb_max', 'prix')
    list_filter = ['date']
    date_hierarchy = 'date'

admin.site.register(Joueur, JoueurAdmin)
admin.site.register(Tournoi, TournoiAdmin)
admin.site.register(Participant, ParticipantAdmin)

