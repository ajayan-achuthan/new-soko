from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.uix.image import Image

class SokobanGame(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid_size = 10
        self.cell_size = min(Window.width, Window.height - 100) // self.grid_size
        self.grid_start_x = (Window.width - self.cell_size * self.grid_size) // 2
        self.grid_start_y = (Window.height - self.cell_size * self.grid_size - 100) // 2

        self.level = [
            "##########",
            "#  $  #  #",
            "#  # $#  #",
            "## #  #  #",
            "## # $## #",
            "#  #  ## #",
            "#    $## #",
            "#   #  @ #",
            "##########"
        ]

        self.player_pos = None
        self.boxes = set()
        self.targets = set()
        self.player_direction = 'down'

        self.load_level()
        self.load_images()
        self.draw_game()

        # Add direction buttons
        button_layout = MDBoxLayout(orientation='horizontal', spacing="10dp", padding="10dp", size_hint=(1, None), height="100dp", pos_hint={'center_x': 0.5, 'y': 0})
        
        left_button = MDIconButton(icon="assets/images/game/game_left_btn.png", on_press=lambda x: self.move('left'), size_hint=(None, None), size=(80, 80))
        right_button = MDIconButton(icon="assets/images/game/game_right_btn.png", on_press=lambda x: self.move('right'), size_hint=(None, None), size=(80, 80))
        up_button = MDIconButton(icon="assets/images/game/game_up_btn.png", on_press=lambda x: self.move('up'), size_hint=(None, None), size=(80, 80))
        down_button = MDIconButton(icon="assets/images/game/game_down_btn.png", on_press=lambda x: self.move('down'), size_hint=(None, None), size=(80, 80))

        button_layout.add_widget(left_button)
        button_layout.add_widget(down_button)
        button_layout.add_widget(up_button)
        button_layout.add_widget(right_button)

        self.add_widget(button_layout)

    def load_images(self):
        self.images = {
            'wall': Image(source='assets/images/game/wall.png').texture,
            'floor': Image(source='assets/images/game/floor.png').texture,
            'box': Image(source='assets/images/game/box.png').texture,
            'box_docked': Image(source='assets/images/game/box_docked.png').texture,
            'dock': Image(source='assets/images/game/dock.png').texture,
            'worker': Image(source='assets/images/game/worker.png').texture,
            'worker_dock': Image(source='assets/images/game/worker_dock.png').texture,
            'worker_up': Image(source='assets/images/game/worker_up.png').texture,
            'worker_down': Image(source='assets/images/game/worker_down.png').texture,
            'worker_left': Image(source='assets/images/game/worker_left.png').texture,
            'worker_right': Image(source='assets/images/game/worker_right.png').texture,
            'worker_dock_up': Image(source='assets/images/game/worker_dock_up.png').texture,
            'worker_dock_down': Image(source='assets/images/game/worker_dock_down.png').texture,
            'worker_dock_left': Image(source='assets/images/game/worker_dock_left.png').texture,
            'worker_dock_right': Image(source='assets/images/game/worker_dock_right.png').texture,
        }

    def load_level(self):
        for y, row in enumerate(self.level):
            for x, cell in enumerate(row):
                if cell == '@':
                    self.player_pos = (x, y)
                elif cell == '$':
                    self.boxes.add((x, y))
                elif cell == '.':
                    self.targets.add((x, y))
                elif cell == '*':
                    self.boxes.add((x, y))
                    self.targets.add((x, y))

    def draw_game(self):
        self.canvas.clear()
        with self.canvas:
            # Draw background
            Rectangle(source='assets/images/game/game_bg.png', pos=(0, 0), size=Window.size)

            for y, row in enumerate(self.level):
                for x, cell in enumerate(row):
                    pos_x = self.grid_start_x + x * self.cell_size
                    pos_y = self.grid_start_y + (self.grid_size - y - 1) * self.cell_size

                    if cell == '#':
                        Rectangle(texture=self.images['wall'], pos=(pos_x, pos_y), size=(self.cell_size, self.cell_size))
                    else:
                        Rectangle(texture=self.images['floor'], pos=(pos_x, pos_y), size=(self.cell_size, self.cell_size))

                    if (x, y) in self.targets:
                        Rectangle(texture=self.images['dock'], pos=(pos_x, pos_y), size=(self.cell_size, self.cell_size))

                    if (x, y) in self.boxes:
                        if (x, y) in self.targets:
                            Rectangle(texture=self.images['box_docked'], pos=(pos_x, pos_y), size=(self.cell_size, self.cell_size))
                        else:
                            Rectangle(texture=self.images['box'], pos=(pos_x, pos_y), size=(self.cell_size, self.cell_size))

                    if (x, y) == self.player_pos:
                        if (x, y) in self.targets:
                            Rectangle(texture=self.images[f'worker_dock_{self.player_direction}'], pos=(pos_x, pos_y), size=(self.cell_size, self.cell_size))
                        else:
                            Rectangle(texture=self.images[f'worker_{self.player_direction}'], pos=(pos_x, pos_y), size=(self.cell_size, self.cell_size))

    def move(self, direction):
        dx, dy = {
            'left': (-1, 0),
            'right': (1, 0),
            'up': (0, -1),
            'down': (0, 1)
        }[direction]

        self.player_direction = direction
        new_x, new_y = self.player_pos[0] + dx, self.player_pos[1] + dy

        if self.level[new_y][new_x] != '#':
            if (new_x, new_y) in self.boxes:
                box_new_x, box_new_y = new_x + dx, new_y + dy
                if self.level[box_new_y][box_new_x] != '#' and (box_new_x, box_new_y) not in self.boxes:
                    self.boxes.remove((new_x, new_y))
                    self.boxes.add((box_new_x, box_new_y))
                    self.player_pos = (new_x, new_y)
            else:
                self.player_pos = (new_x, new_y)

        self.draw_game()
        self.check_win()

    def check_win(self):
        if self.boxes == self.targets:
            print("Congratulations! You won!")

class SokobanApp(MDApp):
    def build(self):
        return SokobanGame()

if __name__ == '__main__':
    # PHONE_WIDTH = 1080
    # PHONE_HEIGHT = 2400

    # # Calculate a scaling factor to make the window fit your screen
    # # Adjust this value if the window is too large or small for your monitor
    # SCALE_FACTOR = 0.3

    # Window.size = (PHONE_WIDTH * SCALE_FACTOR, PHONE_HEIGHT * SCALE_FACTOR)

    # # Set DPI to match your phone (406 DPI)
    # Window.dpi = 406
    SokobanApp().run()