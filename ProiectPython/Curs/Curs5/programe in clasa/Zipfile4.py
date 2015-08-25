# Program zipfile4
# Explica zipfile
# Ion Studentul - 1/26/13

import zipfile

print '\n\tCream o arhiva necompresata'
fz_necompresat = zipfile.ZipFile('fisier_zip.zip', mode='w')
try:
    print '\tAdauga fisiere'
    fz_necompresat.write('setup.py')
    #fz_necompresat.write('Python_ico.ico')
finally:
    print '\tInchiderea arhivei'
    fz_necompresat.close()

for info in fz_necompresat.infolist():
    print info.filename, "Marime fisier",info.file_size,"! Marime fisier compresat", info.compress_size,"!"

print '\n\tCream o arhiva compresata'
fz = zipfile.ZipFile('fisier_zip.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
try:
    print '\tAdauga fisiere'
    fz.write('setup.py')
    #fz.write('Python_ico.ico')
finally:
    print '\tInchiderea arhivei'
    fz.close()


fisier_zip = zipfile.ZipFile("fisier_zip.zip", "r")

for info in fisier_zip.infolist():
    print info.filename, "Marime fisier",info.file_size,"! Marime fisier compresat", info.compress_size,"!"


fisier_zip.close()

raw_input("\n\nApasa <enter> pt a iesi.")
