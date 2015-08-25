# Program kivy9
# Explica functiile kivy - text input
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
check1=0


class Test_input(GridLayout):

    def __init__(self, **kwargs):
        super(Test_input, self).__init__(**kwargs)
        self.cols = 1
        self.text = Label(text='un label')
        self.add_widget(self.text)
        self.checkbox1 = CheckBox(text="1",group = "test")
        self.add_widget (self.checkbox1)
        self.checkbox2 = CheckBox()
        self.checkbox2.group = "test"
        self.add_widget (self.checkbox2)
        self.checkbox1.bind(active=self.Ruleaza_la_activare)
    
    def Ruleaza_la_activare(self ,value ,instance):
        global check1
        print value,"Asta e value"
        print instance,"Asta este instance"
        if (check1 %2 == 0) :
            print('The checkbox1 is active')
        else:
            print('The checkbox2 is active')
        check1 += 1


class AplicatiePersonalizata(App):

    def build(self):
        return Test_input()


if __name__ == '__main__':
    AplicatiePersonalizata().run()
