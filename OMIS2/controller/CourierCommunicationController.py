from controller.Controller import Controller

from manager.CourierCommunicationManager import CourierCommunicationManager
from manager.CommunicationManager import CommunicationManager
from model.SystemComposition import SystemComposition

from model.User import User
from model.Courier import Courier
from view.Application import Application


class CourierCommunicationController(Controller):
    def __init__(self) -> None:
        self.manager: CommunicationManager = CommunicationManager(User(), User())

    def control_messages_to_courier(self) -> None:
        courier_manager: CourierCommunicationManager = CourierCommunicationManager(User(), Courier())

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        pass
