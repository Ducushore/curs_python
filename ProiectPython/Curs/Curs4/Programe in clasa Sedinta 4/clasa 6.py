# Program clasa6
# Demonstreaza utilizarea obiectelor
# Ion Stundentul - 1/26/13

class NumeClasa(object):
    """clasa mea"""
    tipuriCarte = {"caro","trefla","inima rosie","inima neagra"}
    numereCarte = {"2","3","4","5","6","7","8","9","10","A","J","Q","K"}
    
    def __init__(self,tip,nr):
        """initializeaza variablie"""
        self.tip = tip
        self.nr  = nr
        self.matchTip = 0
        self.matchNr  = 0
        

    def __str__(self):
        """afiseaza toate caracteristicile"""
        if self.tip in NumeClasa.tipuriCarte:
            self.matchTip=1
        if self.nr in NumeClasa.numereCarte:
            self.matchNr=1
        if self.matchNr==1 and self.matchTip==1:
            ret=" "
        else:
            ret = " nu "
        
        return "Numarul si tipul ales de tine"+ret+"exista in packetul de carti!\n Valori:"+self.tip+","+self.nr
    
#cream primul obiect         
obiect1=NumeClasa("caro","2")
print obiect1
print "\n"

#cream al doilea obiect
obiect2=NumeClasa("2","verde")
print obiect2
print "\n"

#altertam primul obiect 
obiect1.nr="4"
print obiect1
print "\n"

#alteram al doilea obiect
obiect2.matchTip=1
obiect2.matchNr=1
print obiect2
print "\n"


raw_input("\n\nApasa <enter> pt a iesi.")
