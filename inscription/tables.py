import django_tables2 as tables
from django_tables2.utils import A
from models import Joueur

class JoueurTable(tables.Table):
  pseudo = tables.LinkColumn('inscription:profils', args=[A('pseudo')])
  class Meta:
    model = Joueur
    attrs = {"class": "paleblue"}

