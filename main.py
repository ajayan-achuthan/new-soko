from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
import os
import importlib
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from kivymd.app import MDApp

# Add the parent directory of 'ui' to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AppReloader(FileSystemEventHandler):
    def __init__(self, reload_func):
        self.reload_func = reload_func

    def on_modified(self, event):
        if event.src_path.endswith(('collections.py', 'collections.kv')):
            Clock.schedule_once(lambda dt: self.reload_func(), 0.1)

class HotReload(BoxLayout):
    def __init__(self, **kwargs):
        super(HotReload, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.app_container = BoxLayout()
        self.add_widget(self.app_container)
        self.current_app = None
        Clock.schedule_once(self.load_app, 0)

        # Set up watchdog
        self.observer = Observer()
        self.observer.schedule(AppReloader(self.load_app), path='ui', recursive=False)
        self.observer.start()

    def load_app(self, *args):
        try:
            # Clean up the previous app instance if it exists
            if self.current_app:
                self.current_app.on_stop()
                self.current_app.root_window.remove_widget(self.current_app.root)

            # Reload the KV file
            Builder.unload_file('ui/collections.kv')
            Builder.load_file('ui/collections.kv')

            # Reload the Python module
            module = importlib.import_module('ui.collections')
            importlib.reload(module)
            app_class = getattr(module, 'CollectionsApp')

            # Create a new app instance
            app_instance = app_class()
            app_instance.load_all_kv_files(app_instance.kv_directory)
            root_widget = app_instance.build()
            if root_widget is None:
                print("Error: build() method returned None")
                return

            self.app_container.clear_widgets()
            self.app_container.add_widget(root_widget)

            # Call on_start method
            Clock.schedule_once(lambda dt: app_instance.on_start())

            self.current_app = app_instance
            print("App reloaded successfully")
        except Exception as e:
            print(f"Error loading app: {e}")
            import traceback
            traceback.print_exc()

    def on_stop(self):
        if self.current_app:
            self.current_app.on_stop()
        self.observer.stop()
        self.observer.join()

class HotReloadApp(MDApp):
    def build(self):
        return HotReload()

    def on_stop(self):
        self.root.on_stop()

if __name__ == '__main__':
    HotReloadApp().run()
