'''

LE BIHAN Raphaël

Patate : exemple d'utilisation de l'héritage des classes
NB : je ne connais pas trop la syntaxe de python orienté objet donc il y aura peut être quelques erreurs de forme

'''


'''

fichier : Patate.py
définition d'une patate, et de ses caractéristiques

'''

from random import randint

class Patate:
	
	def __init__(self):
		self.hp = 100
		self.maladies = []

	def appliquerMaladies(self):
		for m in self.maladies:
			m.ticMaladie(self)

	def apparitionMaladies(self):
		"""fonction destinée à être remplacée par les fonctions des classes filles des différentes variétés de patate."""
		return None

	def genererMaladies(self):
		for (m,p) in self.apparitionMaladies():
			i = randint(1,100)
			if i <= 100*p:
				self.maladies.append(m)

	def ticPatate(self):
		self.genererMaladies()
		self.appliquerMaladies()






