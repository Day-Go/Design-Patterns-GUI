from abc import ABC, abstractmethod
from products import Widget, DarkWindow, LightWindow, DarkButton, LightButton

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
    def create_window(self) -> Widget:
        return DarkWindow()

    # Create Product B
    def create_button(self) -> Widget:
        return DarkButton()


class LightModeFactory(ThemeFactory):
    """ Concrete factory 2 """
    # Create Product A
    def create_window(self) -> Widget:
        return LightWindow()

    # Create Product B
    def create_button(self) -> Widget:
        return LightButton()
