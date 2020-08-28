from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from Mechanics import Paddle, Ball, Canvas

Window.size = (650,400)

class GamePanel(RelativeLayout):
    def __init__(self, **kwargs):
        super(GamePanel, self).__init__(**kwargs)
        self.b1 = Label(text="Left")
        self.add_widget(self.b1)

        self.PaddleRight = Paddle(5)
        self.PaddleLeft = Paddle(5)
        self.Ball = Ball(5)
        self.Canvas = Canvas()

        self.add_widget(self.Canvas)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
        self.b1.text = "keyboard quit"

    def setup(self):
        sz = Window.size
        szp = [sz[0]/8, sz[0]/20]
        
        self.size_hint = (1, 0.95)
        self.pos_hint = {'top':0.95}

        self.PaddleRight.parent = self
        self.PaddleLeft.parent = self
        self.Ball.parent = self
        
        self.Canvas.setup()
        self.Ball.setup([0,0], 5)
        self.PaddleLeft.setup([0,sz[1]/2], szp)
        self.PaddleRight.setup([sz[0],sz[1]/2], szp)

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1]=='up':
            self.PaddleRight.move(1)
        elif keycode[1]=='down':
            self.PaddleRight.move(-1)
        elif keycode[1]=='w':
            self.PaddleLeft.move(1)
        elif keycode[1]=='s':
            self.PaddleLeft.move(-1)
