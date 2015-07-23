# Manipularea sir caractere  prin if statement si repetarea prin while
# Demonstreaza  utilizarea sintaxei while
# Ion Studentul 1/13/03

print("\tSalut! \nAceasta e un program de conversie euro-lei")

while (True):
    euro=raw_input("\nScrie te rog valoarea euro:\n")

    if (euro.isdigit()):
        euro=int(euro)
        print "Valoarea convertita este :",euro*4.5," RON"
    else:
        print"Valoarea introdusa nu este un numar!"

    renunta=raw_input("\n\nApasa q pt a iesi si orice pt. a repeta conversia.\n")
    if (renunta.upper()=='Q'):
        break


print "\nLa revedere!"

