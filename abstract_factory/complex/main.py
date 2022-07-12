from dearpypixl import Application, Viewport
from dearpypixl.items.containers import Window, Group
from dearpypixl.items.basic import Text
from factories import ThemeFactory, DarkModeFactory, LightModeFactory
from colors import *

class GUI(Application, Viewport):
    def __init__(self, factories: dict[ThemeFactory]) -> None:
        self.primary_window = Window()

        dark_factory = factories['dark_mode']
        light_factory = factories['light_mode']

        dark_window = dark_factory.create_window()
        light_window = light_factory.create_window()

        dark_button = dark_factory.create_button()
        light_button = light_factory.create_button()

        with self.primary_window:
            with Group(width=620, horizontal=True):
                with dark_window.render():
                    Text('Dark mode factory', color=WHITE)
                    with Group(width=300, horizontal=True):
                        dark_btn_factory = dark_button.render()
                        dark_btn_factory.label = 'New dark button'
                        dark_win_factory = dark_button.render()
                        dark_win_factory.label = 'New dark window'
                    with Group():
                        self.dark_factory_output = dark_window.render()
                    
                with light_window.render():
                    Text('Light mode factory', color=BLACK)
                    with Group(width=300, horizontal=True):
                        light_btn_factory = light_button.render()
                        light_btn_factory.label = 'New light button'
                        light_win_factory = light_button.render()
                        light_win_factory.label = 'New light window'
                    with Group():
                        self.light_factory_output = light_window.render()

        @dark_btn_factory.events.on_click
        def create_dark_button():
            with self.dark_factory_output:
                dark_button.render().label = "I'm a new dark button!"

        @dark_win_factory.events.on_click
        def create_dark_window():
            with self.dark_factory_output:
                self.dark_factory_output = dark_window.render()

        @light_btn_factory.events.on_click
        def create_light_button():
            with self.light_factory_output:
                light_button.render().label = "I'm a new light button!"

        @light_win_factory.events.on_click
        def create_light_window():
            with self.light_factory_output:
                self.light_factory_output = light_window.render()

        self.start()

if __name__ == '__main__':
    factories = {
        'dark_mode': DarkModeFactory(),
        'light_mode': LightModeFactory()  
    }

    GUI(factories)
