from controller.Controller import Controller
from controller.ControllerFactory import ControllerFactory

from view.Application import Application

from model.SystemComposition import SystemComposition


class MainController(Controller):
    def __init__(self, application: Application) -> None:
        self.app: Application = application
        self.system_composition: SystemComposition = SystemComposition()

        controllers_factory: ControllerFactory = ControllerFactory()
        self.controllers: list[Controller] = controllers_factory.controllers_initialize(self.app, self.system_composition)

    def launch_program(self, application: Application, controllers: list[Controller], system_composition: SystemComposition) -> None:
        pass

    def control(self, application: Application, controllers: list[Controller], system_composition: SystemComposition) -> None:
        pass
