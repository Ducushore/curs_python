# Program kivy
# Explica functiile kivy
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        x =Label(text='Utilizator ')
        self.add_widget(x)
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Parola'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.password.bind(on_text_validate= self.verific_user_si_parola)

    def verific_user_si_parola(self,t):
        print t,"instanta" 
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
        return LoginScreen()


if __name__ == '__main__':
    AplicatiePersonalizata().run()
