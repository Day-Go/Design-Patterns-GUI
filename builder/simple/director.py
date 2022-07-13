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

    def build_simple_window(self) -> None:
        self.builder.add_button()

    def build_complex_window(self) -> None:
        self.builder.add_button()
        self.builder.add_text_input()
        self.builder.add_int_slider()
