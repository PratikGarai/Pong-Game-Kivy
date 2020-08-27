from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class GamePanel(BoxLayout):
    def __init__(self, **kwargs):
        super(GamePanel, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.add_widget(Button(text = "Left"))
        self.add_widget(Button(text = "Right"))

    def setup(self):
        self.size_hint = (1, 0.95)
        self.pos_hint = {'top':0.95}
