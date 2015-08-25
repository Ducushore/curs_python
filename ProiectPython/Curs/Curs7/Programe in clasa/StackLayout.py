# Program kivy7
# Explica functiile kivy - Stacklayout
# Ion Studentul - 1/26/13

import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

class Stack_Layout(StackLayout):

    def __init__(self, **kwargs):
        super(Stack_Layout, self).__init__(**kwargs)
        #self.orientation='vertical'
        self.orientation='lr-bt'
        self.padding=60
        self.spacing=20
        self.size_hint_x =0.3
        self.size_hint_y =0.3
        self.buton1 = Button(text='Primul buton')
        self.add_widget(self.buton1)
        self.buton2 = Button(text='Al doilea buton')
        self.add_widget(self.buton2)
        
class MyApp(App):

    def build(self):
        x=Stack_Layout()
        return x


if __name__ == '__main__':
    MyApp().run()
