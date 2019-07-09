'''

LE BIHAN Raphaël

Patate : exemple d'utilisation de l'héritage des classes
NB : je ne connais pas trop la syntaxe de python orienté objet donc il y aura peut être quelques erreurs de forme

'''


'''

fichier : PatateContagieuse.py
définition d'une patate, et de ses caractéristiques

'''

from Patate import Patate
from MaladieTranquille import MaladieTranquille
from MaladieProgressive import MaladieProgressive

class PatateContagieuse(Patate):

# les patates de cette variété se transmettent facilement leurs maladies : plus il existe de patates de cette variété, plus leur probabilité de tomber malade est élevé

	nombrePatates = 0

	def __init__(self):
		Patate.__init__(self)
		self.nombrePatates += 1

	def apparitionMaladies(self):
		"""Renvoie les différentes maladies, avec la proba d'apparition de la maladie."""
		return [(MaladieTranquille(),0.05 * self.nombrePatates), (MaladieProgressive(),0.01 * self.nombrePatates)]
