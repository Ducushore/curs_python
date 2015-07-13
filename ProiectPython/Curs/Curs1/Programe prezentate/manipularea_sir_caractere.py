# Manipularea sir caractere 
# Demonstreaza  manipularea variabilelor ce conti un sir de caractere
# Ion Studentul 1/13/03

# Citat Presedinte IBM, Thomas Watson, in 1943
citat = "I think there is a world market for maybe five computers."
print "Citat original:"
print citat

print "\nIn litere mari:"
print citat.upper()

print "\nIn litere mici:"
print citat.lower()

print "\nCa titul:"
print citat.title()

print "\nCu o mica schimbare:"
print citat.replace("five", "millions of")

print "\nCitatul original este inca :"
print citat

print "\nVerificare daca variabila este un sir de caractere format numai \
din numere:"
print citat.isdigit()# exclusiv cifre

print "\nVerificare daca variabila este sir de caractere format din \
caractere alpha:"

print citat.isalpha() # exclusiv litere

citat_modificat= citat.replace(" ","")
citat_modificat= citat_modificat.replace(".","")

print "\nVerificare daca variabila este sir de caractere format din caractere alpha:"
print citat_modificat.isalpha()

raw_input("\n\nApasa <enter> pt a iesi.")

