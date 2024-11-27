from model.PickUpPoint import PickUpPoint
from model.Ticket import Ticket


class StandardPickUpPointManager:
    def __init__(self, tickets: list[Ticket], packages: dict) -> None:
        self.pick_up_point: PickUpPoint = PickUpPoint()
        self.tickets: list[Ticket] = tickets
        self.packages: dict = packages

    def ticket_order(self) -> None:
        pass

    def take_package(self) -> None:
        pass

    def deliver_package(self) -> None:
        pass
