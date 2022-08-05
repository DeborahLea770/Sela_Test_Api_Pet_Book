from models.BaseObj import BaseObj
import re


class RegisterView(BaseObj):
    def __init__(self, userName: str, password: str):
        S_Char = ['$', '#', '@', '!', '*']
        if not isinstance(userName, str):
            raise TypeError("user name must be string")
        self._userName = userName
        if not isinstance(password, str):
            raise TypeError("password must be string")
        if len(password) < 8:
            raise ValueError("Make sure your password is at lest 8 letters")
        elif re.search('[a-z]', password) is None:
            raise ValueError("Make sure your password has a lowercase letter in it")
        elif re.search('[A-Z]', password) is None:
            raise ValueError("Make sure your password has a capital letter in it")
        elif re.search('[0-9]', password) is None:
            raise ValueError("Make sure your password has a number in it")
        elif not any(char in S_Char for char in password):
            raise ValueError("Your password must have at least 1 special character ($, #, @, !, *)")
        self._password = password

    @property
    def userName(self):
        """Gets the userName of this Model.  # noqa: E501
        :return: The userName of this Model.  # noqa: E501
        :rtype: str
        """
        return self._userName

    @userName.setter
    def userName(self, userName):
        """Sets the userName of this Model.
        :param userName: The username of this Model.  # noqa: E501
        :type: str
        """
        if userName is None:
            raise ValueError("Invalid value for `userName`, must not be `None`")  # noqa: E501
        if not isinstance(userName, str):
            raise TypeError("user name must be string!")
        self._userName = userName

    @property
    def password(self):
        """Gets the password of this Model.  # noqa: E501
        :return: The password of this Model.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this model.
        :param password: The password of this Model.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if not isinstance(password, str):
            raise TypeError("password must be string")
        self._password = password
