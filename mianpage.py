from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from win32api import GetSystemMetrics

#finding width and height of the window for full screen.
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
Config.set('graphics', 'width', width)
Config.set('graphics', 'height', height-30)

filename = ""



class Imglayout(FloatLayout):
    def __init__(self, **args):
        super(Imglayout, self).__init__(**args)

        with self.canvas.before:
            Color(0, 0, 0, 0)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.updates, pos=self.updates)

    def updates(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

class MainPageApp(App):
    im = Image(source='')

    def getStr(self):
        self.im.source = filename

    def build(self):
        layout1 = BoxLayout(size_hint=(1, None), height=50, orientation="horizontal")
        textinput = TextInput(multiline=False)
        searchinput=TextInput()
        searchbutton=Button(text="Search")
        upload = Button(text="Upload")
        filename = textinput.text
        upload.bind(on_press=self.getStr)
        layout1.add_widget(textinput)
        layout1.add_widget(upload)
        layout1.add_widget(searchinput)
        layout1.add_widget(searchbutton)
        print(textinput.text)
        layout = BoxLayout(size_hint=(1, None), height=50)
        c = Imglayout()

        for mode in ('Label Recognition','Search in the Image', 'Help'):
            button = Button(text=mode)
            button.bind()
            layout.add_widget(button)

        self.im.keep_ratio = False
        self.im.allow_stretch = True
        c.add_widget(self.im)
        root = BoxLayout(orientation="vertical")
        root.add_widget(c)
        root.add_widget(layout1)
        root.add_widget(layout)
        return root

if __name__ == '__main__':
    MainPageApp().run()