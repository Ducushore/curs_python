# Program Socket program1 Client
# Explica functiile Socket
# Ion Studentul - 1/26/13

print "Program cerere asistenta client\n"
import socket               # importa modulul socket

s = socket.socket()         # Creaza un obiect socket

host = "192.168.1.6"      # Vom trimite cererea al un server dat
port = 12345                # Rezerva un port pentru aplicatie

s.connect((host, port))     # Solicitam conectarea la serverul dat
print s.recv(1024)          # Afisam mesajele trimise
print s.recv(1024)          # Afisam mesajele trimise
s.close                     # Inchidem conexiunea

raw_input("Apasa enter sa iesi")