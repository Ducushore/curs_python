# Program kivy3
# Explica functiile kivy -  image widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class ImagineaMea(GridLayout):

    def __init__(self, **kwargs):
        super(ImagineaMea, self).__init__(**kwargs)
        self.cols = 1
        self.imag1 = Image(source="jaguar.jpg")
        self.add_widget(self.imag1)
        self.imag2 = Image(source="jaguar.jpg")
        self.imag2.size_hint_x = 0.5
        self.imag2.size_hint_y = 0.2
        self.add_widget(self.imag2)

class AplicatiePersonalizata(App):

    def build(self):
        return ImagineaMea()
    
if __name__ == '__main__':
    AplicatiePersonalizata().run()
