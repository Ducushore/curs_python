# Fisier: sys-argv-exemplu.py

import sys

print "Numele programului este : ", sys.argv[0]

if len(sys.argv) > 1:
    print "Exista ", len(sys.argv)-1, "argumente"
    for arg in sys.argv[1:]:
        print arg
else:
    print "Nu exista argumente!"

