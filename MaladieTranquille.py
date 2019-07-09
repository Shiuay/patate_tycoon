'''

LE BIHAN Raphaël

Patate : exemple d'utilisation de l'héritage des classes
NB : je ne connais pas trop la syntaxe de python orienté objet donc il y aura peut être quelques erreurs de forme

'''


'''

fichier : MaladieTranquille.py
définition d'une maladie pas trop dangereuse

'''

from Maladie import Maladie

class MaladieTranquille(Maladie):

# on réécrit par dessus la méthode générique de Maladie.py

	def ticMaladie(self, patate):
		"""Enlève un petit peu de HP à la patate."""

		patate.hp -= 1
