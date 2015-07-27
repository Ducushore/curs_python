# Functie parametrii default si keyword args
# Demonstreaza parametrii standard si argumente cheie
# Ion Stundentul - 1/26/13

# parametrii pozitionali
def ziNastere1(name, age):
    print "Salut,", name, "!", "Am auzit ca ai", age, "ani!.\n"

# parametrii cu valori standards
def ziNastere2(name = "Ion Studentul", age = 20):
    print "Salut,", name, "!", "Am auzit ca ai", age, "ani!.\n"
ziNastere1("Catalin", 20)
ziNastere1(20, "Catalin")
ziNastere1(name = "Catalin", age = 20)
ziNastere1(age = 20, name = "Catalin")

ziNastere2()
ziNastere2(name = "Maria")
ziNastere2(age = 18)
ziNastere2(name = "Maria", age = 18)
ziNastere2("Maria", 18)

raw_input("\n\nApasa <enter> pt a iesi.")
