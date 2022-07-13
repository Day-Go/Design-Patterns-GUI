"""
Written by John Long - 13/07/2022
"""
import inspect
from dearpypixl import Application, Viewport
from dearpypixl.items.containers import Window, Group, Tooltip
from dearpypixl.items.basic import Text, Button
from dearpypixl.viewport import get_mouse_pos
from director import Director
from builders import WindowBuilder

def source_to_string(method: object):
    return f'Source code:\n\n{inspect.getsource(method)}'


class GUI(Application, Viewport):
    def __init__(self) -> None:
        self.director = Director() 
        self.builder = WindowBuilder() 
        self.director.builder = self.builder

        with Window('Example director methods', pos=(500,300)) as self.director_window:
            # Director method 1
            btn_form = Button('Tell the builder to build a form', events=True)
            with Tooltip(parent=btn_form):
                source_code = source_to_string(self.director.build_form)
                Text(source_code)

            # Director method 2
            btn_numpad = Button('Tell the builder to build a number pad', 
                                events=True)
            with Tooltip(parent=btn_numpad):
                source_code = source_to_string(self.director.build_numberpad)
                Text(source_code)

            # Director method 3
            btn_calc = Button('Tell the builder to build a calculator', 
                              events=True)
            with Tooltip(parent=btn_calc):
                source_code = source_to_string(self.director.build_calculator)
                Text(source_code)

            # Customizable method
            btn_custom = Button('Make your own director method!', events=True)

        @btn_form.events.on_click
        def _():
            self.director.build_form()
    
        @btn_numpad.events.on_click
        def _():
            self.director.build_numberpad()

        @btn_calc.events.on_click
        def _():
            self.director.build_calculator()

        @btn_custom.events.on_click
        def _():
            self.director.build_a_director()
        
        
        self.start()

if __name__ == '__main__':
    GUI()
