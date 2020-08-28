from kivy.properties import ListProperty

class Paddle():
    position = ListProperty([0,0])

    def __init__(self, velocity):
        self.velocity = velocity

    def setup(self, position):
        self.position = position

    def move(self, direction):
        self.position[1] += direction*velocity

    def on_position(self, instance, pos):
        #nthing yet
        pass

class Ball():
    position = ListProperty([0,0])

    def __init__(self, velocity):
        self.velocity = velocity

    def setup(self, position):
        self.position = position

    def move(self, direction):
        self.position = [self.velocity[0]+self.position[0], self.velocity[1]+self.position[1]]

    def on_position(self, instance, pos):
        #redraw ball here
        pass

class Canvas
