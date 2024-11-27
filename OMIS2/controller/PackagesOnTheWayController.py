from controller.Controller import Controller

from manager.StandardPackageManager import StandardPackageManager
from manager.PackagesOnTheWayManager import PackagesOnTheWayManager
from model.SystemComposition import SystemComposition
from view.Application import Application


class PackagesOnTheWayController(Controller):
    def __init__(self):
        self.manager: StandardPackageManager = StandardPackageManager()

    def control_packages_on_the_way(self) -> None:
        pass

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        package_manager: PackagesOnTheWayManager = PackagesOnTheWayManager()
