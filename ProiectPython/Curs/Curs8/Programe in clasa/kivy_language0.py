from kivy.base import runTouchApp
from kivy.lang import Builder

kv = '''

BoxLayout:
    Button
        text: 'test1'
        on_press: print "test1"
    Button:
        text: 'test2'
        on_press: print "test2"
'''
if __name__ == '__main__':
    runTouchApp(Builder.load_string(kv))
