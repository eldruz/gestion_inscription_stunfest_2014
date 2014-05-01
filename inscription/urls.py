from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from inscription.models import Joueur, Tournoi, Participant

# URLS pour le gestionnaire d'inscription

urlpatterns = patterns('',
        url(r'^liste_joueurs/$', 'inscription.views.joueur_table_view', name='liste_joueurs'),
        url(r'^inscription/$', 'inscription.views.fiche_inscription'),
        url(r'^profil/(?P<pseudo_joueur>.*?)/$','inscription.views.profil_joueur',name='profils'),
        url(r'^tournoi/(?P<tournoi_titre>.*)/$', 'inscription.views.joueurs_inscrits_liste', name='tournois'),
        )

