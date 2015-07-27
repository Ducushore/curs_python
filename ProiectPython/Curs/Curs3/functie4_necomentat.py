# Functie ce demonstreaza namespace-urile
# Demonstreaza mespace-urile
# Ion Stundentul - 1/26/13

#variabilele globale
nume="Ion Studentul"
fructe=3

print "--------------------program namespace------------------"
# definitii 
def AreMere(num):
    """Foloseste paramentrul num si incr variabila globala
    De asemenea se modifica si o variabila locala"""
    print "Functia AreMere:"
    print "Salut, ", num, "!", "Ai ",fructe," mere?."
    print num+" al doilea\n"

def ArePere():
    print "Functia ArePere:"
    """Foloseste nume variabila globala"""
    print "Salut,", nume, "! \n"

def FaraEroare():
    """Nu incearca sa modifice o variabila globala- genereaza eroare"""
    print "Functia FaraEroare:"
    print fructe
    
def Eroare():
    """Incearca sa modifice o variabila globala- genereaza eroare"""
    print "Functia Eroare:"  
    print fructe
    fructe+=fructe

#main
AreMere(nume)
ArePere()
FaraEroare()
Eroare()  # linie decomentata pt. a vedea programul cu errori

raw_input("\n\nApasa <enter> pt a iesi.")
