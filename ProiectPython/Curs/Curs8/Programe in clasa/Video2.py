# Program kivy 10
# Explica functiile kivy -  video widget
# Ion Studentul - 1/26/13
 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
     
         
class MyApp(App):
    def build(self):
        self.parent= FloatLayout()
        self.Menu(None)
        return self.parent
    
    def Menu(self, buton):
        self.parent.clear_widgets()
        try:
            self.video1.state="stop"
        except:
            pass
        try:
            pass
            self.video2.state="stop"
        except:
            pass
        self.layout1 =GridLayout(cols=2)
        self.layout1.spacing =100
        self.layout1.padding =100
        button1 = Button(text='Play video1', font_size=14)
        button1.bind(on_press=self.on_button_press1) 
        self.layout1.add_widget(button1) #add button
        button2 = Button(text='Play video2', font_size=14)
        button2.bind(on_press=self.on_button_press2) 
        self.layout1.add_widget(button2) 
        self.parent.add_widget(self.layout1)
        return self.parent
               
    def on_button_press1(self,buton):
        self.parent.clear_widgets()
        self.layout2 =GridLayout(cols=2)
        menuBack = Button(text='Menu', font_size=14)
        menuBack.size_hint = (0.1,0.1)
        menuBack.bind(on_press=self.Menu) 
        self.layout2.add_widget(menuBack)
        self.video1= VideoPlayer(source='softboy.avi', state='play')
        self.layout2.add_widget(self.video1)
        self.parent.add_widget(self.layout2) 
        return self.parent
    
    def on_button_press2(self,buton):
        self.parent.clear_widgets()
        self.layout3 =GridLayout(cols=2)
        menuBack = Button(text='Menu', font_size=14)
        menuBack.size_hint = (0.1,0.1)
        menuBack.bind(on_press=self.Menu) 
        self.layout3.add_widget(menuBack)
        self.video2= VideoPlayer(source='videoplayback.avi', state='play')
        self.layout3.add_widget(self.video2) 
        self.parent.add_widget(self.layout3) 
        return self.parent
    
if __name__ == '__main__':
    MyApp().run()
