from models.baseObj import baseObj


class User(baseObj):

    def __init__(self, id: int, username: str, password: str, firstName=None, lastName=None, email=None, phone=None,
                 userStatus=None):
        super().__init__()
        self._id = None
        self._username = None
        self._password = None
        self._firstName = None
        self._lastName = None
        self._email = None
        self._phone = None
        self._userStatus = None
        if not str(id).isdigit():
            raise TypeError("user id must be a integer!")
        self._id = id

        if not isinstance(username, str):
            raise TypeError("user name must be string!")
        self._username = username

        if not isinstance(password, str):
            raise TypeError("password must be string")
        self._password = password
        if firstName is not None:
            if not isinstance(firstName, str):
                raise TypeError("first name must be string!")
            self._firstName = firstName

        if lastName is not None:
            if not isinstance(lastName, str):
                raise TypeError("last name must be string!")
            self._lastName = lastName

        if email is not None:
            if not isinstance(email, str):
                raise TypeError("email must be string!")
            self._email = email

        if phone is not None:
            if not str(phone).isdigit():
                raise TypeError("phone must be integer!")
            self._phone = phone

        if userStatus is not None:
            if not str(userStatus).isdigit():
                raise TypeError("user status name must be a integer")
            self._userStatus = userStatus

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501
        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, Id):
        """Sets the id of this User.
        :param id: The id of this User.  # noqa: E501
        :type: int
        """
        if not str(Id).isdigit():
            raise TypeError("user id must be a integer!")
        self._id = Id

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501
        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the name of this User.
        :param username: The username of this User.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501
        if not isinstance(username, str):
            raise TypeError("user name must be string!")
        self._username = username

    @property
    def password(self):
        """Gets the password of this User.  # noqa: E501
        :return: The password of this User.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.
        :param password: The password of this User.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if not isinstance(password, str):
            raise TypeError("password must be string")
        self._password = password

    @property
    def firstName(self):
        """Gets the firstName of this User.  # noqa: E501
        :return: The firstName of this User.  # noqa: E501
        :rtype: str
        """
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        """Sets the firstName of this User.
        :param firstName: The firstName of this User.  # noqa: E501
        :type: str
        """
        if firstName is None:
            raise ValueError("Invalid value for `firstName`, must not be `None`")  # noqa: E501
        if not isinstance(firstName, str):
            raise TypeError("first name must be string!")
        self._firstName = firstName

    @property
    def lastName(self):
        """Gets the lastName of this User.  # noqa: E501
        :return: The lastName of this User.  # noqa: E501
        :rtype: str
        """
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        """Sets the lastName of this User.
        :param lastName: The lastName of this User.  # noqa: E501
        :type: str
        """
        if lastName is None:
            raise ValueError("Invalid value for `lastName`, must not be `None`")  # noqa: E501
        if not isinstance(lastName, str):
            raise TypeError("last name must be string!")
        self._lastName = lastName

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501
        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.
        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if not isinstance(email, str):
            raise TypeError("email must be string!")
        self._email = email

    @property
    def phone(self):
        """Gets the phone of this User.  # noqa: E501
        :return: The phone of this User.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this User.
        :param phone: The phone of this User.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501
        if not str(phone).isdigit():
            raise TypeError("phone must be integer!")
        self._phone = phone

    @property
    def userStatus(self):
        """Gets the userStatus of this User.  # noqa: E501
        :return: The userStatus of this User.  # noqa: E501
        :rtype: str
        """
        return self._userStatus

    @userStatus.setter
    def userStatus(self, userStatus):
        """Sets the userStatus of this User.
        :param userStatus: The userStatus of this User.  # noqa: E501
        :type: str
        """
        if userStatus is None:
            raise ValueError("Invalid value for `userStatus`, must not be `None`")  # noqa: E501
        if not str(userStatus).isdigit():
            raise TypeError("user status name must be a integer")
        self._userStatus = userStatus


def main():
    u = User("12232", "43143", "4r5345c", "omer", "mazor", "omermazor144@gmail.com", 207976903, 5)
    print(u)

if __name__ == '__main__':
    main()
