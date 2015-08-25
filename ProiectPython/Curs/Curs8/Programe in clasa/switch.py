# Program kivy5
# Explica functiile kivy -  slider widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.label import Label

class Switch_implementare(GridLayout):

    def __init__(self, **kwargs):
        super(Switch_implementare, self).__init__(**kwargs)
        self.cols = 1
        self.padding = 150
        self.switch1 = Switch()
        self.switch1.active = True
        self.add_widget(self.switch1)
        self.arata_volum = Label (text = "volum: 10")
        self.add_widget(self.arata_volum)
        self.slide_muzica = Slider(min=0, max=100, value=10)
        self.slide_muzica.step = 5
        self.slide_muzica.orientation="horizontal" # alte optiuni 'vertical'
        self.add_widget(self.slide_muzica)
        self.switch1.bind(active=self.dezactiveaza_volum)
        self.slide_muzica.bind(value=self.valoare_volum)

    def valoare_volum (self,x,y):
        '''utilziat pentru a vedea volumul'''
        self.arata_volum.text = "volum: "+str(int(self.slide_muzica.value))
        
    def dezactiveaza_volum (self,x,y):
        '''utilziat pentru a acctiva sau a dezactiva slider-ul'''
        if (self.switch1.active == False) :
            self.slide_muzica.disabled =True
        else:
            self.slide_muzica.disabled =False
            self.slide_muzica.value = 0

        
class AplicatiePersonalizata(App):

    def build(self):
        return Switch_implementare()
    
if __name__ == '__main__':
    AplicatiePersonalizata().run()
