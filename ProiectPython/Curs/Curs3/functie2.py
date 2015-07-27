# Functie input si output
# Demonstreaza parametrii si valorile returnate
# Ion Stundentul - 1/26/13

Nrlist={1:True,2:False,3:False,4:False,5:True,6:False,7:False,8:False,9:False}
raspDaNu=None


def Afiseaza(mesaj):
    """ Afiseaza un mesaj dat."""
    print "Acesta este mesajul: "+str(mesaj).upper()+"!"
    
def Intreaba_da_nu():
    """ Intreaba da sau nu."""
    raspuns = None
    while raspuns not in ("d", "n"):
        print "Raspunde prin \"d\" sau \"n\"."
        raspuns = raw_input().lower()
    if (raspuns=="d"):
        raspuns="da"
    elif (raspuns=="n"):
        raspuns="nu"
    else:
        pass
    print "Raspunsul ales de tine este "+raspuns

def Returneaza(numar):
    """ Verifica daca exista in  este marcata sau nu."""
    if(numar in Nrlist):
        if(Nrlist[numar]==False):
            return "marcat ca fals"
        else:
            return "marcat ca adevarat"
    else:
        return "nemarcat"



#rulare
Afiseaza("Salut Python.\n")

nr = Returneaza(2)
print "Iata ce ne returneaza Returneaza(2):", nr,"\n"

raspuns = Intreaba_da_nu()

raw_input("\n\nApasa <enter> pt a iesi.")