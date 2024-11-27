from model.User import User


class CommunicationManager:
    def __init__(self, sender: User, recipient: User) -> None:
        self.sender: User = sender
        self.recipient: User = recipient

    def send_message(self, message: str) -> None:
        pass

    def receive_message(self, message: str) -> None:
        pass
