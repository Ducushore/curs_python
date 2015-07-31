# Program clasa5
# Demonstreaza concepte clase
# Ion Stundentul - 1/26/13

class NumeClasa(object):
    """clasa mea"""
    def __init__(self):
        self.numarInstante= 0

print ("cream 4 obiecte!")
obiect1=NumeClasa()
obiect2=NumeClasa()
obiect3=NumeClasa()
obiect4=NumeClasa()

#vizualizam argumentul numarInstante
print("vizualizam argumentul numarInstante!")
print obiect1.numarInstante
print obiect2.numarInstante
print obiect3.numarInstante
print obiect4.numarInstante

print ("modificam argumentul numarInstante!")
obiect1.numarInstante=0
obiect2.numarInstante=1
obiect3.numarInstante=2
obiect4.numarInstante=30

print("vizualizam argumentul numarInstante modificat!")
print obiect1.numarInstante
print obiect2.numarInstante
print obiect3.numarInstante
print obiect4.numarInstante
print NumeClasa.numarInstante

raw_input("\n\nApasa <enter> pt a iesi.")
