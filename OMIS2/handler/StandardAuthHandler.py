from model.User import User


class StandardAuthHandler:
    def __init__(self) -> None:
        pass

    def check_full_name_without_user(self, full_name: str) -> bool:
        pass

    def check_full_name_with_user(self, full_name: str, user: User) -> bool:
        pass

    def check_password_without_user(self, password: str) -> bool:
        pass

    def check_password_with_user(self, password: str, user: User) -> bool:
        pass
