from manager.StandardPackageManager import StandardPackageManager

from model.Package import Package


class PackageManager(StandardPackageManager):
    def __init__(self) -> None:
        super().__init__()

    def show_packages(self) -> None:
        pass
