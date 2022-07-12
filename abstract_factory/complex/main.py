"""
Written by John Long - 12/07/2022

This example shows a more functional implementation of the abstract factory
design pattern. There are two main difference in terms of design when compared 
to the simple example. 
    1. The two abstract products from the simple example are combined into a 
       single abstract base class since all of the products only need to 
       implement a create method. All other functionality is handled by the 
       dearpypixl library.
    2. We introduce a concrete product base class (ThemedWidget) which inherits 
       from the abstract product base class (Widget). The concrete product
       base class is the parent of all concrete products and it implements the
       apply_theme method, which all ThemedWidgets share.

The demonstration shows how themed components can be created from the GUI while
it is running.
"""
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

        dark_window = dark_factory.window_method()
        light_window = light_factory.window_method()

        dark_button = dark_factory.button_method()
        light_button = light_factory.button_method()

        with self.primary_window:
            with Group(width=620, horizontal=True):
                with dark_window.create():
                    Text('Dark mode factory', color=WHITE)
                    with Group(width=300, horizontal=True):
                        dark_btn_factory = dark_button.create()
                        dark_btn_factory.label = 'New dark button'
                        dark_win_factory = dark_button.create()
                        dark_win_factory.label = 'New dark window'
                    with Group():
                        self.dark_factory_output = dark_window.create()
                    
                with light_window.create():
                    Text('Light mode factory', color=BLACK)
                    with Group(width=300, horizontal=True):
                        light_btn_factory = light_button.create()
                        light_btn_factory.label = 'New light button'
                        light_win_factory = light_button.create()
                        light_win_factory.label = 'New light window'
                    with Group():
                        self.light_factory_output = light_window.create()

        @dark_btn_factory.events.on_click
        def create_dark_button():
            with self.dark_factory_output:
                dark_button.create().label = "I'm a new dark button!"

        @dark_win_factory.events.on_click
        def create_dark_window():
            with self.dark_factory_output:
                self.dark_factory_output = dark_window.create()

        @light_btn_factory.events.on_click
        def create_light_button():
            with self.light_factory_output:
                light_button.create().label = "I'm a new light button!"

        @light_win_factory.events.on_click
        def create_light_window():
            with self.light_factory_output:
                self.light_factory_output = light_window.create()

        self.start()

if __name__ == '__main__':
    factories = {
        'dark_mode': DarkModeFactory(),
        'light_mode': LightModeFactory()  
    }

    GUI(factories)
