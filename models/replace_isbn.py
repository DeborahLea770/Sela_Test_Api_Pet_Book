from models.BaseObj import BaseObj


class ReplaceIsbn(BaseObj):
    def __init__(self, user_id: str, isbn: str):
        self._userId = None
        self._isbn = None

        if user_id is not None:
            if not isinstance(user_id, str):
                raise TypeError("user id must be string")
            self._userId = user_id

        if isbn is not None:
            if not isinstance(isbn, str):
                raise TypeError("isbn must be string")
            self._isbn = isbn

    @property
    def isbn(self):
        """Gets the isbn of this Model.  # noqa: E501
        :return: The isbn of this Model.  # noqa: E501
        :rtype: str
        """
        return self._isbn


if __name__ == "__main__":
    C = ReplaceIsbn("fhiu", "isbn")
    print(C)
