# Program RE 3
# Explica regular exp
# Ion Studentul - 1/26/13

import re

sir = """Aseara am mancat un hotdog mare."""

m = re.search("(d\w+)", "carnat" , sir)
if m:
    print(m.groups())