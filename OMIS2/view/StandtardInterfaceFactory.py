from view.Window import Window
from view.Button import Button
from view.Table import Table
from view.Field import Field
from view.Layer import Layer


class StandardInterfaceFactory:
    def __init__(self):
        pass

    def create_window(self) -> Window:
        pass

    def create_button(self) -> Button:
        pass

    def create_table(self) -> Table:
        pass

    def create_field(self) -> Field:
        pass

    def create_layer(self) -> Layer:
        pass
