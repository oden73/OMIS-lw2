from controller.Controller import Controller

from handler.AuthHandler import AuthHandler
from model.SystemComposition import SystemComposition
from view.Application import Application


class AuthController(Controller):
    def __init__(self) -> None:
        self.auth_handler: AuthHandler = AuthHandler()

    def auth_control(self) -> None:
        pass

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        pass
