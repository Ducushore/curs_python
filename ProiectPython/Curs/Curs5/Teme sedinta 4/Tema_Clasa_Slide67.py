# Program Citire fisiere
# Explica accesarea fisierelor
# Ion Studentul - 1/26/13

print "\nCiteste toate liniile si le adauga intr-o lista cate o linie pe element."
text_file = open("Tema_Clasa.ini", "a+")
linii = text_file.readlines()
print linii

print "\n Am scris linia 4"
text_file.write("\nEU SUNT 4")
text_file.close()

text_file = open("Tema_Clasa.ini", "r")
print "Fisier recitit\n",text_file.read(),"\nfisier recitit" #citeste toate liniile intr-un sir de caracter
text_file.close()
