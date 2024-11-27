from manager.StandardPickUpPointManager import StandardPickUpPointManager


class PickUpPointManager(StandardPickUpPointManager):
    def __init__(self, packages: dict) -> None:
        super().__init__([], packages)

    def take_package(self) -> None:
        pass

    def deliver_package(self) -> None:
        pass
    