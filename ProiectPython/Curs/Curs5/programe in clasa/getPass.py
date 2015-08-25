# Program GetPass
# Explica functiile getPass
# Ion Studentul - 1/26/13

import getpass

usr = getpass.getuser()# returneaza userul logat

passw = getpass.getpass("Introdu parola pentru userul "+usr+":")

print usr, passw

raw_input("\n\nApasa <enter> pt a iesi.")