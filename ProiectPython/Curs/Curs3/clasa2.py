# Program clasa2
# Demonstreaza utilizarea constructor
# Ion Stundentul - 1/26/13

class NumeClasa(object):
    """clasa mea"""
    def __init__(self,nume):
        """nume student"""
        self.nume= nume

    def metodaAfisare(self):
        """afiseaza toate caracteristicile"""
        print "metoda afisare\t", self.nume
        
obiect1=NumeClasa("Ion Studentul")

obiect1.metodaAfisare()
print "valoarea obiect1.nume este :",obiect1.nume

raw_input("\n\nApasa <enter> pt a iesi.")



