from django.db import models

class Joueur(models.Model):
    pseudo = models.CharField(max_length=254, primary_key=True)
    nom = models.CharField(max_length=254,blank=True,null=True)
    prenom = models.CharField(max_length=254,blank=True,null=True)
    email = models.EmailField(max_length=254,blank=True,null=True)
    telephone = models.CharField(max_length=254,blank=True,null=True)
    num_commande = models.CharField(max_length=254,blank=True,null=True)

    def __unicode__(self):
        return self.pseudo

    def clean(self):
      if not self.pseudo:
        raise ValidationError('Il faut un pseudo')



class Tournoi(models.Model):
    LISTE_JEUX = (
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
    titre = models.CharField('Intitule du tournoi', max_length=254, primary_key=True)
    jeu = models.CharField(max_length=254, choices=LISTE_JEUX)
    support = models.CharField(max_length=254)
    date = models.DateTimeField('Date du tournoi')
    tournoi_format = models.CharField('Format du tournoi',max_length=254)
    nb_max = models.PositiveSmallIntegerField('Nombre maximum de joueurs')
    prix = models.PositiveSmallIntegerField('Prix du tournoi')

    def __unicode__(self):
        return self.titre

class Participant(models.Model):
    pseudo = models.ForeignKey(Joueur)
    titre_tournoi = models.ForeignKey(Tournoi)

    def __unicode__(self):
        return self.pseudo.__unicode__() + ' in ' + self.titre_tournoi.__unicode__()

