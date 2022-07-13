from abc import ABC, abstractmethod
from products import Product


class WindowBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
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


class SimpleBuilder(WindowBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        print('New product started -> Resetting product state.')
        self.reset()
        return product

    def add_button(self) -> None:
        self._product.add("button")

    def add_text_input(self) -> None:
        self._product.add("input_text")

    def add_int_slider(self) -> None:
        self._product.add("int_slider")