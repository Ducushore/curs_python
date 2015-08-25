# Program zipfile1
# Explica zipfile
# Ion Studentul - 1/26/13

import zipfile

fisier_zip = zipfile.ZipFile("exemplu.zip", "r")

# listeaza fisierele
for nume in fisier_zip.namelist():
    print "Fisier:",nume


# list file information
for info in fisier_zip.infolist():
    print '\n',info.filename
    print '\tComment:\t', info.comment
    print '\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)'
    print '\tZIP version:\t', info.create_version
    print '\tCompressed:\t', info.compress_size, 'bytes'
    print '\tUncompressed:\t', info.file_size, 'bytes'
    
raw_input("\n\nApasa <enter> pt a iesi.")