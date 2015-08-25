# Program kivy9
# Explica functiile kivy - toggle button
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton

class Test_input(GridLayout):

    def __init__(self, **kwargs):
        super(Test_input, self).__init__(**kwargs)
        self.cols = 1
        self.text = Label(text='un label')
        self.add_widget(self.text)
        self.Toggle1 = ToggleButton(text="Voteaza-ma!")
        self.Toggle1.bold = "True"
        self.Toggle1.group = "Eu cu cine votez?"
        self.Toggle1.background_color = (1,0,0,1)
        self.add_widget (self.Toggle1)
        self.Toggle2 = ToggleButton(text="Ba voteaza-ma pe mine!")
        self.Toggle2.bold = "True"
        self.Toggle2.group = "Eu cu cine votez?"
        self.Toggle2.background_color = (1,0,0,1)
        self.add_widget (self.Toggle2)
        self.Toggle3 = ToggleButton(text="Eu promit sa nu fur ... prea mult!")
        self.Toggle3.bold = "True"
        self.Toggle3.group = "Eu cu cine votez?"
        self.Toggle3.background_color = (1,0,0,1)
        self.Toggle3.state ="down"
        self.add_widget (self.Toggle3)
        self.Toggle1.bind(on_press=self.Ruleaza_la_activare_t1)
        self.Toggle2.bind(on_press=self.Ruleaza_la_activare_t2)
        self.Toggle3.bind(on_press=self.Ruleaza_la_activare_t3)
        
    def Ruleaza_la_activare_t1(self ,value ):
        print "The Toggle1 este ",self.Toggle1.state
        print "The Toggle2 este ",self.Toggle2.state
        print "The Toggle3 este ",self.Toggle3.state,"\n"

        
    def Ruleaza_la_activare_t2(self ,value ):
        print "The Toggle1 este ",self.Toggle1.state
        print "The Toggle2 este ",self.Toggle2.state
        print "The Toggle3 este ",self.Toggle3.state,"\n"
        
    def Ruleaza_la_activare_t3(self ,value ):
        print "The Toggle1 este ",self.Toggle1.state
        print "The Toggle2 este ",self.Toggle2.state
        print "The Toggle3 este ",self.Toggle3.state,"\n"
    

class AplicatiePersonalizata(App):

    def build(self):
        return Test_input()


if __name__ == '__main__':
    AplicatiePersonalizata().run()
