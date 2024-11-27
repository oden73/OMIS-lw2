from controller.Controller import Controller
from manager.CourierProfileCreationManager import CourierProfileCreationManager

from model.SystemComposition import SystemComposition
from view.Application import Application




class CourierProfileShowController(Controller):
    def __init__(self) -> None:
        pass

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        manager: CourierProfileCreationManager = CourierProfileCreationManager()
