# Program clasa3
# Demonstreaza utilizarea static atibutes
# Ion Stundentul - 1/26/13

class NumeClasa(object):
    """clasa mea"""
    total=0
    def __init__(self,nume):
        """nume student"""
        self.nume= nume
        NumeClasa.total+=1

    def metodaAfisare(self):
        """afiseaza toate caracteristicile"""
        print "metoda afisare\t", self.nume
        print "avem ", NumeClasa.total ,"obiecte!"
        
obiect1=NumeClasa("Ion Studentul")
obiect2=NumeClasa("Mihai Studentul")
obiect3=NumeClasa("Mihai Studentu13")

variabila = obiect1.metodaAfisare()
obiect2.metodaAfisare()
obiect3.metodaAfisare()

raw_input("\n\nApasa <enter> pt a iesi.")



