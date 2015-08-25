from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.label import Label
 
class Example1(App):
 
    def build(self):
        #define the carousel
        carousel = Carousel(direction='right')
        carousel.anim_move_duration = 1
        carousel.padding = 40
        carousel.loop = True
        image1 = Image(source="nature1.jpg")
        carousel.add_widget(image1)
        image2 = Image(source="nature2.jpg")
        carousel.add_widget(image2)
        image3 = Image(source="nature3.jpg")
        carousel.add_widget(image3)
        image4 = Image(source="nature4.jpg")
        carousel.add_widget(image4)
        eticheta =  Label (text = "Am ajuns la finalul listei!", font_size = 40)
        carousel.add_widget(eticheta)
        
        return carousel
 
if __name__ == '__main__':
    Example1().run()
