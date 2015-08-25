# Program Pickle
# Explica utilizarea modulului Pickle
# Ion Studentul - 1/26/13

import cPickle

nume = {1:"Popescu", 2:"Scaraoski", 3:"Mahomed",4:"McDonald"}
pasari=["vrabie","vultur","porumbel","corb"]

fisier = open("pickle_1.bazadedate", "w")

cPickle.dump(nume, fisier)
cPickle.dump(pasari, fisier)

fisier.close()


fisier_citit = open("pickle_1.bazadedate", "r")

nume_citit = cPickle.load(fisier_citit)
pasari_citit = cPickle.load(fisier_citit)

print nume_citit
print pasari_citit

raw_input("\n\nApasa <enter> pt a iesi.")