from controller.Controller import Controller

from model.SystemComposition import SystemComposition

from view.Application import Application

from manager.ClientProfileCreationManager import ClientProfileCreationManager


class ClientProfileShowController(Controller):
    def __init__(self) -> None:
        pass

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        manager: ClientProfileCreationManager = ClientProfileCreationManager()
