from typing import Any
from pprint import PrettyPrinter

class Product():
    def __init__(self) -> None:
        self.widgets = {}
        self.pp = PrettyPrinter(indent=4)

    def add(self, widget_repr: str, widget: object) -> None:
        self.widgets.update({widget_repr: widget})

    def list_parts(self) -> None:
        print('Product parts:')
        self.pp.pprint(self.widgets)