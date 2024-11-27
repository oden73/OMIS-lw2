from view.Application import Application

from model.SystemComposition import SystemComposition

from controller.Controller import Controller


class StandardControllerFactory:
    def __init__(self):
        pass

    def controllers_initialize(self, application: Application, system_composition: SystemComposition) -> list[Controller]:
        pass
