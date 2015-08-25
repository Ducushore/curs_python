# Program Tema_in_clasa_slide66
# Demonstreaza utilizarea obiectelor
# Ion Stundentul - 1/26/13



class Clasa1(object):
    """Clasa mostenita"""

    def __init__(self, marca, tip):
        """ parametrii intrare"""
        self.marca= marca
        self.tip=tip

    def Culoare(self,culoare):
        """Creaza culoare"""
        self.culoare = culoare
        
    def AfisareCuloare(self):
        """Afiseaza culoare"""
        return self.culoare

class Clasa2(Clasa1):
    """mosteneste clasa 1"""
    def ScauneIncal(self,rasp):
        """adauga argumentul scaune_incalzite"""
        self.scaune_incalzite = rasp

class Clasa3(Clasa1):
    """mosteneste clasa 1"""
    def OpticLed(self,rasp):
        """adauga argumentul scaune_incalzite"""
        self.Blocuri_Optice_LED = rasp

# main

car1 = Clasa2("ARO","M461")
car1.ScauneIncal("Da")
car1.Culoare("rosu")

car2 = Clasa3("Dacia","1310")
car2.OpticLed("Nu")
car2.Culoare("negru")

print "marca:",car1.marca
print "tip:",car1.tip
print "Scaune Electrice:",car1.scaune_incalzite
print "Culoare:",car1.AfisareCuloare()
print
print "marca:",car2.marca
print "tip:",car2.tip
print "Blocuri Optice LED:",car2.Blocuri_Optice_LED
print "Culoare:",car2.AfisareCuloare()


