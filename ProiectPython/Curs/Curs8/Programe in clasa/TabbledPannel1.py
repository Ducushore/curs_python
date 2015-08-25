from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
 
class TabbedPanelApp(App):
      def build(self):
          tb_panel= TabbedPanel()
          tb_panel.background_image ="fundal2.jpg"
          tb_panel.default_tab_text =  "tab-ul default"
          tb_panel.default_tab_content = Image(source='infoacademy3.gif',pos=(200, 100), size=(200, 200))

          th_text_head = TabbedPanelHeader(text='Text tab')
          th_text_head.content= Label(text='Infoacademy', font_size = 40)
 
          th_img_head= TabbedPanelHeader(text='Image tab')
          th_img_head.content= Image(source='infoacademy4.gif',pos=(400, 100), size=(400, 400))
 
          th_btn_head = TabbedPanelHeader(text='Button tab')
          layout= GridLayout(cols=1)
          eticheta=Label(text='tab-ul cu buton', font_size = 40)
          buton=Button(text='Acesta este un buton',font_size=20)
          layout.add_widget(eticheta)
          layout.add_widget(buton)
          th_btn_head.content= layout
          th_btn_head.content.padding = 200
          
 
          tb_panel.add_widget(th_text_head)
          tb_panel.add_widget(th_img_head)
          tb_panel.add_widget(th_btn_head)         
 
          return tb_panel
 
if __name__ == '__main__':
    TabbedPanelApp().run()
