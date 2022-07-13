from builders import WindowBuilder


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
        self.builder.make_window('Build-a-director')
        self.builder.add_text_input('Method name')

        self.builder._product.list_parts()
        return self.builder.product
