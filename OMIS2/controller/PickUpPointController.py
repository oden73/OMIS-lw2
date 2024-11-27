from controller.Controller import Controller

from manager.StandardPickUpPointManager import StandardPickUpPointManager
from manager.PickUpPointManager import PickUpPointManager

from model.PickUpPoint import PickUpPoint
from model.SystemComposition import SystemComposition
from view.Application import Application


class PickUpPointController(Controller):
    def __init__(self) -> None:
        self.pick_up_point: PickUpPoint = PickUpPoint()
        self.manager: StandardPickUpPointManager = StandardPickUpPointManager([], {})

    def pick_up_point_control(self) -> None:
        pass

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        pick_up_point_manager: PickUpPointManager = PickUpPointManager({})
