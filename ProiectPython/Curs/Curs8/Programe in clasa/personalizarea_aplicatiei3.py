# Program ico si dimensiune
# Explica functiile kivy
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config



class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Utilizator '))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Parola'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.password.bind(on_text_validate= self.verific_user_si_parola)

    def verific_user_si_parola(self,t):
        text_user = self.username.text
        text_pass = self.password.text
        if (text_user == "test" and text_pass=="test"):
            self.clear_widgets()
            self.add_widget(Label(text='Bine ai venit!'))
        else:
            self.username.select_all()  
            self.username.delete_selection()      
            self.password.select_all()  
            self.password.delete_selection()
        


class AplicatiePersonalizata(App):

    def build(self):
        self.icon ="python1.ico"
        return LoginScreen()


#seteaza dimensiunea ferestrei
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')

if __name__ == '__main__':
    AplicatiePersonalizata().run()