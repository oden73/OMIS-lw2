from manager.CommunicationManager import CommunicationManager

from model.User import User
from model.Courier import Courier


class CourierCommunicationManager(CommunicationManager):
    def __init__(self, sender: User, recipient: Courier) -> None:
        super().__init__(sender, recipient)

    def send_message(self, message: str) -> None:
        pass

    def receive_message(self, message: str) -> None:
        pass
