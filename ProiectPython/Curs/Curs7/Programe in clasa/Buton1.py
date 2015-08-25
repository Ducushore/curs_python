# Program kivy12
# Explica functiile kivy - Button
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import sys


class Test_input(GridLayout):

    def __init__(self, **kwargs):
        super(Test_input, self).__init__(**kwargs)
        self.cols = 1
        self.text = Label(text='un label')
        self.add_widget(self.text)
        self.buton1 = Button(text="Seteaza Copyright")
        self.buton1.background_normal = "normal.png"
        self.buton1.background_down = "apasat.png"
        self.add_widget (self.buton1)
        self.buton1.bind(on_press=self.Ruleaza_la_activare)
    
    def Ruleaza_la_activare(self ,value ):
        self.copyright = "Infoacademy"
        self.buton1.text= "Am setat!"
        print  value
        print "Copyright setat"


class AplicatiePersonalizata(App):

    def build(self):
        return Test_input()


if __name__ == '__main__':
    AplicatiePersonalizata().run()
