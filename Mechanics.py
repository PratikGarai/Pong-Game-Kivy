from kivy.properties import ListProperty

class Paddle():
    position = ListProperty([0,0])

    def __init__(self, position):
        self.position = position
        self.velocity = 5

    def move(self, direction):
        self.position[1] += direction*velocity

    def on_position(self, instance, pos):
        #redraw on canvas
        pass

class Ball():
    position = ListProperty([0,0])

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def move(self, direction):
        self.position = [self.velocity[0]+self.position[0], self.velocity[1]+self.position[1]]

    def on_position(self, instance, pos):
        #redraw ball here
        pass
