from django import forms
from inscription.models import Joueur, Tournoi, Participant

class FicheInscriptionForm(forms.Form):
  OPTIONS = (
    (u'2X-solo', u'Super Street Fighter 2X 1v1'),
    (u'2X-mirror', u'Super Street Fighter 2X 1v1 Mirror'),
    (u'2X-team', u'Super Street Fighter 2X 3v3'),
    (u'SF4-solo', u'Super Street Fighter 4 Arcade Edition 1v1'),
    (u'SF4-team', u'Super Street Fighter 4 Arcade Edition 2v2 Ratio'),
    (u'Breakers', u'Breakers Revenge 1v1'),
    (u'Cvs2-apo', u'Capcom vs Snk 2 1v1 Apocalypse'),
    (u'Cvs2-team', u'Capcom vs Snk 2 2v2 Team'),
    (u'UMvC3', u'Ultimate Marvel vs Capcom 3 1v1'),
    (u'SC5', u'SoulCalibur 5 1v1'),
    (u'3.3-team', u'Street Fighter 3.3 3v3'),
    (u'3.3-tier', u'Street Fighter 3.3 1v1 Tier List'),
    (u'TTT2', u'Tekken Tag Tournament 2 1v1'),
    (u'Kof13-solo', u'The King of Fighters 13 1v1'),
    (u'Kof-all-stars', u'The King of Fighters All Stars 2v2'),
    (u'Stuntacus', u'Stuntacus GodTiers of the Arena 1v1'),
    (u'Jojo', u'Jojo Bizarre Adventures All Star 1v1'),
    (u'BBCP', u'BlazBlue Chrono Phantasma 1v1'),
    )
  pseudo = forms.CharField(max_length=254, required=True)
  nom = forms.CharField(max_length=254, required=False)
  prenom = forms.CharField(max_length=254, required=False)
  email = forms.CharField(max_length=254, required=False)
  telephone = forms.CharField(max_length=254, required=False)
  num_commande = forms.CharField(max_length=254, required=False)
  tournois = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS, required=False)


