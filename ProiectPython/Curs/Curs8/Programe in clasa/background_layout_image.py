# Program kivy5
# Explica functiile kivy - image background
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before: 
            self.imag1 = Image(source="fundal.jpg")
            self.imag1.opacity = 0.7
            self.add_widget(self.imag1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class MainApp(App):

    def build(self):
        c = CustomLayout()
        self.but1 =Button(text = "Butonul 1",blod =True, background_color = (0,0,1,1))
        self.but1.pos = (290,380)
        self.but1.size_hint = (0.25,0.2)
        c.add_widget(self.but1)
        self.but2 =Button(text = "Butonul 2",blod =True, background_color = (0,0,1,1))
        self.but2.pos = (290,280)
        self.but2.size_hint = (0.27,0.1)
        c.add_widget(self.but2)
        self.but3 =Button(text = "Butonul 2",blod =True, background_color = (0,0,1,1))
        self.but3.pos = (290,180)
        self.but3.size_hint = (0.25,0.1)
        self.but3.opacity = 0.7
        c.add_widget(self.but3)
        return c

if __name__ == '__main__':
    MainApp().run()
