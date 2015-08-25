# Program kivy4
# Explica functiile kivy - image background
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)
        self.imag1 = Image(source="fundal.jpg")
        self.imag1.opacity = 0.5
        self.add_widget(self.imag1)
        self.but1 =Button(text = "Butonul 1",bold =True, background_color = (0,0,1,1))
        self.but1.pos = (350,300)
        self.but1.size_hint = (1,0.05)
        self.but1.opacity = 0.5
        self.imag1.add_widget(self.but1)
        self.but2 =Button(text = "Butonul 2",bold =True, background_color = (0,0,1,1))
        self.but2.pos = (350,200)
        self.imag1.add_widget(self.but2)
        self.but3 =Button(text = "Butonul 3",bold =True, background_color = (0,0,1,1))
        self.but3.pos = (350,100)
        self.but3.size_hint = (0.3,0.05)
        self.imag1.add_widget(self.but3)


class MainApp(App):

    def build(self):
        return CustomLayout()

if __name__ == '__main__':
    MainApp().run()
