# coding: utf-8

"""
    Opisanie API Marketplace

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2005Stickers(object):
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
        'order_id': 'int',
        'part_a': 'int',
        'part_b': 'int',
        'barcode': 'str',
        'file': 'str'
    }

    attribute_map = {
        'order_id': 'orderId',
        'part_a': 'partA',
        'part_b': 'partB',
        'barcode': 'barcode',
        'file': 'file'
    }

    def __init__(self, order_id=None, part_a=None, part_b=None, barcode=None, file=None):  # noqa: E501
        """InlineResponse2005Stickers - a model defined in Swagger"""  # noqa: E501
        self._order_id = None
        self._part_a = None
        self._part_b = None
        self._barcode = None
        self._file = None
        self.discriminator = None
        if order_id is not None:
            self.order_id = order_id
        if part_a is not None:
            self.part_a = part_a
        if part_b is not None:
            self.part_b = part_b
        if barcode is not None:
            self.barcode = barcode
        if file is not None:
            self.file = file

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse2005Stickers.  # noqa: E501

        Identifikator sborohnogo zadania  # noqa: E501

        :return: The order_id of this InlineResponse2005Stickers.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse2005Stickers.

        Identifikator sborohnogo zadania  # noqa: E501

        :param order_id: The order_id of this InlineResponse2005Stickers.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def part_a(self):
        """Gets the part_a of this InlineResponse2005Stickers.  # noqa: E501

        Pervaa hast identifikatora etiketki (dla pehati podpisi)  # noqa: E501

        :return: The part_a of this InlineResponse2005Stickers.  # noqa: E501
        :rtype: int
        """
        return self._part_a

    @part_a.setter
    def part_a(self, part_a):
        """Sets the part_a of this InlineResponse2005Stickers.

        Pervaa hast identifikatora etiketki (dla pehati podpisi)  # noqa: E501

        :param part_a: The part_a of this InlineResponse2005Stickers.  # noqa: E501
        :type: int
        """

        self._part_a = part_a

    @property
    def part_b(self):
        """Gets the part_b of this InlineResponse2005Stickers.  # noqa: E501

        Vtoraa hast identifikatora etiketki  # noqa: E501

        :return: The part_b of this InlineResponse2005Stickers.  # noqa: E501
        :rtype: int
        """
        return self._part_b

    @part_b.setter
    def part_b(self, part_b):
        """Sets the part_b of this InlineResponse2005Stickers.

        Vtoraa hast identifikatora etiketki  # noqa: E501

        :param part_b: The part_b of this InlineResponse2005Stickers.  # noqa: E501
        :type: int
        """

        self._part_b = part_b

    @property
    def barcode(self):
        """Gets the barcode of this InlineResponse2005Stickers.  # noqa: E501

        Zakodirovannoe znahenie etiketki  # noqa: E501

        :return: The barcode of this InlineResponse2005Stickers.  # noqa: E501
        :rtype: str
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """Sets the barcode of this InlineResponse2005Stickers.

        Zakodirovannoe znahenie etiketki  # noqa: E501

        :param barcode: The barcode of this InlineResponse2005Stickers.  # noqa: E501
        :type: str
        """

        self._barcode = barcode

    @property
    def file(self):
        """Gets the file of this InlineResponse2005Stickers.  # noqa: E501

        Polnoe predstavlenie etiketki v zadannom formate. (kodirovka base64)  # noqa: E501

        :return: The file of this InlineResponse2005Stickers.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this InlineResponse2005Stickers.

        Polnoe predstavlenie etiketki v zadannom formate. (kodirovka base64)  # noqa: E501

        :param file: The file of this InlineResponse2005Stickers.  # noqa: E501
        :type: str
        """

        self._file = file

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
        if issubclass(InlineResponse2005Stickers, dict):
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
        if not isinstance(other, InlineResponse2005Stickers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other