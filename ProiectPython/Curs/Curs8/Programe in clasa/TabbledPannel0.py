# Program kivy
# Explica functiile kivy -  TabbedPanel widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
 
class TabbedPanelApp(GridLayout):
    def __init__(self, **kwargs):
        super(TabbedPanelApp, self).__init__(**kwargs)
        self.cols =1
        tb_panel= TabbedPanel()
        
        th_text_head = TabbedPanelHeader(text='Text tab')
        th_text_head.content= Label(text='Un text')
 
        th_img_head= TabbedPanelHeader(text='Image tab')
        th_img_head.content= Image(source='nature4.jpg',pos=(400, 100), size=(400, 400))
 
        th_btn_head = TabbedPanelHeader(text='Button tab')
        th_btn_head.content= Button(text='Acesta este un buton',font_size=20,
                                    size_hint=(0.8, 0.8))
        
        tb_panel.add_widget(th_text_head)
        tb_panel.add_widget(th_img_head)
        tb_panel.add_widget(th_btn_head)         
 
        self.add_widget(tb_panel)
 
class AplicatiePersonalizata(App):

    def build(self):
        return TabbedPanelApp()
    
if __name__ == '__main__':
    AplicatiePersonalizata().run()