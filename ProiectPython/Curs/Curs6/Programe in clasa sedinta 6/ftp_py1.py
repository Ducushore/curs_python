# Program ftp Client
# Explica functiile telnetlib
# Ion Studentul - 1/26/13

import ftplib

ftp = ftplib.FTP('10.0.0.141')

ftp.login()

ftp.retrlines('LIST')

ftp.close()

raw_input("\n\nApasa <enter> pt a iesi.")
