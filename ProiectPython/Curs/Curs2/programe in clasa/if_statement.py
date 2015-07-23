# Manipularea sir caractere  prin if statement
# Demonstreaza  utilizarea sintaxei if
# Ion Studentul 1/13/03

print("\tSalut! \n  Aceasta e un program de conversie euro-lei")

euro=raw_input("\nScrie te rog valoarea euro:\n")

if (euro.isdigit()):
     euro=int(euro)
     print "Valoarea convertita este :",euro*4.5," RON"
else:
    print "Valoarea introdusa nu este un numar!"


raw_input("\n\nApasa <enter> pt a iesi.")


