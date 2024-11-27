from manager.CommunicationManager import CommunicationManager

from model.User import User
from model.Admin import Admin


class CourierCommunicationManager(CommunicationManager):
    def __init__(self, sender: User, recipient: Admin) -> None:
        super().__init__(sender, recipient)

    def send_message(self, message: str) -> None:
        pass

    def receive_message(self, message: str) -> None:
        pass
