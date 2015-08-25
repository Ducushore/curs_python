# Program kivy9
# Explica functiile kivy - Toggle button
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
check1=0


class Test_input(GridLayout):

    def __init__(self, **kwargs):
        super(Test_input, self).__init__(**kwargs)
        self.cols = 1
        self.text = Label(text='un label')
        self.add_widget(self.text)
        self.Toggle = ToggleButton(text="Bifeaza-ma!")
        self.add_widget (self.Toggle)
        self.Toggle.bind(on_press=self.Ruleaza_la_activare)
    
    def Ruleaza_la_activare(self ,value ):
        global check1
        print "Asta este value",value
        if (check1 %2 == 0) :
            print('The Toggle button is active')
        else:
            print('The Toggle button is inactive')
        check1 += 1


class AplicatiePersonalizata(App):

    def build(self):
        return Test_input()


if __name__ == '__main__':
    AplicatiePersonalizata().run()
