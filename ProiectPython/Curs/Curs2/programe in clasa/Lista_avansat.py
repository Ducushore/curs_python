# Lista de cumparaturi
# Demonstreaza optiuni avansate lista 
# Ion Stundentul - 1/26/13
lista=[]

print"\t\t Bine ati venit la programul lista de cumparaturi"

while (True):
    print """
0-Pentru afisare lista actuala
1-Pentru introducerea unui elent nou
2 pentru stergerea unui element existent
3- pentru stergerea intregii liste
q- pentru iesire
"""
    alegere=raw_input("\nIntrodu o cifra:\t")

    if (alegere=="0"):
        if (lista):
            lista.sort()
            print "\nLista cumparaturi este :\n"
            for e in lista:
                print "=>",e
        else:
            print "Lista este goala"
    elif (alegere=="1"):
        elementelnet_objou=raw_input("\nElementul nou este:\t")
        lista.append(elementelnet_objou)
    elif (alegere=='2'):
        if (lista):
            sterge=raw_input("scrie element ce doresti sa-l stergi:")
            if (sterge in lista):
                lista.remove(sterge)
                print "Elementul ", sterge , "a fost sters"
            else:
                print sterge , "nu a fost gasit in lista"
        else:
            print "Lista e goala"
    elif (alegere=='3'):
        lista=[]
        print("lista a fost stearsa")
    elif(alegere.upper()=='Q'):
        break

print "Va multumim ca ati ales acest program"
