# coding: utf-8
from models.baseObj import baseObj


class Tags(baseObj):

    def __init__(self, id=None, name=None):
        super().__init__()
        if id is not None:
            if not str(id).isdigit():
                raise TypeError("id must be a number!")
            self._id = id
        if name is not None:
            if not isinstance(name, str):
                raise TypeError("name must be a string!")
            self._name = name

    @property
    def id(self):
        """Gets the id of this Tags.  # noqa: E501
        :return: The id of this Tags.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, Id):
        """Sets the id of this Tags.
        :param id: The id of this Tags.  # noqa: E501
        :type: int
        """
        if not str(Id).isdigit():
            raise TypeError("id must be a number!")
        self._id = Id

    @property
    def name(self):
        """Gets the name of this Tags.  # noqa: E501
        :return: The name of this Tags.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tags.
        :param name: The name of this Tags.  # noqa: E501
        :type: str
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string!")
        self._name = name
