# Program Socket program1 Server
# Explica functiile Socket
# Ion Studentul - 1/26/13
host = "192.168.1.5"

print "Program cerere asistenta client"
import socket               # importa modulul socket

s = socket.socket()         # Creaza un obiect socket

port = 12345                # Reserva un port local pentru servicul taufor your service.
s.bind((host, port))        # setam legatura(bind-ul) 

s.listen(5)                 # Acum asteptam conexiunea clientului.
                            # Argumentul specifica numarul maxim de  conexiuni de asteptare in coada si 
                            # ar trebuie sa fie mai amre de 0 (Uzual 5).
while True:
   conex_client, adresa = s.accept()     # Stabileste o conexiune cu clientul.
   print 'Am primit solicitare de la ', adresa
   conex_client.send('Iti multumim pentru cerere!')
   conex_client.send('Am inregistrat cererea ta si vom raspunde cat mai repede!')
   conex_client.close()                # Inchidem conexiunea

raw_input("Apasa enter sa iesi")