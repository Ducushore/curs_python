# Program kivy1
# Explica functiile kivy -  image widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class ImagineaMea(GridLayout):

    def __init__(self, **kwargs):
        super(ImagineaMea, self).__init__(**kwargs)
        self.cols = 1
        self.padding = 20
        self.imag1 = Image(source="infoacademy1.gif")
        self.add_widget(self.imag1)
        self.imag2 = Image(source="snake1.jpg")
        self.add_widget(self.imag2)
        self.imag3 = Image(source="snake2.png")
        self.add_widget(self.imag3)

class AplicatiePersonalizata(App):

    def build(self):
        return ImagineaMea()


if __name__ == '__main__':
    AplicatiePersonalizata().run()
