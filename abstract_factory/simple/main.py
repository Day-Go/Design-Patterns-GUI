"""
Written by John Long - 11/07/2022

This is a simple example of the abstract factory design pattern.
The pattern is applied to a GUI application using the dearpypixl GUI library.
In this example only the bear minimum functionality is implemented.
The code follows the abstract UML diagram as shown in the seminal design 
patterns textbook informally know as the Gang of Four Design Patterns
(Design Patterns: Elements of Reusable Object-Oriented Software).

The example doesn't implement any useful features. It was written as an
exercise to get a better understanding of the design pattern. Different 
messages will be printed to the command line depending on which factory is
passed to the GUI class but the theme of the rendered objects won't change.

See the complex example for a more functional demonstration.
"""
from dearpypixl import Application, Viewport
from dearpypixl.items.containers import Window
from factories import ThemeFactory, DarkModeFactory, LightModeFactory


class GUI(Application, Viewport):
    """ The 'client code' that uses (has a) abstract factory 
    
    Args:
        - factory (ThemeFactory): Abstract factory for creating themed widgets.
    """
    def __init__(self, factory: ThemeFactory) -> None:
        self.primary_window = Window()

        window = factory.create_window()
        button = factory.create_button()
        
        with self.primary_window:
            with window.display_window():
                button.display_button()
       
        self.start()


if __name__ == '__main__':
    GUI(LightModeFactory())
    # GUI(DarkModeFactory())  # < --- Uncomment to change GUI theme