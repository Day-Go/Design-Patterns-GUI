"""
Written by John Long - 13/07/2022

A minimum working example of the builder design pattern. The example shows
how window components (widgets) can be composed in a certain order by
the builder to form unique window styles. 

The WindowBuilder provides an interface for what methods a builder can 
implement. The Director class has a builder that it can use construct 
complex windows by implementing methods that outline the order and 
quantity of each widget. In this implementation, a Product is a window 
that has been populated with widgets. 
"""

from dearpypixl import Application, Viewport
from dearpypixl.items.containers import Window, Group
from dearpypixl.items.basic import Text
from director import Director
from builders import SimpleBuilder

class GUI(Application, Viewport):
    def __init__(self) -> None:
        self.director = Director() 
        self.builder = SimpleBuilder() 
        self.director.builder = self.builder

        print('Building simple window...')
        self.director.build_simple_window()
        self.builder.product.list_parts()


        # NOTE: Each time the builder builds a new product it will reset
        #       its product property. In this implementation that means
        #       that the builder can only build one window at a time. 
        #       When it builds a new product, the previous one is cleared.

        print("Building a more complex window...")
        self.director.build_complex_window()
        self.builder.product.list_parts()

if __name__ == '__main__':
    GUI()
