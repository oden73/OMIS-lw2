from controller.Controller import Controller

from manager.StandardPackageManager import StandardPackageManager
from manager.PackageManager import PackageManager

from model.Package import Package
from model.SystemComposition import SystemComposition
from view.Application import Application


class PackageShowController(Controller):
    def __init__(self) -> None:
        self.packages: list[Package] = []
        self.manager: StandardPackageManager = StandardPackageManager()

    def control(self, application: Application, system_composition: SystemComposition) -> None:
        package_manager: PackageManager = PackageManager()
