from controller.Controller import Controller

from manager.ProfileCreationManager import ProfileCreationManager
from model.SystemComposition import SystemComposition
from view.Application import Application


class AdminProfileManagementController(Controller):
    def __init__(self) -> None:
        self.manager: ProfileCreationManager = ProfileCreationManager()

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        pass
