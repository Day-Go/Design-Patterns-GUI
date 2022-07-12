from abc import ABC, abstractmethod
from products import ThemedWindow, ThemedButton, DarkWindow, LightWindow, DarkButton, LightButton


class ThemeFactory(ABC):
    """ The abstract factory """
    @abstractmethod
    def create_window(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

class DarkModeFactory(ThemeFactory):
    """ Concrete factory 1 """
    # Create Product A
    def create_window(self) -> ThemedWindow:
        return DarkWindow()

    # Create Product B
    def create_button(self) -> ThemedButton:
        return DarkButton()


class LightModeFactory(ThemeFactory):
    """ Concrete factory 2 """
    # Create Product A
    def create_window(self) -> ThemedWindow:
        return LightWindow()

    # Create Product B
    def create_button(self) -> ThemedButton:
        return LightButton()
