from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window
from kivymd.uix.list import OneLineIconListItem
from kivymd.theming import ThemeManager
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.scrollview import MDScrollView

class ImageButton(Button):
    pass

class MainScreen(Screen):
    theme_cls = ThemeManager()
    theme_cls.theme_style = "Dark"
    def start_game(self):
        self.manager.current = 'new_game'

    def open_settings(self):
        print("Settings opened")

    def exit_game(self):
        MDApp.get_running_app().stop()

class NewGameScreen(Screen):
    def on_enter(self):
        app = App.get_running_app()
        self.ids.container.clear_widgets()
        icons_item = {
            "Glucose": "circle",
            "Medicine": "pill",
            "Carbs": "food-apple",
            "A1C": "water",
            "Exercise": "run",
            "Weight": "scale-bathroom"
        }
        for item_name, icon in icons_item.items():
            if item_name == "Carbs":
                item = IconListItem(text=item_name, icon=icon, bg_color=(1, 0.8, 0.2, 1))
            else:
                item = IconListItem(text=item_name, icon=icon, bg_color=(0.2, 0.2, 0.2, 1))

            item.bind(on_release=app.show_levels('levels'))
            # item.bind(on_release=lambda instance, x=item: self.manager.current : 'levels')
            self.ids.container.add_widget(item)

class LevelScreen(Screen):
    def on_enter(self):
        grid_layout = GridLayout(cols=4, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        for i in range(1, 101):  # Create 100 buttons
            button = MDRaisedButton(text=str(i), md_bg_color=(0, 0, 0, 1), theme_text_color="Custom", text_color=(1, 1, 1, 1), size_hint=(None, None), size=("40dp", "40dp"))
            grid_layout.add_widget(button)

        scroll_view = MDScrollView()
        scroll_view.add_widget(grid_layout)

        self.add_widget(scroll_view)

class GameScreen(Screen):
    pass

class GameCompleted(Screen):
    pass

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class CollectionsApp(MDApp):
    def build(self):
        Builder.load_file('collections.kv')
        sm = ScreenManager()
        sm.add_widget(NewGameScreen(name='new_game'))
        sm.add_widget(LevelScreen(name='levels'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(GameCompleted(name='complete'))
        return sm

    def show_levels(self, instance):
        self.collection = "collection"
        # self.no_levels = utils.count_levels(collection)
        self.root.current = 'new_game'

if __name__ == '__main__':
    CollectionsApp().run()
