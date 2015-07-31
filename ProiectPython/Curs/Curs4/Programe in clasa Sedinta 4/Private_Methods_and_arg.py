# Program Private methonds and arguments
# Explica mostenirea
# Ion Studentul - 1/26/13

class Clasa_privat(object):
    """test clasa privata"""
    def test_public(self):
        """o metoda publica cu un argument privat"""
        self.argumentPublic = "public"
        self.__argumentPrivat = "privat"
        
    def acceseazaArgPrivat(self):
        """o metoda publica ce acceseaza un argument privat""" 
        print self.__argumentPrivat," <= argument privat "
    
    def __MetodaPrivata(self):
         """o metoda privata"""
         print self.__argumentPrivat," <= argument privat "
         print self.argumentPublic," <= argument public"

    def acceseazaMetodaPrivata(self):
        """o metoda publica ce acceseaza o metoda privata""" 
        print self.__argumentPrivat," <= argument privat "

obj1=Clasa_privat()
obj1.__argumentPrivat
obj1.argumentPrivat
obj1.acceseazaArgPrivat()
obj1._Clasa_privat__argumentPrivat

obj1.__MetodaPrivata()
obj1.MetodaPrivata()
obj1.acceseazaMetodaPrivata()
obj1._Clasa_privat__MetodaPrivata()
