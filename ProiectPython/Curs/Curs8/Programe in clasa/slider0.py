# Program kivy4
# Explica functiile kivy -  slider widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
muzica_activa = 0

class SliderulMeu(GridLayout):

    def __init__(self, **kwargs):
        super(SliderulMeu, self).__init__(**kwargs)
        self.cols = 1
        self.arata_volum = Label (text = "volum: 10")
        self.add_widget(self.arata_volum)
        self.slide_muzica = Slider(min=0, max=100, value=20)
        self.slide_muzica.padding = 20
        self.slide_muzica.orientation="horizontal" # alte optiuni 'vertical'
        self.slide_muzica.step = 10
        self.add_widget(self.slide_muzica)
        self.slide_muzica.bind(value=self.valoare_volum)
        
    def valoare_volum (self,obiect,valoare):
        '''utilziat pentru a vedea volumul'''
        self.arata_volum.text = "volum: "+str(int(self.slide_muzica.value))
        
class AplicatiePersonalizata(App):

    def build(self):
        return SliderulMeu()


if __name__ == '__main__':
    AplicatiePersonalizata().run()
