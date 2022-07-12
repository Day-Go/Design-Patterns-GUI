from dearpypixl import Application, Viewport
from dearpypixl.items.containers import Window
from factories import ThemeFactory, DarkModeFactory, LightModeFactory

class GUI(Application, Viewport):
    def __init__(self, factory: ThemeFactory) -> None:
        self.primary_window = Window()

        window = factory.create_window()
        button = factory.create_button()
        
        with self.primary_window:
            with window.display_window():
                button.display_button()
       

        self.start()


if __name__ == '__main__':
    GUI(DarkModeFactory())
