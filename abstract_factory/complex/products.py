import dearpygui.dearpygui as dpg
from abc import ABC, abstractmethod
from collections import namedtuple
from dearpypixl.items.containers import ChildWindow
from dearpypixl.items.basic import Button
from dearpypixl.itemtypes import Theme
from dearpypixl.itemtypes.themes._theme import ThemeComponent, ThemeColor, ThemeStyle
from colors import *

Style = namedtuple('Style', ['x', 'y', 'category', 'label'])
Color = namedtuple('Color', ['value', 'category', 'label'])

class Widget(ABC):
    """ Abstract Product """
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def apply_theme(self):
        pass


class ThemedWidget(Widget):
    """ Concrete product base class 

    Since all themed widgets need to create their theme on instantiation
    we made this class that inherits from the ABC where the common 
    implementation of apply_theme is defined.

    All concrete products inherit from this class and implement their own
    render methods
    """    
    def create(self):
        pass

    def apply_theme(self, concrete_style: namedtuple):
        with Theme('theme') as theme:
            with ThemeComponent() as theme_component:
                for component in concrete_style: 
                    if isinstance(component, Color):
                        ThemeColor(
                            getattr(dpg, f'mvThemeCol_{component.label}'),
                            value=component.value,
                            category=component.category
                        )
                    elif isinstance(component, Style):
                        ThemeStyle(
                            getattr(dpg, f'mvStyleVar_{component.label}'), 
                            x=component.x,
                            y=component.y,
                            category=component.category                            
                        )
        self.theme = theme


class DarkWidget(ThemedWidget):
    def __init__(self) -> None:
        self.apply_theme([
            Color(value=BLACK, category=0, label='ChildBg'),
            Color(value=GRAY, category=0, label='Button'),
            Color(value=WHITE, category=0, label='Text'),
            Style(x=1, y=1, category=0, label='ChildRounding'),
            Style(x=1, y=1, category=0, label='FrameRounding')
        ])

class LightWidget(ThemedWidget):
    """ Concrete product A2 """
    def __init__(self) -> None:
        self.apply_theme([
            Color(value=OFF_WHITE, category=0, label='ChildBg'),
            Color(value=WHITE, category=0, label='Button'),
            Color(value=BLACK, category=0, label='Text'),
            Style(x=6, y=6, category=0, label='ChildRounding'),
            Style(x=12, y=12, category=0, label='FrameRounding'),
            Style(x=1, y=1, category=0, label='FrameBorderSize')
        ])

class DarkWindow(DarkWidget):
    """ Concrete product A1 """
    def create(self):
        window = ChildWindow()
        window.theme = self.theme
        return window

class LightWindow(LightWidget):
    """ Concrete product A2 """
    def create(self):
        window = ChildWindow()
        window.theme = self.theme
        return window

class DarkButton(DarkWidget):
    """ Concrete product B1 """
    def create(self):
        button = Button(events=True)
        button.theme = self.theme
        return button

class LightButton(LightWidget):
    """ Concrete product B2 """
    def create(self):
        button = Button(events=True)
        button.theme = self.theme
        return button

