'''

LE BIHAN Raphaël

Patate : exemple d'utilisation de l'héritage des classes
NB : je ne connais pas trop la syntaxe de python orienté objet donc il y aura peut être quelques erreurs de forme

'''


'''

fichier : PatateClassique.py
définition d'une patate, et de ses caractéristiques

'''

from Patate import Patate
from MaladieTranquille import MaladieTranquille
from MaladieProgressive import MaladieProgressive

class PatateClassique(Patate):

	def apparitionMaladies(self):
		"""Renvoie les différentes maladies, avec la proba d'apparition de la maladie."""
		return [(MaladieTranquille(),0.05), (MaladieProgressive(),0.01)]
