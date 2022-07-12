from abc import ABC, abstractmethod
from dearpypixl.items.containers import ChildWindow
from dearpypixl.items.basic import Button


class ThemedWindow(ABC):
    """ Abstract product A """
    @abstractmethod
    def display_window(self):
        pass

class DarkWindow(ThemedWindow):
    """ Concrete product A1 """
    def display_window(self):
        print('Making a dark window...')
        return ChildWindow('Dark window')
  
class LightWindow(ThemedWindow):
    """ Concrete product A2 """
    def display_window(self):
        print('Making a light window...')
        return ChildWindow('Light window')


class ThemedButton(ABC):
    """ Abstract product B """
    @abstractmethod
    def display_button(self):
        pass

    @abstractmethod
    def set_callback(self):
        pass

class DarkButton(ThemedButton):
    """ Concrete product B1 """
    def display_button(self):
        print('Making a dark button..')
        return Button('Dark button')

    def set_callback(self):
        pass

class LightButton(ThemedButton):
    """ Concrete product B2 """
    def display_button(self):
        print('Making a light button...')
        return Button('Light button')

    def set_callback(self):
        pass