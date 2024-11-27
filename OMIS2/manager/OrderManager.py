from manager.StandardOrderManager import StandardOrderManager

from model.Order import Order


class OrderManager(StandardOrderManager):
    def __init__(self) -> None:
        super().__init__()

    def show_order(self) -> None:
        pass

    def take_order(self) -> None:
        pass
