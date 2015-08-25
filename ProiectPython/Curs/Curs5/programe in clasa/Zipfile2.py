# Program zipfile2
# Explica zipfile
# Ion Studentul - 1/26/13

import zipfile

fisier_zip = zipfile.ZipFile("exemplu.zip", "r")


for name in fisier_zip.namelist():
    data = fisier_zip.read(name)
    print name," lungime:", len(data)
    print "primele 10 caractere:", repr(data[:10]),"\n"


fisier_zip.extractall("D:\\")


fisier_zip.close()
    
raw_input("\n\nApasa <enter> pt a iesi.")
