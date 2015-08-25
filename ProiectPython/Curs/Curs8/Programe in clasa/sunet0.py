# Program kivy11
# Explica functiile kivy -  audio widget
# Ion Studentul - 1/26/13

from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class VideoPlayerApp(App):

    def build(self):
        layout= GridLayout()
        cols=1
        sound = SoundLoader.load('JO_-_09_-_Fortitude.ogg')
        if sound:
            sound.play()
            print "Sursa fisierului este", sound.source
            print "Lungimea fisierului este ", sound.length

if __name__ == '__main__':
    VideoPlayerApp().run()



    
