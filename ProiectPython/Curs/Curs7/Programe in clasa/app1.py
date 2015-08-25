# Program kivy1
# Explica functiile kivy
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.label import Label


class SalutApp(App):

    def build(self):
        x=Label(text='Salut Lume!')
        x.font_size = 48
        return x


if __name__ == '__main__':
    SalutApp().run()
