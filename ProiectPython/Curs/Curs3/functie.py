# Functie meniu
# Demonstreaza utilizarea functiei
# Ion Stundentul - 1/26/13

def instructiuni():
    """ Afiseaza instructiunile jocului X si 0."""
    print \
    """
    Bine ati venit la incerarea intelectuala binecunoscuta sub numele de X si 0.
    Aceasta batalie se va da intre om si masina reprezentata de un procesor de silicon.

    Poti efectua o mutare prin introducerea unui numar intre 1 - 9, numar ce va fi corespondent pozitiei ilustrate in tabel:

                     1 | 2 | 3
                    -----------
                     4 | 5 | 6
                    -----------
                     7 | 8 | 9

    Imbarbateaza-te omule, caci ai nevoie!!! bataia incepe!\n
    """

# main
print "Iata instructiunile jocului X si 0:"
instructiuni()
print "Aplelarea se poate face de cate ori e nevoie:"
instructiuni()

raw_input("\n\nApasa <enter> pt a iesi.")
