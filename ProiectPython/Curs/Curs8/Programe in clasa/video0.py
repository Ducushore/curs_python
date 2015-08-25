# Program kivy 8
# Explica functiile kivy -  video widget
# Ion Studentul - 1/26/13

from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer


class VideoPlayerApp(App):

    def build(self):
        filename = 'videoplayback.avi'
        return VideoPlayer(source=filename, state='play')


if __name__ == '__main__':
    VideoPlayerApp().run()
