# Program kivy
# Explica functiile kivy
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        x = Label(text='[i]Salut[/i] \n [size=32][b] Lume![/b][/size]',markup =True)
        return x

if __name__ == '__main__':
    MyApp().run()
