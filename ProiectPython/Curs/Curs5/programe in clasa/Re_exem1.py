# Program RE 1
# Explica regular exp
# Ion Studentul - 1/26/13

import re

# Sample strings.
list = ["Linia 1 este prima\n", "Linia doi este linia 2\n", "linia 3", "no match"]

# Loop.
for element in list:
    # Match if two words starting with letter d.
    m = re.match("(\w)*nia", element)

    # See if success.
    if m:
        print(m.group(0))

raw_input("\n\nApasa <enter> pt a iesi.")
