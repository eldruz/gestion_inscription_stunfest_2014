import django_tables2 as tables
from django_tables2.utils import A
from models import Joueur

class JoueurTable(tables.Table):
  pseudo = tables.TemplateColumn('<a href="/inscription/profil/{{record.pseudo}}/">{{record.pseudo}}</a>')
  class Meta:
    model = Joueur
    attrs = {"class": "paleblue"}
