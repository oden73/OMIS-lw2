from controller.Controller import Controller

from manager.AdminCommunicationManager import AdminCommunicationManager
from manager.CommunicationManager import CommunicationManager
from model.SystemComposition import SystemComposition

from model.User import User
from model.Admin import Admin
from view.Application import Application


class AdminCommunicationController(Controller):
    def __init__(self) -> None:
        self.manager: CommunicationManager = CommunicationManager(User(), User())

    def control_messages_to_admin(self) -> None:
        admin_manager: AdminCommunicationManager = AdminCommunicationManager(User(), Admin())

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        pass
