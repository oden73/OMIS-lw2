from view.InterfaceFactory import InterfaceFactory


class Application:
    def __init__(self):
        self.factory: InterfaceFactory = InterfaceFactory()
        self.windows: dict = {}

    def create_interface(self) -> None:
        pass

    def create_button(self) -> None:
        pass

    def create_table(self) -> None:
        pass

    def draw_interface(self) -> None:
        pass
