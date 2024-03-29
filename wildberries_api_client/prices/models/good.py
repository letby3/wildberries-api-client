# coding: utf-8

"""
    API cen i skidok

    S pomohu etih metodov mohno ustanavlivat ceny i skidki. Maksimum — 10 zaprosov za 6 sekund summarno dla vseh metodov.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Good(object):
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
        'nm_id': 'int',
        'price': 'int',
        'discount': 'int'
    }

    attribute_map = {
        'nm_id': 'nmID',
        'price': 'price',
        'discount': 'discount'
    }

    def __init__(self, nm_id=None, price=None, discount=None):  # noqa: E501
        """Good - a model defined in Swagger"""  # noqa: E501
        self._nm_id = None
        self._price = None
        self._discount = None
        self.discriminator = None
        self.nm_id = nm_id
        if price is not None:
            self.price = price
        if discount is not None:
            self.discount = discount

    @property
    def nm_id(self):
        """Gets the nm_id of this Good.  # noqa: E501

        Artikul Wildberries  # noqa: E501

        :return: The nm_id of this Good.  # noqa: E501
        :rtype: int
        """
        return self._nm_id

    @nm_id.setter
    def nm_id(self, nm_id):
        """Sets the nm_id of this Good.

        Artikul Wildberries  # noqa: E501

        :param nm_id: The nm_id of this Good.  # noqa: E501
        :type: int
        """
        if nm_id is None:
            raise ValueError("Invalid value for `nm_id`, must not be `None`")  # noqa: E501

        self._nm_id = nm_id

    @property
    def price(self):
        """Gets the price of this Good.  # noqa: E501

        cena. Valutu mohno poluhit s pomohu metoda [Poluhenie spiska tovarov po artikulam](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/get), pole `currencyIsoCode4217`   # noqa: E501

        :return: The price of this Good.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Good.

        cena. Valutu mohno poluhit s pomohu metoda [Poluhenie spiska tovarov po artikulam](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/get), pole `currencyIsoCode4217`   # noqa: E501

        :param price: The price of this Good.  # noqa: E501
        :type: int
        """

        self._price = price

    @property
    def discount(self):
        """Gets the discount of this Good.  # noqa: E501

        Skidka, %  # noqa: E501

        :return: The discount of this Good.  # noqa: E501
        :rtype: int
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this Good.

        Skidka, %  # noqa: E501

        :param discount: The discount of this Good.  # noqa: E501
        :type: int
        """

        self._discount = discount

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
        if issubclass(Good, dict):
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
        if not isinstance(other, Good):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
