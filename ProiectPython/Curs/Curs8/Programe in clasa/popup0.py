# Program kivy13
# Explica functiile kivy popup widget
# Ion Studentul - 1/26/13

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label

class PopupApp(GridLayout):

    def __init__(self, **kwargs):
        super(PopupApp, self).__init__(**kwargs)
        self.cols = 1
        buton1 = Button(text = "deschide un popup")
        buton1.bind(on_press=self.un_popup)
        self.add_widget(buton1)
        
        
    def un_popup(self,buton):
        """Creaza un popup"""
        inchide=Button(text='Inchide! ')
        self.popup = Popup()
        self.popup.title='Testam un popup'
        self.popup.content=inchide
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



    