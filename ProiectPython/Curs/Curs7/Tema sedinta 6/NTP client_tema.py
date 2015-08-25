# Program Tema 1
# Aplica functiile ntplib si e-mail
# Ion Studentul - 1/26/13

#importam modulele utilizate
import ntplib
import time
import smtplib
originator_email = 'hr@infoacademy.com'
destinatari = ['popescu.catalin.ionut@gmail.com']

#cream un obiect ntplib de tip client
obj = ntplib.NTPClient()

rasp = obj.request("2.ro.pool.ntp.org", 1 , 123, 5)

print "Versiunea NTP este ",rasp.version,"!"

print "Timpul dat de serverul ntp este ", time.ctime(rasp.tx_time)




mesaj = """From: Persona care Origineaza e-mail <hr@infoacademy.com>
To: Ion Studentul <hr@todomain.com>
Subject: SMTP e-mail test

Salut.

Acesta este un mesaj de tip test!"""+"""
Timpul extras prin ntp este """+time.ctime(rasp.tx_time)+""" 

O zi frumoasa,
Catalin
"""

# Gmail Login

username = 'mail.through.python'
parola = 'infoacad'

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com:587')
   smtpObj.starttls()
   smtpObj.login(username,parola)
   smtpObj.sendmail(originator_email, destinatari, mesaj)         
   print "Mesajul electronic a fost trimis cu succes"
except(),e:
   print "Mesajul electronic nu a fost trimis cu succes"
   print e
else:
    smtpObj.quit()

raw_input("Apasa enter sa iesi")

