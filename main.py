from kivy.app import App
from kivy.uix.label import Label

class MayaApp(App):
    def build(self):
        return Label(text="Hello Maya! App is Working 100%")

MayaApp().run()
