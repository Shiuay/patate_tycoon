'''

LE BIHAN Raphaël

Patate : exemple d'utilisation de l'héritage des classes
NB : je ne connais pas trop la syntaxe de python orienté objet donc il y aura sans doute quelques erreurs de forme

'''


'''

fichier : main.py
fonctions principales, mécanique de jeu

'''

from PatateClassique import PatateClassique
from PatateContagieuse import PatateContagieuse
from MaladieTranquille import MaladieTranquille
from MaladieProgressive import MaladieProgressive

pa = []
pa.append(PatateClassique())
pa.append(PatateContagieuse())

for i in range(100):
	for i, p in enumerate(pa):
		p.ticPatate()
		string = str(type(p))[8:-2]
		classe = string[:len(string)//2]
		maladies_progressives = [maladie for maladie in p.maladies if type(maladie) == MaladieProgressive]
		maladies_tranquilles = [maladie for maladie in p.maladies if type(maladie) == MaladieTranquille]
		print("Patate{} : type {} : hp {} : maladies progressives {} : maladies tranquilles = {}".format(i, classe, p.hp, len(maladies_progressives), len(maladies_tranquilles)))
	print("\n")