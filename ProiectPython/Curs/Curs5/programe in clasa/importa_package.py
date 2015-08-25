# Program importa package
# Explica crearea unui package
# Ion Studentul - 1/26/13

print "metoda 1"
import  package_test.cub_1
import  package_test.prog_a
#nume director.nume fisier.functie


#returneaza cubul unui numar
print "cubul numarului 3 este :", package_test.cub_1.cub(3)

#vom da argumentele: ratie=1,primul element=3, nr de elemente=5
print "Suma progresiei aritmetice este: ",  package_test.prog_a.pa(1,3,5)
#returneaza progresia aritmetica

print "metoda 2"
from  package_test.cub_1 import cub
from  package_test.prog_a import pa

#returneaza cubul unui numar
print "cubul numarului 3 este :",cub(3)

#vom da argumentele: ratie=1,primul element=3, nr de elemente=5
print "Suma progresiei aritmetice este: ", pa(1,3,5)
#returneaza progresia aritmetica

print "metoda 3"
from  package_test.cub_1 import cub as CeVreauEu

from  package_test.prog_a import pa as CeVreiTu

#returneaza cubul unui numar
print "cubul numarului 3 este :",CeVreauEu(3)

#vom da argumentele: ratie=1,primul element=3, nr de elemente=5
print "Suma progresiei aritmetice este: ", CeVreiTu(1,3,5)
#returneaza progresia aritmetica

print "metoda 4"
from  package_test import cub_1
from  package_test import prog_a

print "cubul numarului 3 este :",cub_1.cub(3)
print "Suma progresiei aritmetice este: ", prog_a.pa(1,3,5)

raw_input("\n\nApasa <enter> pt a iesi.")
