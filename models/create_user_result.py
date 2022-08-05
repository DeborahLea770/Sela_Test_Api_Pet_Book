from models.BaseObj import BaseObj


class CreateUserResult(BaseObj):
    def __init__(self, userId=None, username=None, books=None):
        self._userId = None
        self._username = None
        self._books = None

        if userId is not None:
            if not isinstance(userId, str):
                raise TypeError("userId must be string")
            self._userId = userId

        if username is not None:
            if not isinstance(username, str):
                raise TypeError("user name must be string")
            self._username = username

        if books is not None:
            if not isinstance(books, list):
                raise TypeError("books must be list of a list")
            self._books = books




if __name__ == "__main__":
    C = CreateUserResult("fhiu", "fdh", ["hih", "hoih", "hkh"])
    print(C)
