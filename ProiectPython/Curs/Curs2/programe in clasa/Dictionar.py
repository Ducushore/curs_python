# Dictionar de facebook
# Demonstreaza dicitonar
# Ion Stundentul - 1/26/13
dictionar={"ASAP": "As Soon As Possible-Cat mai repede posibil",
"ASL": "Age Sex Location-Varsta, sex, locatie",
"BRB": "Be Right Back-Revin imediat",
"FYI": "For Your Info-Pentru informatia ta",
"LOL": "Laugh out Loud-Rad tare",
"PM": "Private Message-mesaj pe privat",
"FRUMI":"Frumos"}

print"\nAccesam dictionarul pentru a vedea ce cuvinte cheie avem:"
print dictionar.keys()

print"\nAccesam dictionarul pentru a vedea ce  valori avem:"
print dictionar.values()

print "\nToate elementele dictionarului sunt:"
for elem in dictionar.keys():
    print "cheie:",elem ,"=> valoare:",dictionar[elem]
    
print "\nToate elementele dictionarului sunt:"
for elem in dictionar:
    print "cheie:",elem ,"=> valoare:",dictionar[elem]

#apelarea directa trebuie testat inainte pentru a nu genera eroare
if "BRB" in dictionar:
    print "\nCe inseamna BRB:",dictionar["BRB"],"\n"
    
#Exista cheia Frumi testarea modul alternativ
print "Exista cheia Frumi:",dictionar.has_key("Frumi")
print "Exista cheia FRUMI",dictionar.has_key("FRUMI")

raw_input("\n\nApasa <enter> pt a iesi.")



