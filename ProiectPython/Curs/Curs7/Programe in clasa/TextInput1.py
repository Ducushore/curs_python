# Program kivy9
# Explica functiile kivy - text input
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Test_input(GridLayout):

    def __init__(self, **kwargs):
        super(Test_input, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='un label'))
        self.text_input_1 = TextInput(background_color = (0.4,0.6,0.8,1))
        self.text_input_1.foreground_color = (0,1,0,1)
        self.text_input_1.font_size = 26
        self.text_input_1.padding=20
        self.text_input_1.hint_text_color = (1,0,0,1)
        self.text_input_1.hint_text="07xx.xxx.xxx!"
        self.add_widget(self.text_input_1)

class AplicatiePersonalizata(App):

    def build(self):
        return Test_input()


if __name__ == '__main__':
    AplicatiePersonalizata().run()
