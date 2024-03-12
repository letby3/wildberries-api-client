# coding: utf-8

"""
    Opisanie API Statistiki

    S pomohu etih metodov mohno poluhit othety.   # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IncomesItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'income_id': 'int',
        'number': 'str',
        '_date': 'date',
        'last_change_date': 'datetime',
        'supplier_article': 'str',
        'tech_size': 'str',
        'barcode': 'str',
        'quantity': 'int',
        'total_price': 'float',
        'date_close': 'date',
        'warehouse_name': 'str',
        'nm_id': 'int',
        'status': 'str'
    }

    attribute_map = {
        'income_id': 'incomeId',
        'number': 'number',
        '_date': 'date',
        'last_change_date': 'lastChangeDate',
        'supplier_article': 'supplierArticle',
        'tech_size': 'techSize',
        'barcode': 'barcode',
        'quantity': 'quantity',
        'total_price': 'totalPrice',
        'date_close': 'dateClose',
        'warehouse_name': 'warehouseName',
        'nm_id': 'nmId',
        'status': 'status'
    }

    def __init__(self, income_id=None, number=None, _date=None, last_change_date=None, supplier_article=None, tech_size=None, barcode=None, quantity=None, total_price=None, date_close=None, warehouse_name=None, nm_id=None, status=None):  # noqa: E501
        """IncomesItem - a model defined in Swagger"""  # noqa: E501
        self._income_id = None
        self._number = None
        self.__date = None
        self._last_change_date = None
        self._supplier_article = None
        self._tech_size = None
        self._barcode = None
        self._quantity = None
        self._total_price = None
        self._date_close = None
        self._warehouse_name = None
        self._nm_id = None
        self._status = None
        self.discriminator = None
        if income_id is not None:
            self.income_id = income_id
        if number is not None:
            self.number = number
        if _date is not None:
            self._date = _date
        if last_change_date is not None:
            self.last_change_date = last_change_date
        if supplier_article is not None:
            self.supplier_article = supplier_article
        if tech_size is not None:
            self.tech_size = tech_size
        if barcode is not None:
            self.barcode = barcode
        if quantity is not None:
            self.quantity = quantity
        if total_price is not None:
            self.total_price = total_price
        if date_close is not None:
            self.date_close = date_close
        if warehouse_name is not None:
            self.warehouse_name = warehouse_name
        if nm_id is not None:
            self.nm_id = nm_id
        if status is not None:
            self.status = status

    @property
    def income_id(self):
        """Gets the income_id of this IncomesItem.  # noqa: E501

        Nomer postavki  # noqa: E501

        :return: The income_id of this IncomesItem.  # noqa: E501
        :rtype: int
        """
        return self._income_id

    @income_id.setter
    def income_id(self, income_id):
        """Sets the income_id of this IncomesItem.

        Nomer postavki  # noqa: E501

        :param income_id: The income_id of this IncomesItem.  # noqa: E501
        :type: int
        """

        self._income_id = income_id

    @property
    def number(self):
        """Gets the number of this IncomesItem.  # noqa: E501

        Nomer UPD  # noqa: E501

        :return: The number of this IncomesItem.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this IncomesItem.

        Nomer UPD  # noqa: E501

        :param number: The number of this IncomesItem.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def _date(self):
        """Gets the _date of this IncomesItem.  # noqa: E501

        Data postuplenia. Esli hasovoi poas ne ukazan, to beretsa Moskovskoe vrema UTC+3.  # noqa: E501

        :return: The _date of this IncomesItem.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this IncomesItem.

        Data postuplenia. Esli hasovoi poas ne ukazan, to beretsa Moskovskoe vrema UTC+3.  # noqa: E501

        :param _date: The _date of this IncomesItem.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def last_change_date(self):
        """Gets the last_change_date of this IncomesItem.  # noqa: E501

        Data i vrema obnovlenia informacii v servise. Eto pole sootvetstvuet parametru `dateFrom` v zaprose. Esli hasovoi poas ne ukazan, to beretsa Moskovskoe vrema UTC+3.  # noqa: E501

        :return: The last_change_date of this IncomesItem.  # noqa: E501
        :rtype: datetime
        """
        return self._last_change_date

    @last_change_date.setter
    def last_change_date(self, last_change_date):
        """Sets the last_change_date of this IncomesItem.

        Data i vrema obnovlenia informacii v servise. Eto pole sootvetstvuet parametru `dateFrom` v zaprose. Esli hasovoi poas ne ukazan, to beretsa Moskovskoe vrema UTC+3.  # noqa: E501

        :param last_change_date: The last_change_date of this IncomesItem.  # noqa: E501
        :type: datetime
        """

        self._last_change_date = last_change_date

    @property
    def supplier_article(self):
        """Gets the supplier_article of this IncomesItem.  # noqa: E501

        Artikul prodavca  # noqa: E501

        :return: The supplier_article of this IncomesItem.  # noqa: E501
        :rtype: str
        """
        return self._supplier_article

    @supplier_article.setter
    def supplier_article(self, supplier_article):
        """Sets the supplier_article of this IncomesItem.

        Artikul prodavca  # noqa: E501

        :param supplier_article: The supplier_article of this IncomesItem.  # noqa: E501
        :type: str
        """

        self._supplier_article = supplier_article

    @property
    def tech_size(self):
        """Gets the tech_size of this IncomesItem.  # noqa: E501

        Razmer tovara (primer S, M, L, XL, 42, 42-43)  # noqa: E501

        :return: The tech_size of this IncomesItem.  # noqa: E501
        :rtype: str
        """
        return self._tech_size

    @tech_size.setter
    def tech_size(self, tech_size):
        """Sets the tech_size of this IncomesItem.

        Razmer tovara (primer S, M, L, XL, 42, 42-43)  # noqa: E501

        :param tech_size: The tech_size of this IncomesItem.  # noqa: E501
        :type: str
        """

        self._tech_size = tech_size

    @property
    def barcode(self):
        """Gets the barcode of this IncomesItem.  # noqa: E501

        Bar-kod  # noqa: E501

        :return: The barcode of this IncomesItem.  # noqa: E501
        :rtype: str
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """Sets the barcode of this IncomesItem.

        Bar-kod  # noqa: E501

        :param barcode: The barcode of this IncomesItem.  # noqa: E501
        :type: str
        """

        self._barcode = barcode

    @property
    def quantity(self):
        """Gets the quantity of this IncomesItem.  # noqa: E501

        Kolihestvo  # noqa: E501

        :return: The quantity of this IncomesItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this IncomesItem.

        Kolihestvo  # noqa: E501

        :param quantity: The quantity of this IncomesItem.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def total_price(self):
        """Gets the total_price of this IncomesItem.  # noqa: E501

        cena iz UPD  # noqa: E501

        :return: The total_price of this IncomesItem.  # noqa: E501
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this IncomesItem.

        cena iz UPD  # noqa: E501

        :param total_price: The total_price of this IncomesItem.  # noqa: E501
        :type: float
        """

        self._total_price = total_price

    @property
    def date_close(self):
        """Gets the date_close of this IncomesItem.  # noqa: E501

        Data prinatia (zakrytia) v WB. Esli hasovoi poas ne ukazan, to beretsa Moskovskoe vrema UTC+3.  # noqa: E501

        :return: The date_close of this IncomesItem.  # noqa: E501
        :rtype: date
        """
        return self._date_close

    @date_close.setter
    def date_close(self, date_close):
        """Sets the date_close of this IncomesItem.

        Data prinatia (zakrytia) v WB. Esli hasovoi poas ne ukazan, to beretsa Moskovskoe vrema UTC+3.  # noqa: E501

        :param date_close: The date_close of this IncomesItem.  # noqa: E501
        :type: date
        """

        self._date_close = date_close

    @property
    def warehouse_name(self):
        """Gets the warehouse_name of this IncomesItem.  # noqa: E501

        Nazvanie sklada  # noqa: E501

        :return: The warehouse_name of this IncomesItem.  # noqa: E501
        :rtype: str
        """
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, warehouse_name):
        """Sets the warehouse_name of this IncomesItem.

        Nazvanie sklada  # noqa: E501

        :param warehouse_name: The warehouse_name of this IncomesItem.  # noqa: E501
        :type: str
        """

        self._warehouse_name = warehouse_name

    @property
    def nm_id(self):
        """Gets the nm_id of this IncomesItem.  # noqa: E501

        Artikul WB  # noqa: E501

        :return: The nm_id of this IncomesItem.  # noqa: E501
        :rtype: int
        """
        return self._nm_id

    @nm_id.setter
    def nm_id(self, nm_id):
        """Sets the nm_id of this IncomesItem.

        Artikul WB  # noqa: E501

        :param nm_id: The nm_id of this IncomesItem.  # noqa: E501
        :type: int
        """

        self._nm_id = nm_id

    @property
    def status(self):
        """Gets the status of this IncomesItem.  # noqa: E501

        Tekuhii status postavki  # noqa: E501

        :return: The status of this IncomesItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IncomesItem.

        Tekuhii status postavki  # noqa: E501

        :param status: The status of this IncomesItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["Prinato"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IncomesItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IncomesItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
