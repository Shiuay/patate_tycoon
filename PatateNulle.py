'''

LE BIHAN Raphaël

Patate : exemple d'utilisation de l'héritage des classes
NB : je ne connais pas trop la syntaxe de python orienté objet donc il y aura peut être quelques erreurs de forme

'''


'''

fichier : PatateNulle.py
définition d'une patate peu résistante aux maladies

'''

from Patate import Patate
from MaladieTranquille import MaladieTranquille
from MaladieProgressive import MaladieProgressive

class PatateNulle(Patate):

	def apparitionMaladies():
		"""Renvoie les différentes maladies, avec la proba d'apparition de la maladie."""
		return [(MaladieTranquille(),0.3), (MaladieProgressive(),0.1)]
