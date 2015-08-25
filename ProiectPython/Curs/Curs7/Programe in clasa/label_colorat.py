# Program kivy
# Explica functiile kivy - caracteristici label
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.label1=Label(text='Salut Lume!',
                       italic=True, 
                       font_size=46, 
                       color=(1,0.2,0.2,0.8))
        self.add_widget(self.label1)
        
class MyApp(App):

    def build(self):
        x=LoginScreen()
        return x


if __name__ == '__main__':
    MyApp().run()

