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

class InlineResponse2004(object):
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
        'price': 'float',
        'discount': 'int',
        'promo_code': 'float'
    }

    attribute_map = {
        'nm_id': 'nmId',
        'price': 'price',
        'discount': 'discount',
        'promo_code': 'promoCode'
    }

    def __init__(self, nm_id=None, price=None, discount=None, promo_code=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger"""  # noqa: E501
        self._nm_id = None
        self._price = None
        self._discount = None
        self._promo_code = None
        self.discriminator = None
        if nm_id is not None:
            self.nm_id = nm_id
        if price is not None:
            self.price = price
        if discount is not None:
            self.discount = discount
        if promo_code is not None:
            self.promo_code = promo_code

    @property
    def nm_id(self):
        """Gets the nm_id of this InlineResponse2004.  # noqa: E501

        Artikul WB  # noqa: E501

        :return: The nm_id of this InlineResponse2004.  # noqa: E501
        :rtype: int
        """
        return self._nm_id

    @nm_id.setter
    def nm_id(self, nm_id):
        """Sets the nm_id of this InlineResponse2004.

        Artikul WB  # noqa: E501

        :param nm_id: The nm_id of this InlineResponse2004.  # noqa: E501
        :type: int
        """

        self._nm_id = nm_id

    @property
    def price(self):
        """Gets the price of this InlineResponse2004.  # noqa: E501

        cena  # noqa: E501

        :return: The price of this InlineResponse2004.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InlineResponse2004.

        cena  # noqa: E501

        :param price: The price of this InlineResponse2004.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def discount(self):
        """Gets the discount of this InlineResponse2004.  # noqa: E501

        Skidka  # noqa: E501

        :return: The discount of this InlineResponse2004.  # noqa: E501
        :rtype: int
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this InlineResponse2004.

        Skidka  # noqa: E501

        :param discount: The discount of this InlineResponse2004.  # noqa: E501
        :type: int
        """

        self._discount = discount

    @property
    def promo_code(self):
        """Gets the promo_code of this InlineResponse2004.  # noqa: E501

        Promokod  # noqa: E501

        :return: The promo_code of this InlineResponse2004.  # noqa: E501
        :rtype: float
        """
        return self._promo_code

    @promo_code.setter
    def promo_code(self, promo_code):
        """Sets the promo_code of this InlineResponse2004.

        Promokod  # noqa: E501

        :param promo_code: The promo_code of this InlineResponse2004.  # noqa: E501
        :type: float
        """

        self._promo_code = promo_code

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
        if issubclass(InlineResponse2004, dict):
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
        if not isinstance(other, InlineResponse2004):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other