# Program Tema_RE.py
# Explica functiile RE si os.popen
# Ion Studentul - 1/26/13

import os,re
print "aplicam comanda date in consola"

stdin, stdout = os.popen2('date /t')
stdin.close()

print "Citim output"
captura = stdout.read()

print "Afisam output"
print captura

print "Cautam cu ajutorul modulului re anul curent"
cauta=re.search("(\d{4,4})",captura)
if cauta:
    print cauta.group(0)

raw_input("Apasa <<enter>> sa iesi!")
