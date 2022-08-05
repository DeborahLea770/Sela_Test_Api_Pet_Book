from models.baseObj import baseObj
import datetime


class Order(baseObj):

    def __init__(self, id: int, petId: int, quantity=None, shipDate=None, status=None, complete=None):
        super().__init__()
        self._id = None
        self._petId = None
        self._quantity = None
        self._shipDate = None
        self._status = None
        self._complete = None
        if not str(id).isdigit():
            raise TypeError("order id must be a integer!")
        self._id = id
        if not str(petId).isdigit():
            raise TypeError("order pet_id must be a integer!")
        self._petId = petId
        if quantity is not None:
            if not str(quantity).isdigit():
                raise TypeError("order quantity must be a integer!")
            self._quantity = quantity
        if shipDate is not None:
            if not isinstance(shipDate, datetime.datetime):
                raise TypeError("order shipDate must be a datetime!")
            self._shipDate = shipDate
        if status is not None:
            if not isinstance(status, str):
                raise TypeError("status must be a string!")
            if not status == "placed" and not status == "approved" and not status == "delivered":
                raise ValueError("status must be one of: placed/approved/delivered")
            self._status = status
        if complete is not None:
            if not isinstance(complete, bool):
                raise TypeError("order complete must be a boolean!")
            self._complete = complete

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501
        :return: The id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, Id):
        """Sets the id of this Order.
        :param Id: The id of this Order.  # noqa: E501
        :type: int
        """
        if not str(id).isdigit():
            raise TypeError("order id must be a integer!")
        self._id = Id

    @property
    def pet_id(self):
        """Gets the petId of this Order.  # noqa: E501
        :return: The petId of this Order.  # noqa: E501
        :rtype: int
        """
        return self._petId

    @pet_id.setter
    def pet_id(self, petId):
        """Sets the petId of this Order.
        :param petId: The petId of this Order.  # noqa: E501
        :type: int
        """
        if not str(petId).isdigit():
            raise TypeError("order pet_id must be a integer!")
        self._petId = petId

    @property
    def quantity(self):
        """Gets the quantity of this Order.  # noqa: E501
        :return: The quantity of this Order.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Order.
        :param quantity: The quantity of this Order.  # noqa: E501
        :type: int
        """
        if not str(quantity).isdigit():
            raise TypeError("order quantity must be a integer!")
        self._quantity = quantity

    @property
    def shipDate(self):
        """Gets the shipDate of this Order.  # noqa: E501
        :return: The shipDate of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._shipDate

    @shipDate.setter
    def shipDate(self, shipDate):
        """Sets the shipDate of this Order.
        :param shipDate: The quantity of this Order.  # noqa: E501
        :type: datetime
        """
        if shipDate is None:
            raise ValueError("Invalid value for `shipDate`, must not be `None`")  # noqa: E501
        if not isinstance(shipDate, datetime.datetime):
            raise TypeError("order shipDate must be a datetime!")
        self._shipDate = shipDate

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501
        :return: The status of this Order.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.
        :param status: The quantity of this Order.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if not isinstance(status, str):
            raise TypeError("status must be a string!")
        if not status == "placed" and not status == "approved" and not status == "delivered":
            raise ValueError("status must be one of: placed/approved/delivered")
        self._status = status

    @property
    def complete(self):
        """Gets the complete of this Order.  # noqa: E501
        :return: The complete of this Order.  # noqa: E501
        :rtype: boolean
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this Order.
        :param complete: The quantity of this Order.  # noqa: E501
        :type: boolean
        """
        if complete is None:
            raise ValueError("Invalid value for `complete`, must not be `None`")  # noqa: E501
        if not isinstance(complete, bool):
            raise TypeError("order complete must be a boolean!")
        self._complete = complete


def main():
    o = Order(3242, 23457, 43534, datetime.datetime.now(), "approved", False)
    print(o.to_json())


if __name__ == '__main__':
    main()
