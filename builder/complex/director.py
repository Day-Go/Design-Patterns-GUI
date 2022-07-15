from pandas import value_counts
from builders import WindowBuilder
import inspect

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> WindowBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: WindowBuilder) -> None:
        self._builder = builder

    def build_form(self) -> None:
        self.builder.make_window('Customer satisfaction form',
                                  width=400, height=125)

        self.builder.add_text_input('Full name')
        self.builder.add_text_input('Occupation')
        self.builder.add_int_slider('Satisfaction')
        self.builder.add_button('Submit')

        self.builder._product.list_parts()

    def build_numberpad(self):
        self.builder.make_window('Simple number pad',
                                  width=410, height=100)

        self.builder.add_group(horizontal=True, horizontal_spacing=10)
        [self.builder.add_button(label=n, parent=self.builder.group) 
         for n in [7, 8, 9]]

        self.builder.add_group(horizontal=True, horizontal_spacing=10)
        [self.builder.add_button(label=n, parent=self.builder.group) 
         for n in [4, 5, 6]]

        self.builder.add_group(horizontal=True, horizontal_spacing=10)
        [self.builder.add_button(label=n, parent=self.builder.group) 
         for n in [1, 2, 3]]

        self.builder._product.list_parts()

    def build_calculator(self):
        self.build_numberpad()
        self.builder.window.label = 'Simple calculator'

        self.builder._product.list_parts()

    def build_a_director(self):
        self.code_string = 'from dearpypixl.items.containers import Window, ChildWindow, Group\nfrom dearpypixl.items.basic import Text, Button, InputText, SliderInt\n\ndef custom_director():\n\twith Window():\n'.format(None)

        self.builder.make_window('Build-a-director', width=1200, height=700)
        self.builder.add_text_input('Widget label')
        print(self.builder.input_text)

        self.builder.add_group(horizontal=True, horizontal_spacing=10)
        for method in dir(self.builder):
            if 'add' in method:
                self.builder.add_button(method, parent=self.builder.group)

        self.n_leading_tabs = 2
        callback_values = {}
        for i, (key, val) in enumerate(self.builder.__dict__.items()):
            if '(' in key:
                def cb(sender):
                    widget_type = sender.label.split('_')[1:]
                    widget_type = [string.capitalize() for string in widget_type]
                    widget_type = ''.join(widget_type)

                    tab = '\t'
                    leading_tabs = ''
                    for _ in range(self.n_leading_tabs):
                        leading_tabs += tab         
                    
                    if self.builder.input_text.value:
                        new_string = f'{widget_type}(label="{self.builder.input_text.value}")'
                    else:
                        new_string = f'{widget_type}()'

                    print(widget_type)
                    if widget_type == 'Text':

                        new_string = new_string.replace('label', 'default_value')

                    if widget_type == 'ChildWindow' or widget_type == 'Group':
                       self.code_string += leading_tabs + 'with ' + new_string + ':\n'
                       self.n_leading_tabs += 1
                    else:
                        self.code_string += leading_tabs + new_string + '\n'

                    self.builder.text.value = self.code_string

                val.callback = cb

        self.builder.add_button('Create')


        print(f'{globals()=}')
        print(f'{locals()=}')
        for i, (key, val) in enumerate(self.builder.__dict__.items()):
            print(key)
            if 'Create' in key:
                def create_cb(sender):
                    print('creating...')
                    self.code_string += 'custom_director()' 
                    exec(self.code_string, globals())
                val.callback = create_cb
        


        # @self.builder.button.events

        self.builder.add_group(horizontal=True, horizontal_spacing=10)
        # self.builder.add_child_window(self.builder.group)
        self.builder.add_child_window(self.builder.group)
        self.builder.add_text(self.code_string, parent=self.builder.child_window)
        self.builder._product.list_parts()

        return self.builder.product
