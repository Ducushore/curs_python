# Program Telnet Client
# Explica functiile telnetlib
# Ion Studentul - 1/26/13

import telnetlib,re

HOST = "route-views.routeviews.org"
user = "rviews"
password =""
debug_level_telnet = 1

telnet_obj = telnetlib.Telnet(HOST)

#putem sa setam un debug elvel
telnet_obj.set_debuglevel(debug_level_telnet)
telnet_obj.read_until("login: " , 5)
telnet_obj.write(user + "\r\n")

telnet_obj.read_until("password: " ,5)
telnet_obj.write(password + "\r\n")

telnet_obj.read_until(">",10)

if (debug_level_telnet!=0):
  print telnet_obj.read_until(">",10)

telnet_obj.write("show version"+ "\r\n")

captura = telnet_obj.read_until("--more--",10)

if (debug_level_telnet!=0):
  print captura

telnet_obj.write("exit" + "\r\n")

telnet_obj.close()

test_cap=re.search("Version \d\d.\d\(\d\)",captura)
if test_cap:
  print "S-a gasit textul cautat!"#test_cap.group(0)
  print "versiunea este "+ test_cap.group(0)
else:
  print captura

raw_input("\n\nApasa <enter> pt a iesi.")

