from inscription.models import Joueur, Tournoi, Participant
from tables import JoueurTable
from forms import FicheInscriptionForm
from django.shortcuts import get_object_or_404, render, render_to_response, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django_tables2 import RequestConfig

def joueur_table_view(request):
  table = JoueurTable(Joueur.objects.all())
  RequestConfig(request).configure(table)
  return render(request, 'inscription/joueur_list.html', {'liste_joueurs': table})

def profil_joueur(request, pseudo_joueur):
  joueur = Joueur.objects.get(pk=pseudo_joueur)
  liste_tournoi_inscrit = Participant.objects.filter(pseudo=joueur.pseudo).values_list('titre_tournoi', flat=True)

  if request.method == 'POST':
    print 'lol'
    return render(request, 'inscription/inscription.html', {'form': form})
  else:
    form = FicheInscriptionForm(initial={
      'pseudo': joueur.pseudo,
      'nom': joueur.nom,
      'num_commande': joueur.num_commande,
      'infos': joueur.infos,
      'tournois': liste_tournoi_inscrit,
      })
    return render(request, 'inscription/inscription.html', {'form': form})

def joueurs_inscrits_liste(request, tournoi_titre):
  liste_joueurs = Participant.objects.filter(titre_tournoi = tournoi_titre).order_by('pseudo')
  nb_places = Tournoi.objects.get(titre = tournoi_titre).nb_max - liste_joueurs.count()
  return render(
      request,
      'inscription/participants_tournoi.html',
      {'liste_joueurs': liste_joueurs, 'titre_tournoi': tournoi_titre, 'nb_places': nb_places})

def fiche_inscription(request):
  if request.method == 'POST':
    form = FicheInscriptionForm(request.POST)
    # Un formulaire valide est juste un formulaire dont le champ pseudo est renseigne
    if form.is_valid():
      # recuperation des informations du joueur
      pseudo = form.cleaned_data['pseudo']
      nom = form.cleaned_data['nom']
      infos = form.cleaned_data['infos']
      num_commande = form.cleaned_data['num_commande']

      joueur = Joueur(
          pseudo=pseudo,
          nom=nom,
	  infos=infos,
          num_commande=num_commande)

      # on le sauvegarde/update dans la base
      joueur.save()

      # inscription aux tournois coches
      # on recupere les cases tournois coches
      liste_tournoi_inscrit = form.cleaned_data['tournois']
      # pour chaque tournoi coche
      for tournoi_inscrit in liste_tournoi_inscrit:
        # si il n est pas deja inscrit au tournoi
        if not Participant.objects.filter(pseudo=pseudo, titre_tournoi=tournoi_inscrit).exists():
          # recuperation des participants au tournoi
          participants_tournoi = Participant.objects.filter(titre_tournoi = tournoi_inscrit)
          # recuperation des informations du tournoi en question
          tournoi = Tournoi.objects.get(titre=tournoi_inscrit)
          # si le tournoi est plein
          if tournoi.nb_max <= participants_tournoi.count():
            # redirection vers la page du tournoi
            return redirect('/inscription/tournoi/'+tournoi.titre)
          # ajout de la participation au tournoi 
          participant = Participant.objects.create(pseudo=joueur, titre_tournoi=tournoi)
        #endif
      #endfor

      # desinscription des tournois decoches
      # on recupere les inscription aux tournois qui ont ete decochees
      liste_tournoi_non_inscrit = Participant.objects.exclude(titre_tournoi__in=liste_tournoi_inscrit).filter(pseudo=pseudo)
      print liste_tournoi_non_inscrit

      liste_tournoi_non_inscrit.delete()
      

    return redirect('/inscription/liste_joueurs/')

  else:
    form = FicheInscriptionForm()

  return render( request, 'inscription/inscription.html', {'form': form} )
