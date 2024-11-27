from model.Package import Package


class StandardPackageManager:
    def __init__(self) -> None:
        self.packages: list[Package] = []

    def show_packages(self) -> None:
        pass
