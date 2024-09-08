from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.image import Image

# Setting the window size (Optional)
Window.size = (360, 640)  # You can adjust this as per your need

# Main Screen
class MainScreen(Screen):
    pass

# Screen Manager
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Optional theme
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')

    def start_game(self, instance):
        print("Start Game button pressed.")
        # Implement your game start logic here

    def open_settings(self):
        print("Settings button pressed.")
        # Implement settings logic here

    def exit_app(self):
        print("Exit button pressed.")
        self.stop()

# Run the app
if __name__ == '__main__':
    MainApp().run()
