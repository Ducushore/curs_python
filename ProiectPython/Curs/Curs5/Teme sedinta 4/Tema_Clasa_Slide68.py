# Program  Adunare cu doua metode
# Explica Try except si polimorfism
# Ion Studentul - 1/26/13

class Afisare():
    """Afiseaza suma sau imputirea a doua elemente"""
    def __init__(self, a, b):
        """retruneaza suma"""
        self.a = a
        self.b = b
        try:
            a+b
        except:
            print "Nu se poate adunare"
        else:
            print "Suma lor este "+ str(a+b)

    def __str__(self):
        """retruneaza produsul"""
        try:
            self.a*self.b
        except:
            return "Nu se poate inmultire"
        else:
            return "produsul lor este" + str(self.a*self.b)
        
o1 = Afisare("1","12")
print o1
print
o2 = Afisare(1,12)
print o2
print
o3 = Afisare("1",12)
print o3


