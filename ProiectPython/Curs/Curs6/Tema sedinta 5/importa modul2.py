# Program importa modul
# Explica crearea unui modul
# Ion Studentul - 1/26/13

import sys,os

if sys.platform == "win32":
    import modul2
else:
    sys.exit()

print os.getcwd()
os.chdir("D:\Catalin\Predare Python\carte\Sedinta 5")
print os.getcwd()
print modul2.Adunare("2","3")

raw_input("\n\nApasa <enter> pt a iesi.")
