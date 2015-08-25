# Program Trimite e-mail format standard
# Explica functiile smtplib
# Ion Studentul - 1/26/13

import smtplib

originator_email = 'hr@infoacademy.com'
destinatari = ['hr@todomain.com']

mesaj = """From: Persona care Origineaza e-mail <hr@infoacademy.com>
To: Ion Studentul <hr@todomain.com>
Subject: SMTP e-mail test

Salut.

Acesta este un mesaj de tip test!

O zi frumoasa,
Catalin
"""

try:
   smtpObj = smtplib.SMTP('127.0.0.1')
   smtpObj.sendmail(sender, destinatari, mesaj)         
   print "Mesajul electronic a fost trimis cu succes"
except(),e:
   print "Mesajul electronic nu a fost trimis cu succes"
   print e
