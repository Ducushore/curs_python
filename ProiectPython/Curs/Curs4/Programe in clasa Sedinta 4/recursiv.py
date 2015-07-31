# Program clasa recursiva
# Demonstreaza recursivitatea clasei 
# Ion Studentul - 1/26/13

class NumeClasa(object):
    """clasa mea"""
    instante=0
    def __init__(self):
        """initializarea obiectului"""
        NumeClasa.instante=NumeClasa.instante+1
    def creareinstante(self,nrInstante):
        """creaza multiple instante"""
        for i in range(nrInstante):
            globals()["x"+str(i)]=NumeClasa()
        
obiect1=NumeClasa()

obiect1.creareinstante(5)
print "Nr de instante existent este ",obiect1.instante

print "Obiectul x3 are argumentul instante ce este egal cu",x3.instante


raw_input("\n\nApasa <enter> pt a iesi.")



