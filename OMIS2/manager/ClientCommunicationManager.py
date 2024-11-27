from manager.CommunicationManager import CommunicationManager

from model.User import User
from model.Client import Client


class ClientCommunicationManager(CommunicationManager):
    def __init__(self, sender: User, recipient: Client) -> None:
        super().__init__(sender, recipient)

    def send_message(self, message: str) -> None:
        pass

    def receive_message(self, message: str) -> None:
        pass
