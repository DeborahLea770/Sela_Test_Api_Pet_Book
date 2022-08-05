from models.BaseObj import BaseObj


class GetUserResult(BaseObj):
    def __init__(self, user_id=None, user_name=None, books=None):
        self._user_id = None
        self._user_name = None
        self._books = None

        if user_id is not None:
            if not isinstance(user_id, str):
                raise TypeError("user id must be string")
            self._user_id = user_id

        if user_name is not None:
            if not isinstance(user_name, str):
                raise TypeError("user name must be string")
            self._user_name = user_name

        if books is not None:
            if not isinstance(books, list):
                raise TypeError("books must be list bookModel")
            self._books = books


if __name__ == "__main__":
    C = GetUserResult("fhiu", "fdh", ["hih", "hoih", "hkh"])
    print(C)
