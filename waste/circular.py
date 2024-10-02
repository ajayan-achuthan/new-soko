from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.label import Label
from kivy.clock import Clock


class CircularProgressBar((Widget)):
    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        self.percentage = 0  # Initial percentage
        self.max_percentage = 74  # Target percentage as shown in your image
        self.size = (200, 200)  # Size of the widget
        self.label = Label(text="0%", font_size=40, pos=(self.center_x - 50, self.center_y - 50))
        self.add_widget(self.label)
        Clock.schedule_interval(self.update_progress, 0.1)

    def on_size(self, *args):
        self.draw()

    def draw(self):
        self.canvas.clear()
        with self.canvas:
            # Background Circle (Light grey)
            Color(0.9, 0.9, 0.9)
            Line(circle=(self.center_x, self.center_y, self.width / 3), width=10)

            # Progress Circle (Green)
            Color(0, 1, 0)
            Line(circle=(self.center_x, self.center_y, self.width / 3, 0, 360 * (self.percentage / 100)),
                 width=10)

    def update_progress(self, dt):
        if self.percentage < self.max_percentage:
            self.percentage += 1  # Increment the percentage
            self.label.text = f"{int(self.percentage)}%"  # Update the label text
            self.label.pos = (self.center_x - 25, self.center_y - 25)  # Reposition the label
            self.draw()  # Redraw the circle


class CircularProgressBarApp(App):
    def build(self):
        return CircularProgressBar()


if __name__ == '__main__':
    CircularProgressBarApp().run()
