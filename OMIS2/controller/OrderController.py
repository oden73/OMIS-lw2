from controller.Controller import Controller

from manager.StandardOrderManager import StandardOrderManager
from manager.OrderManager import OrderManager

from model.Order import Order
from model.SystemComposition import SystemComposition
from view.Application import Application


class OrderController(Controller):
    def __init__(self) -> None:
        self.orders: list[Order] = []
        self.manager: StandardOrderManager = StandardOrderManager()

    def control_courier_orders(self) -> None:
        order_manager: OrderManager = OrderManager()

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        pass
