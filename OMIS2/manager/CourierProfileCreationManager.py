from manager.ProfileCreationManager import ProfileCreationManager

from model.Courier import Courier
from model.SystemComposition import SystemComposition


class CourierProfileCreationManager(ProfileCreationManager):
    def __init__(self) -> None:
        self.courier: Courier = Courier()

    def create_profile(self) -> None:
        pass

    def save_profile(self, system_composition: SystemComposition) -> None:
        pass
