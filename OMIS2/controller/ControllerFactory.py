from controller.Controller import Controller
from controller.StandardControllerFactory import StandardControllerFactory
from model.SystemComposition import SystemComposition
from view.Application import Application


class ControllerFactory(StandardControllerFactory):
    def controllers_initialize(self, application: Application, system_composition: SystemComposition) -> list[Controller]:
        pass
