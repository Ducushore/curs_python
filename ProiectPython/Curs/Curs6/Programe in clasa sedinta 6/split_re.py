# Program RE 2
# Explica regular exp
# Ion Studentul - 1/26/13

import re

sir = """Aseara am mancat un hotdog mare."""

m = re.split("(d\w+)", sir)
if m:
    print m