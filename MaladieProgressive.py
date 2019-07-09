'''

LE BIHAN Raphaël

Patate : exemple d'utilisation de l'héritage des classes
NB : je ne connais pas trop la syntaxe de python orienté objet donc il y aura peut être quelques erreurs de forme

'''


'''

fichier : MaladieProgressive.py
définition d'une maladie qui se développe au fur et à mesure

'''

from Maladie import Maladie

class MaladieProgressive(Maladie):

	def __init__(self):
		self.progression = 0


# on réécrit par dessus la méthode générique de Maladie.py

	def ticMaladie(self, patate):
		"""Enlève un petit peu de HP à la patate mais de plus en plus."""

		self.progression += 1
		patate.hp -= self.progression
