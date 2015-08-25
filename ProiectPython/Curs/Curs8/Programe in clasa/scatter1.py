# Program kivy1
# Explica functiile kivy -  image widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

class Scatter_test(GridLayout):

    def __init__(self, **kwargs):
        super(Scatter_test, self).__init__(**kwargs)
        self.cols = 1
        self.layout1 = GridLayout(cols=1)
        self.eticheta = Label (text = "unghi: 0")
        self.imag1 = Image(source="nature3.jpg")
        self.buton1=Button(text="Afla rotatie")
        self.buton1.size_hint = (1,0.05)
        self.layout1.add_widget(self.eticheta)
        self.layout1.add_widget(self.imag1)
        self.scatter1 = Scatter()
        self.scatter1.auto_bring_to_front = False
        self.scatter1.add_widget(self.layout1)
        self.add_widget(self.scatter1)
        self.add_widget(self.buton1)
        self.buton1.bind(on_press = self.roteste_ma)
        
    def roteste_ma(self,buton):
        """modifica eticheta"""

        self.eticheta.text="unghi: "+str(int(self.scatter1.rotation))
        
class AplicatiePersonalizata(App):

    def build(self):
        return Scatter_test()
    
if __name__ == '__main__':
    AplicatiePersonalizata().run()