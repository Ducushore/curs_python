# Program ftp Client
# Explica functiile telnetlib
# Ion Studentul - 1/26/13

import ftplib

filename = "Sunset.jpg"

ftp = ftplib.FTP('10.0.0.141')

print ftp.login()

print "Extragere continut:\n",ftp.retrlines('LIST')

print '\nCrearea unui fisier local temp ' + filename

fisier = open(filename, 'wb')
ftp.retrbinary("RETR "+ filename ,fisier.write)
fisier.close()
print "Fisiserul a fost copiat!"
ftp.close()

raw_input("\n\nApasa <enter> pt a iesi.")
