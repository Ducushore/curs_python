# Program mostenire -joc2
# Explica mostenirea
# Ion Studentul - 1/26/13

class Fiinta(object):
    """creaza o serie de proprietati ale unei fiinte"""
    def __init__ (self):
        """proprietati mostenite de toate fiintele"""
        self.Reinviere()
        
    def Ranire(self,rana,fiinta_ranita):
        """fiinta eranita"""
        fiinta_ranita.viata=fiinta_ranita.viata-rana
        print "Viata a ajuns la", fiinta_ranita.viata, "(",fiinta_ranita.fiinta,")"
        if (fiinta_ranita.viata<=0):
            fiinta_ranita.viu=0
            print fiinta_ranita.fiinta," a murit!"
    def Reinviere(self):
        """reinvierea unei fiinte - reutilizarea inamicului sau a eroului"""
        self.viu=1
        self.viata=10
        self.sabie=2
        self.fiinta="inamic"
            
class Inamic(Fiinta):
    """Inamic"""
    
    def MetodaDegeaba(self):
        print "degeaba"    


class Erou(Fiinta):
    """Erou"""
    def Proprietati_initiale(self):
        """initializarea eroului"""
        self.viata=100
        self.sabie=4
        self.fiinta="erou"
        
print '\tBine ati venit la jocul "Cavalerul"'
#cream eroul nostru     
EroulMeu=Erou()
EroulMeu.Proprietati_initiale()
print "Iata proprietatile fiintei noastre(",EroulMeu.fiinta,"):"
print "viata :",EroulMeu.viata," puncte"
print "sabie :",EroulMeu.sabie," puncte vatamate din viata"
print EroulMeu.viu

inamic1=Inamic()
inamic1.MetodaDegeaba()
print "\nIntalnim primul ",inamic1.fiinta,"!Deci il atacam cu sabia"
print "Iata proprietatile fiintei intalnite(",inamic1.fiinta,"):"
print "viata :",inamic1.viata," puncte"
print "sabie :",inamic1.sabie," puncte vatamate din viata"
EroulMeu.Ranire(EroulMeu.sabie,inamic1)

print "Vom aplica inamicului un atac special!\n"
EroulMeu.Ranire(20,inamic1)

inamic1.Reinviere()
print "\nIntalnim al doilea ",inamic1.fiinta,"!Deci il atacam cu sabia"
print "Iata proprietatile fiintei intalnite(",inamic1.fiinta,"):"
print "viata :",inamic1.viata," puncte"
print "sabie :",inamic1.sabie," puncte vatamate din viata"
#EroulMeu.Ranire(EroulMeu.sabie,inamic1)
inamic1.viata=inamic1.viata-EroulMeu.sabie


print "Vom aplica inamicului un atac special!\n"
EroulMeu.Ranire(20,inamic1)

raw_input("\n\nApasa <enter> pt a iesi.")



