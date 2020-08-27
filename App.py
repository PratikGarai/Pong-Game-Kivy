from kivy.app import App
from kivy.uix.label import Label

class PongApp(App):
    def build(self):
        return Label(text="hello")

if __name__=='__main__':
    PongApp().run()
