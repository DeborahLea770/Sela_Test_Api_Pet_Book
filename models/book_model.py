from models.BaseObj import BaseObj
import datetime


class Book(BaseObj):
    def __init__(self, isbn: str, title: str, sum_title: str, author: str, publish_date: datetime, publisher: str,
                 pages: int, description: str, website: str):
        self._isbn = None
        self._title = None
        self._sum_title = None
        self._author = None
        self._publish_date = None
        self._publisher = None
        self._pages = None
        self._description = None
        self._website = None

        if not isinstance(isbn, str):
            raise TypeError("Book isbn must be a string!")
        self._isbn = isbn

        if not isinstance(title, str):
            raise TypeError("Book title must be a string!")
        self._title = title

        if not isinstance(sum_title, str):
            raise TypeError("Book sum_title must be a string!")
        self._sum_title = sum_title

        if not isinstance(author, str):
            raise TypeError("Book author must be a string!")
        self._author = author

        if not isinstance(publish_date, datetime.datetime):
            raise TypeError("Book publish date must be a Date!")
        self._publish_date = publish_date

        if not isinstance(publisher, str):
            raise TypeError("Book publisher must be a string!")
        self._publisher = publisher

        if not isinstance(pages, int):
            raise TypeError("Book pages must be a integer!")
        self._pages = pages

        if not isinstance(description, str):
            raise TypeError("Book description must be a string!")
        self._description = description

        if not isinstance(website, str):
            raise TypeError("Book website must be a string!")
        self._website = website
