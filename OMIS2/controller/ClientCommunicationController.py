from controller.Controller import Controller

from manager.ClientCommunicationManager import ClientCommunicationManager
from manager.CommunicationManager import CommunicationManager
from model.SystemComposition import SystemComposition

from model.User import User
from model.Client import Client
from view.Application import Application


class CourierCommunicationController(Controller):
    def __init__(self) -> None:
        self.manager: CommunicationManager = CommunicationManager(User(), User())

    def control_messages_to_client(self) -> None:
        client_manager: ClientCommunicationManager = ClientCommunicationManager(User(), Client())

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        pass
