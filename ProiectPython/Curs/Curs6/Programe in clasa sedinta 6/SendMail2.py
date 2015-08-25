# Program Trimite e-mail tip text
# Explica functiile smtplib
# Ion Studentul - 1/26/13

import smtplib

originator_email = 'hr@infoacademy.com'
destinatari = ['popescu.catalin.ionut@gmail.com']

mesaj = """From: Persona care Origineaza e-mail <hr@infoacademy.com>
To: Ion Studentul <hr@todomain.com>
Subject: SMTP e-mail test

Salut.

Acesta este un mesaj de tip test!

O zi frumoasa,
Catalin
"""

# Gmail Login

username = 'mail.through.python'
parola = 'infoacademy'

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