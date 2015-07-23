'''
Dimineata de Vasile Alexandri
Zori de ziua se revarsa peste vesela natura, Prevestind un soare dulce cu lumina si caldura, In curand si el apare pe orizontul aurit, Sorbind roua diminetii de pe campul inverzit. El se-nalta de trei suliti pe cereasca mandra scara Si cu raze vii saruta june flori de primavara, Deditei si viorele, brebenei si toporasi Ce razbat prin frunze uscate si s-arata dragalasi.
'''


#a.Titlul sa fie indentat cu trei tab-uri si sa sune un beep la rulare utilizand secvente de evadare.
print "\t\t\t\aDimineata de Vasile Alexandri"

#b.Primele doua randuri sa fie printat utilizand ghilimelele triple formate din ghilimea simpla
print '''Zori de ziua se revarsa peste vesela natura, 
Prevestind un soare dulce cu lumina si caldura,'''

#c.Al treilea rand sa fie printat cate un cuvant pe o linie folosind virgula pentru ca textul sa fie afisat la rulare pe un singur rand.
print "In",
print "curand",
print "si",
print "el",
print "apare",
print "pe",
print "orizontul",
print "aurit,"

#d. Al patrulea rand sa fie printat ca o suma de siruri de caractere fiecare cuvand devenind propriul sir de caractere
print "Sorbind "+"roua "+"diminetii "+"de "+"pe "+"campul "+"inverzit."

#e. Randul 5 si randul 6 sa fie printat utilizand ghilimelele triple formate din ghilimea dubla
print """El se-nalta de trei suliti pe cereasca mandra scara 
Si cu raze vii saruta june flori de primavara,"""

#f. Randul 7 sa fie printat ca o variabila cu toate caracterele mari (folosind upper()).
rand7 = "Deditei si viorele, brebenei si toporasi"
caractereMari = rand7.upper()
print caractereMari

#g. Ultimul rand sa fie printat cu inceputul fiecarui cuvant cu litere mari (folosind title())
rand8 = "Ce razbat prin frunze uscate si s-arata dragalasi."
caractereTitle = rand8.title()
print caractereTitle

