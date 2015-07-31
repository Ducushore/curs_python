# Program Citire fisiere
# Explica accesarea fisierelor
# Ion Studentul - 1/26/13

print "\nDeschiderea si inchidera fisierului."
text_file = open("text_importat1.txt", "r")
text_file.close()

print "\nDeschiderea  fisierului."
text_file = open("text_importat1.txt", "r")
print text_file.read() #citeste toate liniile intr-un sir de caracter
text_file.close()

print "\nCiteste doua carctere dintr-o linie."
text_file = open("text_importat1.txt", "r")
print text_file.readline() # Prima linie
print text_file.readline() # A doua linie
print text_file.readline() # A treia linie
text_file.close()

print "\nCiteste toate liniile si le adauga intr-o lista cate o linie pe element."
text_file = open("text_importat1.txt", "r")
linii = text_file.readlines()
print linii
print len(linii)

for linie in linii:
    print linie
text_file.close()

print "\n Parcurcerea prin fisier linie cu linie."
text_file = open("text_importat1.txt", "r")
for linie in text_file:
    print linie
text_file.close()

raw_input("\n\nApasa <enter> pt a iesi.")
