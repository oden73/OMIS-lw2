from manager.ProfileCreationManager import ProfileCreationManager

from model.Admin import Admin
from model.SystemComposition import SystemComposition


class AdminProfileCreationManager(ProfileCreationManager):
    def __init__(self) -> None:
        self.admin: Admin = Admin()

    def create_profile(self) -> None:
        pass

    def save_profile(self, system_composition: SystemComposition) -> None:
        pass
