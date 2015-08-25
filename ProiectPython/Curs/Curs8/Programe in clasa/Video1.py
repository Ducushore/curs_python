# Program kivy 9
# Explica functiile kivy -  video widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class VideoPlayerApp(App):

    def build(self):
        filename = 'videoplayback.avi'
        self.layout = GridLayout(cols=2)
        self.video =  VideoPlayer(source=filename, state='play')
        self.layout.add_widget(self.video)
        
        button1 = Button(text='Play video1', font_size=14)
        button1.bind(on_press=self.play_video1)
        button1.size_hint=(0.2,0.1)
        self.layout.add_widget(button1)
        button2 = Button(text='pauza video1', font_size=14)
        button2.size_hint=(0.2,0.1)
        button2.bind(on_press=self.pauza_video1) 
        self.layout.add_widget(button2)
        button3 = Button(text='stop video1', font_size=14)
        button3.size_hint=(0.2,0.1)
        button3.bind(on_press=self.stop_video1) 
        self.layout.add_widget(button3)
        button4 = Button(text='la 1/3 din film', font_size=14)
        button4.size_hint=(0.2,0.1)
        button4.bind(on_press=self.un_sfert_video1) 
        self.layout.add_widget(button4)
        button5 = Button(text='la 2/3 din film', font_size=14)
        button5.size_hint=(0.2,0.1)
        button5.bind(on_press=self.doua_sferturi_video1) 
        self.layout.add_widget(button5)
        button6 = Button(text='volum : -', font_size=14)
        button6.size_hint=(0.2,0.1)
        button6.bind(on_press=self.minus_video1) 
        self.layout.add_widget(button6)
        button7 = Button(text='volum : +', font_size=14)
        button7.size_hint=(0.2,0.1)
        button7.bind(on_press=self.plus_video1) 
        self.layout.add_widget(button7)
        return self.layout
    
    def play_video1 (self,buton):
        self.video.state='play'
    def pauza_video1 (self,buton):
        self.video.state='pause'
    def stop_video1 (self,buton):
        self.video.state='stop'
    def un_sfert_video1 (self,buton):
        self.video.seek(0.33)
    def doua_sferturi_video1 (self,buton):
        self.video.seek(0.66)
    def minus_video1 (self,buton):
        if (self.video.volume>0):
            self.video.volume -=0.1
    def plus_video1 (self,buton):
        if (self.video.volume<1):
            self.video.volume +=0.1
            

if __name__ == '__main__':
    VideoPlayerApp().run()
