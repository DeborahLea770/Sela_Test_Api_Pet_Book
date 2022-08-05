from models.BaseObj import BaseObj


class LoginViewModel(BaseObj):
    def __init__(self, user_name: str, password: str):

        if not isinstance(user_name, str):
            raise TypeError("user name must be string")
        self._user_name = user_name
        if not isinstance(password, str):
            raise TypeError("password must be string")
        self._password = password


if __name__ == "__main__":
    L = LoginViewModel("aa", "3241")
    print(L)
