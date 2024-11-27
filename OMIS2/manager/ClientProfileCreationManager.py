from manager.ProfileCreationManager import ProfileCreationManager

from model.Client import Client
from model.SystemComposition import SystemComposition


class ClientProfileCreationManager(ProfileCreationManager):
    def __init__(self) -> None:
        self.client: Client = Client()

    def create_profile(self) -> None:
        pass

    def save_profile(self, system_composition: SystemComposition) -> None:
        pass
