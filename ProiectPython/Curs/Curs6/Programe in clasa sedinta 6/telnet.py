# Program Telnet Client
# Explica functiile telnetlib
# Ion Studentul - 1/26/13

import telnetlib

HOST = "10.0.0.99"
user = "user"
password ="cisco"

telnet_obj = telnetlib.Telnet(HOST)
telnet_obj.set_debuglevel(9)
telnet_obj.read_until("login: " , 5)
telnet_obj.write(user + "\r\n")

telnet_obj.read_until("password: " ,5)
telnet_obj.write(password + "\r\n")
   
print telnet_obj.read_until(">",10)

telnet_obj.write("show ip interface brief"+ "\r\n"+" "+ " ")

captura = telnet_obj.read_until(">",10)
print """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""

print captura

telnet_obj.write("exit" + "\r\n")

telnet_obj.close()

raw_input("\n\nApasa <enter> pt a iesi.")

