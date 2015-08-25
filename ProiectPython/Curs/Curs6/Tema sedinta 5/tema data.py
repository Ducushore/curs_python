#Tema afla data
# utilizarea random si calendar
# Ion Studentul -1 Ian 2013

import random
import calendar

saptamana={0:"luni",1:"marti",2:"miercuri",3:"joi",4:"vineri",5:"sambata",6:"duminica"}

def dataAleatoriu():
    lista=[]
    an=random.randrange(2000,2020) 
    luna=random.randrange(1,12)
    zi=random.randrange(1,28)
    lista+=[an]
    lista+=[luna]
    lista+=[zi]
    return lista

Apelare1=dataAleatoriu()
print "Data aleasa este anul: ",Apelare1[0],", luna: ",Apelare1[1],", ziua: ",Apelare1[2]
zi_sap1 =  calendar.weekday(Apelare1[0],Apelare1[1],Apelare1[2])
print "Ziua saptamanii pt. data aleasa este ",saptamana[zi_sap1]

Apelare2=dataAleatoriu()
print "Data aleasa este anul: ",Apelare2[0],", luna: ",Apelare2[1],", ziua: ",Apelare2[2]
zi_sap2 =  calendar.weekday(Apelare2[0],Apelare2[1],Apelare2[2])
print "Ziua saptamanii pt. data aleasa este ",saptamana[zi_sap2]

Apelare3=dataAleatoriu()
print "Data aleasa este anul: ",Apelare3[0],", luna: ",Apelare3[1],", ziua: ",Apelare3[2]
zi_sap3 =  calendar.weekday(Apelare3[0],Apelare3[1],Apelare3[2])
print "Ziua saptamanii pt. data aleasa este ",saptamana[zi_sap3]



      
