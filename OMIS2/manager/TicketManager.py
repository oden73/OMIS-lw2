from manager.StandardPickUpPointManager import StandardPickUpPointManager

from model.Ticket import Ticket


class TicketManager(StandardPickUpPointManager):
    def __init__(self, tickets: list[Ticket]) -> None:
        super().__init__(tickets, {})

    def ticket_order(self) -> None:
        pass