from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
#from .game import Game

class Hantei(FloatLayout):

    source = StringProperty('./data/siro.jpg')


    def Size_Change(self):
        width = self.width
        height = self.height

        for k in self.ids:
            self.ids[k].font_size = width * 0.03


    def buttonClicked(self):
        print(self.source)
        self.source= '/data/hantei.jpg'

    def buttonClicked2(self):
        print(self.source)
        self.source= '/data/siro.jpg'
