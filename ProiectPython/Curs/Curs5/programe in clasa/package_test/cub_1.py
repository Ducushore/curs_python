# Program cub
# Explica crearea unui package
# Ion Studentul - 1/26/13


def cub(nr=1):
    """ Ridicarea la cub."""
    try:
        raspuns=nr*nr*nr
    except:
        raspuns="Trebuie sa dai un numar"
    
    return raspuns

if __name__ == "__main__":
    print "Rulezi acest modul direct, deci nu va rula nimic. Importa acest modul."
    raw_input("\n\nApasa <enter> pt a iesi.")
