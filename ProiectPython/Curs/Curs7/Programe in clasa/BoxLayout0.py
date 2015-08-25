# Program kivy
# Explica functiile kivy - BoxLayout
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation='vertical'
        self.padding = 100
        b1 = Button(text='Primul buton')
        self.add_widget(b1)
        self.buton2 = Button(text='Al doilea buton')
        self.add_widget(self.buton2)

        
class MyApp(App):

    def build(self):
        x=LoginScreen()
        return x


if __name__ == '__main__':
    MyApp().run()


