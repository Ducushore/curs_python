# Index Sir de caractere
# Demonstreaza indexarea sirului de caractere
# Ion Studentul - 1/27/03

iteratii=0
cuvantInvers=""

cuvant = raw_input("\n\nScrie un cuvant:\t")

print "Cuvantul tau este", cuvant, "\n"

high = len(cuvant)

print "Lungimea cuvantului este:",high

for var in cuvant:
    print cuvant[iteratii]," trebuie sa fie egal cu ", var
    iteratii+=1 #interatii = interatii+1
    cuvantInvers=var+cuvantInvers
    print cuvantInvers

print "\nCuvantul ales se scrie invers: ",cuvantInvers

raw_input("\n\nApasa <enter> pt a iesi.")
