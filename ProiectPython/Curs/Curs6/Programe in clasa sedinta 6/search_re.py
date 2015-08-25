# Program RE 1
# Explica regular exp
# Ion Studentul - 1/26/13

import re

sir = """Aseara am mancat un hotdog mare."""

m = re.search("(d\w+)", sir)
if m:
    print(m.group(0))