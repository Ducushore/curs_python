# Program clasa3
# Demonstreaza utilizarea metodei speciale __str__
# Ion Studentul - 1/26/13

class NumeClasa(object):
    """clasa mea"""
    def __init__(self,nume):
        """nume student"""
        self.nume= nume

    def __str__(self):
        """afiseaza toate caracteristicile"""
        return "metoda afisare:\t"+str(self.nume)

        
obiect1=NumeClasa("Ion Studentul")

print obiect1

raw_input("\n\nApasa <enter> pt a iesi.")
