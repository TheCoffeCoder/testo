from kivy.garden.mapview import MapView
from kivymd.app import MDApp

class Map(MapView):
    pass

class MainApp(MDApp):
    def build(self):
        return Map()

MainApp().run()

