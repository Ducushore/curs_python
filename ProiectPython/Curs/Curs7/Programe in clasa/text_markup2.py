# Program kivy8
# Explica functiile kivy
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Salut \n [size=48]Lume![/size] ', markup=True )

if __name__ == '__main__':
    MyApp().run()
