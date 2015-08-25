# Program kivy
# Explica functiile kivy -  slider widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label

class SliderulMeu(GridLayout):

    def __init__(self, **kwargs):
        super(SliderulMeu, self).__init__(**kwargs)
        self.cols = 1
        self.padding = 150
        self.toggle1 = ToggleButton(text="muzica")
        self.toggle1.background_normal = "on.png"
        self.toggle1.background_down = "off.png"
        self.add_widget(self.toggle1)
        self.arata_volum = Label (text = "volum: 10")
        self.add_widget(self.arata_volum)
        self.slide_muzica = Slider(min=0, max=100, value=10)
        self.slide_muzica.step = 5
        self.slide_muzica.orientation="horizontal" # alte optiuni 'vertical'
        self.add_widget(self.slide_muzica)
        self.toggle1.bind(on_press=self.dezactiveaza_volum)
        self.slide_muzica.bind(value=self.valoare_volum)

    def valoare_volum (self,x,y):
        '''utilziat pentru a vedea volumul'''
        self.arata_volum.text = "volum: "+str(int(self.slide_muzica.value))
        
    def dezactiveaza_volum (self,x):
        '''utilziat pentru a acctiva sau a dezactiva slider-ul'''
        if (self.toggle1.state == "down") :
            self.slide_muzica.disabled =True
        else:
            self.slide_muzica.disabled =False
            self.slide_muzica.value = 0
        
class AplicatiePersonalizata(App):

    def build(self):
        return SliderulMeu()
    
if __name__ == '__main__':
    AplicatiePersonalizata().run()