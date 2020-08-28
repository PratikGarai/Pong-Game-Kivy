from kivy.uix.widget import Widget

class Paddle():

    def __init__(self, velocity):
        self.position = [0,0]
        self.velocity = velocity

    def setup(self, position):
        self.position = position
        self.on_position()

    def move(self, direction):
        self.position[1] += direction*self.velocity
        self.on_position()

    def on_position(self):
        #nthing yet
        pass

class Ball():

    def __init__(self, velocity):
        self.position = [0,0]
        self.velocity = velocity

    def setup(self, position):
        self.position = position
        self.on_position()

    def move(self, direction):
        self.position = [self.velocity[0]+self.position[0], self.velocity[1]+self.position[1]]
        self.on_position()

    def on_position(self):
        #redraw ball here
        pass

class Canvas(Widget):
    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)
