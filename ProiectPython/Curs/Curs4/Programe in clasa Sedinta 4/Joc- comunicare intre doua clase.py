# Program joc
# Demonstreaza apelarea unei clase in alta clasa 
# Ion Studentul - 1/26/13

class Inamic(object):
    """Inamic"""
    def __init__ (self):
        """initalizarea inamicului"""
        self.viata=10
    
    def Ranire(self,rana):
        """Inamicul e ranit"""
        self.viata=self.viata-rana
        print "Viata inamicului a ajuns la", self.viata
        if (self.viata<=0):
            print "Inamicul a murit!"

class Erou(object):
    """Erou"""
    def __init__(self):
        """initializarea eroului"""
        self.viata=100
        self.sabie=2
    def Atac(self,rana,inamic):
        """Inamicul va fi ranit!"""
        inamic.Ranire(rana)

    
        
EroulMeu=Erou()

inamic1=Inamic()
print "\nIntalnim primul inamic!Deci il atacam cu sabia"
EroulMeu.Atac(EroulMeu.sabie,inamic1)

print "\nVom aplica inamicului un atac special"
EroulMeu.Atac(20,inamic1)

raw_input("\n\nApasa <enter> pt a iesi.")



