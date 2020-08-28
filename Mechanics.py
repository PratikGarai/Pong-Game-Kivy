from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class Paddle():

    def __init__(self, velocity):
        self.velocity = velocity
        self.position = [0,0]
        self.size = [0,0]

    def setup(self, position,size):
        self.position = position
        self.on_position()

    def move(self, direction):
        self.position[1] += direction*self.velocity
        self.parent.b1.text = str(self.position)
        self.on_position()

    def on_position(self):
        self.parent.Canvas.redraw()

class Ball():

    def __init__(self, velocity):
        self.velocity = velocity
        self.position = [0,0]
        self.size = [0,0]

    def setup(self, position, radius):
        self.position = position
        self.on_position()

    def move(self, direction):
        self.position = [self.velocity[0]+self.position[0], self.velocity[1]+self.position[1]]
        self.on_position()

    def on_position(self):
        self.parent.Canvas.redraw()

class Canvas(Widget):
    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)

    def setup(self):
        self.p1 = self.parent.PaddleLeft 
        self.p2 = self.parent.PaddleRight

    def redraw(self):
        with self.canvas :
            self.canvas.clear()
            Rectangle(pos = self.p1.position , size=self.p1.size)
            Rectangle(pos = self.p2.position , size=self.p2.size)
