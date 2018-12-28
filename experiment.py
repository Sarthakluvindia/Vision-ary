from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.graphics import Mesh
from math import cos, sin, pi
from kivy.config import Config
from win32api import GetSystemMetrics

#finding width and height of the window for full screen.
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
Config.set('graphics', 'width', width)
Config.set('graphics', 'height', height-30)

class MeshTestApp(App):

    def change_mode(self, mode, *largs):
        self.mesh.mode = mode

    def build_mesh(self):
        """ returns a Mesh of a rough circle. """
        vertices = []
        indices = []
        step = 10
        istep = (pi * 2) / float(step)
        for i in range(step):
            x = 350 + cos(istep * i) * 100
            y = 350 + sin(istep * i) * 100
            vertices.extend([x, y, 0, 0])
            indices.append(i)
        return Mesh(vertices=vertices, indices=indices)

    def build(self):
        wid = Widget()
        with wid.canvas:
            self.mesh = self.build_mesh()
        mode = 'triangle_strip'
        self.change_mode(mode)
        lvision = Label(text='Vision\n-\nARY', font_size='100sp', halign='center', valign= 'middle')
        root = BoxLayout(orientation="horizontal")
        root.add_widget(wid)
        root.add_widget(lvision)

        return root


if __name__ == '__main__':
    MeshTestApp().run()