# Program modul
# Explica crearea unui modul
# Ion Studentul - 1/26/13


def Adunare(a,b):
    """ Adunare! functia are nevoie de doi parametrii"""
    try:
        x=a+b
    except:
        x="Cele doua elemente trebuie fie adunate/concatenate "
    
    return x

if __name__ == "__main__":
    print "Rulezi acest modul direct, deci nu va rula nimic. Importa acest modul."
    raw_input("\n\nApasa <enter> pt a iesi.")
