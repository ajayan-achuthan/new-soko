from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton

# Set the size of the window to match your phone's resolution
# Your phone: 2400x1080 FHD+
PHONE_WIDTH = 1080
PHONE_HEIGHT = 2400

# Calculate a scaling factor to make the window fit your screen
# Adjust this value if the window is too large or small for your monitor
SCALE_FACTOR = 0.3

Window.size = (PHONE_WIDTH * SCALE_FACTOR, PHONE_HEIGHT * SCALE_FACTOR)

# Set DPI to match your phone (406 DPI)
Window.dpi = 406

class MobileApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # or "Light"
        screen = MDScreen()
        button = MDRaisedButton(
            text="Hello Mobile",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size=dp(18)  # Adjust font size using dp
        )
        screen.add_widget(button)
        return screen

if __name__ == '__main__':
    MobileApp().run()