# inventar de joc
# Demonstreaza lista
# Ion Stundentul - 1/26/13

#crearea unei liste cu articole in inventar
inventar = ["sabie","armura","scut", "potiune de vindecare"]    


# afisarea listei
print "\nLista inventar este :\n", inventar

# afisarea fiecarui element din listei
print "\nElementele inventarului sunt:"
for item in inventar:
    print "=>",item

print "\n\nlungimea inventarului este: " , len(inventar)
jumateInv= len(inventar)/2
print "\nElementul al ", jumateInv+1 ," din inventar este: ",
inventar[jumateInv]
#Folosim jumateInv+1 deoarece primul element este 0.

print "Ai gasit un cufar cu potiune magica ."
print "lista inventar1",inventar
cufar=["potiune magica"]
inventar+=cufar
#inventar=inventar+cufar

print "lista inventar2",inventar

# afisarea listei
print "\nLista inventar este acum :\n", inventar

print "\nAi gasit o spada foarte buna asa ca ai aruncat sabia .\n"
inventar[0]= "spada"
# afisarea listei
print "Lista inventar este acum :\n", inventar


raw_input("\n\nApasa <enter> pt a iesi.")
