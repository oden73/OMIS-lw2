from handler.StandardAuthHandler import StandardAuthHandler
from model.User import User


class AuthHandler(StandardAuthHandler):
    def check_full_name_with_user(self, full_name: str, user: User) -> bool:
        pass

    def check_password_with_user(self, password: str, user: User) -> bool:
        pass
