from abc import ABC, abstractmethod
from products import Product
from dearpypixl.itemtypes import Item
from dearpypixl.items.containers import Window, ChildWindow, Group
from dearpypixl.items.basic import Text, Button, InputText, SliderInt 


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_text() -> None:
        pass

    @abstractmethod
    def add_button(self) -> None:
        pass

    @abstractmethod
    def add_text_input(self) -> None:
        pass

    @abstractmethod
    def add_int_slider(self) -> None:
        pass

    @abstractmethod
    def add_table(self) -> None:
        pass

    @abstractmethod
    def add_group(self) -> None:
        pass


class WindowBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def make_window(self, label: str=None, width: int=None, height: int=None):
        # The builder only needs one window per product.
        # Make a new Product instance if this method is called.
        self.reset()

        self.window = Window(label)
        if width:
            self.window.width = width
        if height:
            self.window.height = height

        self._product.add(repr(self.window), self.window)

    def add_text(self, value: str = ''):
        with self._product.window:
            Text(value)

    def add_button(self, label: str = None, parent: Item = None,
                   rel_x: float = None) -> None:
        with self.window:
            if parent:
                btn = Button(label, parent=parent)
            else:
                btn = Button(label)
            btn.width = 125

        self._product.add(repr(btn), btn)

    def add_text_input(self, label: str = None) -> None:
        with self.window:
            input_text = InputText(label)

        self._product.add(repr(input_text), input_text)

    def add_int_slider(self, label: str = None) -> None:
        with self.window:
            int_slider = SliderInt(label)

        self._product.add(repr(int_slider), int_slider)

    def add_table(self) -> None:
        pass

    def add_group(
                self, 
                horizontal: bool = False, 
                horizontal_spacing: int = None
            ) -> None:
        with self.window:
            if horizontal:
                self.group = Group(
                    horizontal=horizontal,
                    horizontal_spacing=horizontal_spacing
                )
            else:
                self.group = Group()

        self._product.add(repr(self.group), self.group)
        
