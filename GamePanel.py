from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class GamePanel(BoxLayout):
    def __init__(self, **kwargs):
        super(GamePanel, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.b1 = Button(text="Left")
        self.b2 = Button(text="Right")
        self.add_widget(self.b1)
        self.add_widget(self.b2)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
        self.b1.text = "keyboard quit"

    def setup(self):
        self.size_hint = (1, 0.95)
        self.pos_hint = {'top':0.95}

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1]=='w':
            self.b1.text = str(keyboard)+"\n"+str(text)+"\n"+str(modifiers)
        if keycode[1]=='up':
            self.b2.text = str(keycode)
