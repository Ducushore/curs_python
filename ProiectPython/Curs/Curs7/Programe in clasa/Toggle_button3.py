# Program kivy11
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
        self.Toggle1 = ToggleButton(text = "muzica")
        self.Toggle1.background_normal = "on.png"
        self.Toggle1.color = (0,1,0,1)
        self.Toggle1.background_down = "off.png"
        self.add_widget (self.Toggle1)
        self.Toggle2 = ToggleButton(text = "efecte")
        self.Toggle2.background_normal = "on.png"
        self.Toggle2.background_down = "off.png"
        self.add_widget (self.Toggle2)
        self.Toggle1.bind(on_press=self.Ruleaza_la_activare_t1)
        self.Toggle2.bind(on_press=self.Ruleaza_la_activare_t2)
        
    def Ruleaza_la_activare_t1(self ,value ):
        print "The Toggle1 este ",self.Toggle1.state
        print "The Toggle2 este ",self.Toggle2.state,"\n"
        
    def Ruleaza_la_activare_t2(self ,value ):
        print "The Toggle1 este ",self.Toggle1.state
        print "The Toggle2 este ",self.Toggle2.state,"\n"
        
class AplicatiePersonalizata(App):
    def build(self):
        return Test_input()


if __name__ == '__main__':
    AplicatiePersonalizata().run()
