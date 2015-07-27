# Program clasa1
# Demonstreaza utilizarea clasei
# Ion Stundentul - 1/26/13

class NumeClasa(object):
    """clasa mea"""
    def metodaNume(self):
        """nume student"""
        self.nume= raw_input("cum se numeste studentul?\n")
    def metodaNotaPython(self,materie,nota):
        """setare materie/nota"""
        self.materie=materie
        self.nota=nota
    def metodaAfisare(self):
        """afiseaza toate caracteristicile"""
        print "metoda afisare\t", self.nume,"=",self.materie,":", self.nota
        
obiect1=NumeClasa()
obiect2=NumeClasa()

obiect1.metodaNume()
obiect1.metodaNotaPython("Python", "10")
obiect1.metodaAfisare()
print "valoarea obiect1.nume este :",obiect1.nume,"\n\n"

obiect2.metodaNume()
obiect2.metodaNotaPython("Python", "10+")
obiect2.metodaAfisare()
print "valoarea obiect2.nume este :",obiect2.nume,"\n\n"

print "valoarea obiect2.nume este :",obiect1.nume,"\n\n"

raw_input("\n\nApasa <enter> pt a iesi.")



