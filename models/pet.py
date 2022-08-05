from models.baseObj import baseObj
from models.category import Category
from models.tags import Tags


class Pet(baseObj):

    def __init__(self, id: int, name: str, category=None, photoUrls=None, tags=None, status=None):
        super().__init__()
        self._id = None
        self._name = None
        self._category = None
        self._photoUrls = None
        self._tags = None
        self._status = None
        if not str(id).isdigit():
            raise TypeError("id must be a number!")
        self._id = id
        if not isinstance(name, str):
            raise TypeError("name must be a string!")
        self._name = name
        if category is not None:
            if not isinstance(category, Category) and not isinstance(category, dict):
                raise TypeError("category must be instance of Category or dict!")
            if isinstance(category, dict):
                category = Category(**category)
            # self._category = Category.to_json(category)
            self._category = category
        if photoUrls is not None:
            if not isinstance(photoUrls, list):
                raise TypeError("photoUrls must be a list of strings!")
            for photoUrl in photoUrls:
                if not isinstance(photoUrl, str):
                    raise TypeError("one or more of the urls is not a string!")
            self._photoUrls = photoUrls
        if tags is not None:
            if not isinstance(tags, list):
                raise TypeError("tags must be a list of Tags!")
            for tag in tags:
                if not isinstance(tag, Tags) and not isinstance(tag, dict):
                    raise TypeError("one or more of the tags is not instance of Tags or dict!")
                # Tags.to_json(tag)
                if isinstance(tag, dict):
                    tags = Tags(**tag)
            self._tags = tags
        if status is not None:
            if not isinstance(status, str):
                raise TypeError("status must be a string!")
            if not status == "available" and not status == "pending" and not status == "sold":
                raise ValueError("status must be one of: available/sold/pending")
            self._status = status

    @property
    def id(self):
        """Gets the id of this Pet.  # noqa: E501
        :return: The id of this Pet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, Id):
        """Sets the id of this Pet.
        :param id: The id of this Pet.  # noqa: E501
        :type: int
        """
        if not str(Id).isdigit():
            raise TypeError("id must be a number!")
        self._Id = Id

    @property
    def name(self):
        """Gets the name of this Pet.  # noqa: E501
        :return: The name of this Pet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pet.
        :param name: The name of this Pet.  # noqa: E501
        :type: str
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string!")
        self._name = name

    @property
    def category(self):
        """Gets the category of this Pet.  # noqa: E501
        :return: The category of this Pet.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Pet.
        :param category: The category of this Pet.  # noqa: E501
        :type: Category
        """
        if not isinstance(category, Category):
            raise TypeError("category must be instance of Category!")
        self._category = category

    @property
    def photoUrls(self):
        """Gets the photoUrls of this Pet.  # noqa: E501
        :return: The photoUrls of this Pet.  # noqa: E501
        :rtype: list of str
        """
        return self._photoUrls

    @photoUrls.setter
    def photoUrls(self, photoUrls):
        """Sets the photoUrls of this Pet.
        :param photoUrls: The photoUrls of this Pet.  # noqa: E501
        :type: list of str
        """
        if not isinstance(photoUrls, list):
            raise TypeError("photoUrls must be a list of strings!")
        for photoUrl in photoUrls:
            if not isinstance(photoUrl, str):
                raise TypeError("one or more of the urls is not a string!")
        self._photoUrls = photoUrls

    @property
    def tags(self) -> list:
        """Gets the tags of this Pet.  # noqa: E501
        :return: The tags of this Pet.  # noqa: E501
        :rtype: list
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Pet.
        :param tags: The tags of this Pet.  # noqa: E501
        :type: list
        """
        if not isinstance(tags, list):
            raise TypeError("tags must be a list of Tags!")
        for tag in tags:
            if not isinstance(tag, Tags):
                raise TypeError("one or more of the tags is not instance of Tags!")
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this Pet.  # noqa: E501
        :return: The status of this Pet.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Pet.
        :param status: The status of this Pet.  # noqa: E501
        :type: str
        """
        if not isinstance(status, str):
            raise TypeError("status must be a string!")
        if not status == "available" and not status == "pending" and not status == "sold":
            raise ValueError("status must be one of: available/sold/pending")
        self._status = status


def main():
    category = Category(345345, "tamirCat")
    T = Tags(345345, "tamirTag")
    P = Pet("343434", "tamir", category, ["ewrgtewrt", "EWrewr", "WDr ew"], [T], "pending")


if __name__ == '__main__':
    main()
