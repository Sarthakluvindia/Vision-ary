from kivy.app import App
import io
import os
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from google.cloud import vision
from google.cloud.vision import types

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


class MainTApp(App):
    im = Image(source='img1.png')
    textinput = TextInput(multiline=False)
    btnLabel = Button(text='Label Recognition')
    label = Label()
    manager=ScreenManager()

    def build(self):
        layout1 = BoxLayout(size_hint=(1, None), height=50, orientation="horizontal")
        searchinput = TextInput()
        searchbutton = Button(text="Search")
        cat = Button(text="Upload")
        cat.bind(on_press=self.callback)
        layout1.add_widget(self.textinput)
        layout1.add_widget(cat)
        layout1.add_widget(searchinput)
        layout1.add_widget(searchbutton)

        layout = BoxLayout(size_hint=(1, None), height=50)

        self.btnLabel.bind(on_press=self.btnclick)
        btnSearch = Button(text='Search inside Image')
        btnHelp = Button(text='Help required?')
        layout.add_widget(self.btnLabel)
        layout.add_widget(btnSearch)
        layout.add_widget(btnHelp)
        root = BoxLayout(orientation='vertical')
        c = Imglayout()
        root.add_widget(c)

        self.im.keep_ratio = False
        self.im.allow_stretch = True
        c.add_widget(self.im)
        root.add_widget(layout1)
        root.add_widget(layout)
        return root

    def callback(self, value):
        filename = self.textinput.text
        self.im.source = filename

    def btnclick(self, value):
        client = vision.ImageAnnotatorClient()
        filename = self.textinput.text
        # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname(__file__), filename)

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        # Match each identified label with the one being searched for
        for label in labels:
            self.label.text = label.description


        self.btnLabel.configure(text="Done")
        self.btnLabel.configure(text="Upload Image")


if __name__ == '__main__':
    MainTApp().run()