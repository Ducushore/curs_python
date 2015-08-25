# Program NTP Client
# Explica functiile ntplib
# Ion Studentul - 1/26/13

#importam modulele utilizate
import ntplib
import time

#cream un obiect ntplib de tip client
obj = ntplib.NTPClient()

rasp = obj.request("0.ro.pool.ntp.org", 2 , 123, 5)

print "Versiunea NTP este ",rasp.version,"!"

print "Timpul dat de serverul ntp este ", time.ctime(rasp.tx_time)

raw_input("Apasa enter sa iesi")

