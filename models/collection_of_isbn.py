from models.BaseObj import BaseObj


class CollectionOfIsbn(BaseObj):
    def __init__(self, isbn: str):
        self._isbn = None

        if isbn is not None:
            if not isinstance(isbn, str):
                raise TypeError("isbn must be string")
            self._isbn = isbn


