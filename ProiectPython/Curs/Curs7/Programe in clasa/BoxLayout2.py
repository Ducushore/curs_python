# Program kivy6
# Explica functiile kivy - BoxLayout
# Ion Studentul - 1/26/13

import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class Box_Layout(BoxLayout):

    def __init__(self, **kwargs):
        super(Box_Layout, self).__init__(**kwargs)
        self.orientation='vertical'
        self.padding=20
        self.spacing=20
        self.buton1 = Button(text='Primul buton')
        self.add_widget(self.buton1)
        self.buton2 = Button(text='Al doilea buton')
        self.add_widget(self.buton2)

        
class MyApp(App):

    def build(self):
        root = Box_Layout()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0.2, 0.1, 0.9, 0.8)  # blue;
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    MyApp().run()


