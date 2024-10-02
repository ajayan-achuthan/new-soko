from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton  # Using MDRaisedButton from kivymd
from kivy.utils import get_color_from_hex

KV = '''
Screen:
    MDFloatLayout:
        Image:
            source: 'D:/cwading/GitHub/new-soko/assets/images/levels/level_bg.png'
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        GridLayout:
            id: button_grid
            cols: 4
            rows: 4
            padding: dp(20)
            spacing: dp(10)
            size_hint: None, None
            width: self.minimum_width
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
'''

class LevelSelectorApp(MDApp):

    def build(self):
        self.title = "Level Selector"
        screen = Builder.load_string(KV)

        # Defining grid layout for buttons
        button_grid = screen.ids.button_grid

        for i in range(1, 16):
            if i == 9:
                # Empty button with a green background
                btn = MDRaisedButton(text=str(i), font_size='24sp', md_bg_color=get_color_from_hex("#B3FF00"),
                                     text_color=(0, 0, 0, 1))
            else:
                # Regular buttons
                btn = MDRaisedButton(text=str(i), font_size='24sp', md_bg_color=get_color_from_hex("#B3FF00"),
                                     text_color=(0, 0, 0, 1))

            # Manually set size and shape to ensure square buttons
            btn.size_hint = None, None
            btn.size = (100, 100)  # Square size
            btn.size_hint_min = (100, 100)  # Ensuring the button remains square
            button_grid.add_widget(btn)

        return screen


if __name__ == "__main__":
    LevelSelectorApp().run()
