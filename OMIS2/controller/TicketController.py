from controller.Controller import Controller

from manager.StandardPickUpPointManager import StandardPickUpPointManager
from manager.TicketManager import TicketManager
from model.SystemComposition import SystemComposition

from model.Ticket import Ticket
from view.Application import Application


class TicketController(Controller):
    def __init__(self) -> None:
        self.tickets: list[Ticket] = []
        self.manager: StandardPickUpPointManager = StandardPickUpPointManager(self.tickets, {})

    def ticket_control(self) -> None:
        pass

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        ticket_manager: TicketManager = TicketManager(self.tickets)
