from abc import ABC, abstractmethod
from products import Widget, DarkWindow, LightWindow, DarkButton, LightButton

class ThemeFactory(ABC):
    """ The abstract factory """
    @abstractmethod
    def window_method(self):
        pass

    @abstractmethod
    def button_method(self):
        pass

class DarkModeFactory(ThemeFactory):
    """ Concrete factory 1 """
    # Create Product A
    def window_method(self) -> Widget:
        return DarkWindow()

    # Create Product B
    def button_method(self) -> Widget:
        return DarkButton()


class LightModeFactory(ThemeFactory):
    """ Concrete factory 2 """
    # Create Product A
    def window_method(self) -> Widget:
        return LightWindow()

    # Create Product B
    def button_method(self) -> Widget:
        return LightButton()
