from abc import ABC, abstractmethod
from dearpypixl.items.containers import ChildWindow
from dearpypixl.items.basic import Button


class ThemedWindow(ABC):
    """ Abstract product A """
    @abstractmethod
    def render_window(self):
        pass

class DarkWindow(ThemedWindow):
    """ Concrete product A1 """
    def render_window(self):
        print('Rendering a dark window...')
        return ChildWindow('Dark window')
  
class LightWindow(ThemedWindow):
    """ Concrete product A2 """
    def render_window(self):
        print('Rendering a light window...')
        return ChildWindow('Light window')


class ThemedButton(ABC):
    """ Abstract product B """
    @abstractmethod
    def render_button(self):
        pass

class DarkButton(ThemedButton):
    """ Concrete product B1 """
    def render_button(self):
        print('Rendering a dark button..')
        return Button('Dark button')

class LightButton(ThemedButton):
    """ Concrete product B2 """
    def render_button(self):
        print('Rendering a light button...')
        return Button('Light button')
