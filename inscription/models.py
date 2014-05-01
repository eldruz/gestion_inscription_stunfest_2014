from django.db import models

class Joueur(models.Model):
    pseudo = models.CharField(max_length=254, primary_key=True)
    nom = models.CharField(max_length=254,blank=True,null=True)
    num_commande = models.CharField(max_length=254,blank=True,null=True)
    infos = models.CharField(max_length=254,blank=True,null=True)

    def __unicode__(self):
        return self.pseudo

    def clean(self):
      if not self.pseudo:
        raise ValidationError('Il faut un pseudo')



class Tournoi(models.Model):
    LISTE_JEUX = (
            (u'2X', u'Super Street Fighter 2X'),
            (u'SF4', u'Super Street Fighter 4 Arcade Edition'),
            (u'Breakers', u'Breakers Revenge'),
            (u'Cvs2', u'Capcom vs Snk 2'),
            (u'UMvC3', u'Ultimate Marvel vs Capcom 3'),
            (u'SC5', u'SoulCalibur 5'),
            (u'3.3', u'Street Fighter 3.3'),
            (u'TTT2', u'Tekken Tag Tournament 2'),
            (u'Kof13', u'The King of Fighters 13'),
            (u'Kof', u'The King of Fighters All Stars'),
            (u'Stuntacus', u'Stuntacus GodTiers of the Arena'),
            (u'Jojo', u'Jojo Bizarre Adventures All Star'),
            (u'BBCP', u'BlazBlue Chrono Phantasma'),
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

