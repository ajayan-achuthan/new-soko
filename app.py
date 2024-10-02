from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout

class ClassicButton(MDRaisedButton):
    pass

KV = '''
MDScreen:
    md_bg_color: 0, 0, 0, 1
    FitImage:
        source: "D:/cwading/GitHub/new-soko/assets/images/bg-sky.png"
        size_hint: 1, 1
        pos_hint: {"center_x": .5, "center_y": .5}

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(10)

        MDLabel:
            text: "Collectiona"
            halign: "left"
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_y": .5}

        ScrollView:
            MDList:
                id: collections_list
                spacing: dp(10)

<ClassicButton>:
    size_hint: 1, None
    height: dp(500)
    md_bg_color: 0.2, 0.4, 0.2, 1
    theme_text_color: "Custom"
    text_color: 0.8, 1, 0.2, 1
    font_size: "18sp"
    padding: dp(10)

    MDBoxLayout:
        orientation: "horizontal"
        padding: 0

        MDBoxLayout:
            orientation: "vertical"
            size_hint_x: 0.9
            MDLabel:
                text: "Classics"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 0.8, 1, 0.2, 1
                font_size: "18sp"
            MDLabel:
                text: "3/86"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 0.5
                font_size: "14sp"
        MDProgressBar:
            value: 62
            size_hint_x: 0.3
            pos_hint: {"center_y": .5}
            color: 0.8, 1, 0.2, 1
'''

class CollectionsApp(MDApp):
    def build(self):
        Window.size = (360, 640)  # Adjust as needed for your device
        return Builder.load_string(KV)

    def on_start(self):
        for _ in range(8):
            button = ClassicButton()
            self.root.ids.collections_list.add_widget(button)

if __name__ == "__main__":
    CollectionsApp().run()
