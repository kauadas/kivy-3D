from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Mesh, RenderContext, Rotate, Translate
from kivy.graphics.transformation import Matrix
from kivy.clock import Clock
import load_file
import numpy as np


def gpu_matriz(matriz):
    order=[]
    for i in matriz:
        order+=i

    return order


def Mesh3D(vertices,indices):

    vertices=gpu_matriz(vertices)
    
    vex=[(b'v_pos',3,'float'),
    (b'v_normal',3,'float'),
    (b'v_tc0',2,'float'),
    (b'color',3,'float')]

    
    return Mesh(vertices=vertices,indices=indices,fmt=vex,mode="triangles")



class view3d(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.canvas = RenderContext()
        self.canvas.shader.source = 'shaders.glsl'
        Clock.schedule_interval(self.rodar,1/60)
        with self.canvas:
            self.draw()

    def rodar(self,*args):
        self.rot.angle+=1

    def draw(self):
        asp = self.width / self.height
        proj = Matrix().view_clip(-asp,asp,-1,1,1,100,1)
        self.canvas['projection_mat'] = proj

        vertices,indices=load_file.load('cubo.obj')
        
        self.rot = Rotate(angle=30,origin=(0,1,-6),axis=(0,1,0))
        Translate(0,0,-6)
        Mesh3D(load_file.process(vertices),indices)

class app(App):
    def build(self):
        return view3d()


app().run()