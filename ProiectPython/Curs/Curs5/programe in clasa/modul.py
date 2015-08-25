# Program modul
# Explica crearea unui modul
# Ion Studentul - 1/26/13


def pa(ratie,primul_termen,nr_termeni):
    """ prgresie_aritmetica."""
    try:
        x=primul_termen*nr_termeni+(ratie*nr_termeni*(nr_termeni-1))/2
    except:
        x="Toate elementele trebuie sa fie numere"
    
    return x

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
