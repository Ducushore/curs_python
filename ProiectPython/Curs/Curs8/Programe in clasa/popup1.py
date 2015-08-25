# Program kivy13
# Explica functiile kivy popup widget
# Ion Studentul - 1/26/13

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class PopupApp(GridLayout):

    def __init__(self, **kwargs):
        super(PopupApp, self).__init__(**kwargs)
        self.cols = 1
        buton1 = Button(text = "deschide un popup")
        buton1.size = (0.8,0.8)
        buton1.bind(on_press=self.un_popup)
        self.add_widget(buton1)
        
    def un_popup(self,buton):
        """Creaza un popup"""
        inchide=Button(text='Inchide!')
        inchide.size_hint = (1,0.1)
        eticheta=Label(text ="Acesta este un popup informativ!")
        layout2=BoxLayout()
        layout2.orientation = "vertical"
        layout2.add_widget(eticheta)
        layout2.add_widget(inchide)
        layout2.padding = 40
        self.popup = Popup()
        self.popup.size_hint = (None,None)
        self.popup.size = (400, 400)
        self.popup.title='Testam un popup'
        self.popup.content=layout2
        self.popup.open()
        inchide.bind(on_press=self.inchide_popup)
    
    def inchide_popup(self, Buton):
        """inchide"""
        self.popup.dismiss()
    
class AplicatiePersonalizata(App):

    def build(self):
        return PopupApp()

if __name__ == '__main__':
    AplicatiePersonalizata().run()



    