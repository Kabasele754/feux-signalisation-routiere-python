from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock


class FeuxSignalisationApp(App):
    def __init__(self, **kwargs):
        super(FeuxSignalisationApp, self).__init__(**kwargs)
        self.colors = [ 'vert', 'orange', 'rouge',]
        self.index = 0

    def build(self):
        layout = FloatLayout(size=(100, 100))
        self.draw_lights(layout)
        Clock.schedule_interval(self.change_color, 5)  # Change color every 5 seconds
        return layout

    def change_color(self, dt):
        self.index = (self.index + 1) % len(self.colors)
        self.root.clear_widgets()
        self.draw_lights(self.root)

    def draw_lights(self, layout):
        with layout.canvas:
            for i, color in enumerate(self.colors):
                if i == self.index:
                    current_color = color
                    if current_color == 'rouge':
                        Color(1, 0, 0)  # rouge

                    elif current_color == 'orange':
                        Color(1, 0.5, 0)  # orange
                    elif current_color == 'vert':
                        Color(0, 1, 0)  # vert
                    Ellipse(pos=(300, 300 * i), size=(200, 200))
                else:
                    Color(0.5, 0.5, 0.5)  # gris
                    Ellipse(pos=(300, 300 * i), size=(200, 200))


if __name__ == '__main__':
    FeuxSignalisationApp().run()
