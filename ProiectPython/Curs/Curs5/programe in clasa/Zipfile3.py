# Program zipfile1
# Explica zipfile
# Ion Studentul - 1/26/13

import zipfile

fz = zipfile.ZipFile('fisier_zip.zip', mode='w')
try:
    print 'Adauga fisiere'
    fz.write('setup.py')
    #fz.write('Python_ico.ico')
except:
    pass

fz.close()
    
raw_input("\n\nApasa <enter> pt a iesi.")
