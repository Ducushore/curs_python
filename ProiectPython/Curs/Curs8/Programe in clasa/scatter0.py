# Program kivy
# Explica functiile kivy -  scatter widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class Scatter_test(GridLayout):

    def __init__(self, **kwargs):
        super(Scatter_test, self).__init__(**kwargs)
        self.cols = 1
        self.scatter1 = Scatter()
        self.imag1 = Image(source="nature1.jpg")
        self.scatter1.add_widget(self.imag1)
        self.add_widget(self.scatter1)

class AplicatiePersonalizata(App):

    def build(self):
        return Scatter_test(size=(400, 400),size_hint=(None, None))


if __name__ == '__main__':
    AplicatiePersonalizata().run()
