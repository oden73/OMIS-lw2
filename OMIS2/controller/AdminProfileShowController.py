from controller.Controller import Controller
from model.SystemComposition import SystemComposition
from view.Application import Application

from manager.AdminProfileCreationManager import AdminProfileCreationManager

class AdminProfileShowController(Controller):
    def __init__(self) -> None:
        pass

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        manager: AdminProfileCreationManager = AdminProfileCreationManager()
    