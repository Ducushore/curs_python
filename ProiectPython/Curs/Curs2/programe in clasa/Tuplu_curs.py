# inventar de joc
# Demonstreaza tuplu
# Ion Studentul - 1/26/13

inventar = None
print "Acest program sustine inventarul unui personaj dintr-un joc.\n"
# tratarea tuplului ca o conditie 

if (not inventar):
    print "Momentan nu ai nici o arma in inventar."

#crearea de tuplu cu articole in inventar
inventar = ("sabie","armura","scut","potiune de vindecare")    

# afisarea tuplului
print "\nTuplul inventar este acum :\n", inventar

# afisarea fiecarui element din tuplu
print "\nElementele inventarului sunt:"
for item in inventar:
    print "=>",item

print "\n\nlungimea inventarului este: " , len(inventar)
print "\nElementul al doilea din inventar este: ",inventar[1]

raw_input("\n\nApasa <enter> pt a iesi.")
