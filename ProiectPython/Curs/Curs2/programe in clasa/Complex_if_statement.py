# Manipularea sir caractere  prin if statement si elif
# Demonstreaza  utilizarea sintaxei if-elif
# Ion Studentul 1/13/03

print"\tSalut! \nAceasta e un program de conversie Euro->lei sau Lei->Euro"

alegereMoneda=raw_input("\nScrie L pt. conversia Euro->Lei si E pt. conversia  Lei->Euro:\n")
alegereMoneda=alegereMoneda.upper()

if (alegereMoneda.isalpha()):
    if (alegereMoneda=='L'):
        euro=raw_input("\nScrie nr. de euro ce doresti sa-l convertesti:\n")
        if (euro.isdigit()):
            euro=int(euro)
            print "Valoarea convertita este :",euro*4.55," RON"
        else:
            print "Valoarea introdusa nu este un numar!"

    elif (alegereMoneda=="E"):
        lei=raw_input("\nScrie nr. de lei ce doresti sa-l convertesti:\n")
        if (lei.isdigit()):
            lei=int(lei)
            print "Valoarea convertita este :",lei/4.55," EURO"
        else:
            print "Valoarea introdusa nu este un numar!"

    else:
        print "Valoarea introdusa nu este recunoscuta!" 
else:
    print "Valoarea introdusa nu este un caracater alfa!" 
    
raw_input("\n\nApasa <enter> pt a iesi.")

