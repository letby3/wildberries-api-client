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

class InlineResponse2007Stickers(object):
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
        'url': 'str'
    }

    attribute_map = {
        'order_id': 'orderID',
        'url': 'url'
    }

    def __init__(self, order_id=None, url=None):  # noqa: E501
        """InlineResponse2007Stickers - a model defined in Swagger"""  # noqa: E501
        self._order_id = None
        self._url = None
        self.discriminator = None
        if order_id is not None:
            self.order_id = order_id
        if url is not None:
            self.url = url

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse2007Stickers.  # noqa: E501

        Identifikator sborohnogo zadania  # noqa: E501

        :return: The order_id of this InlineResponse2007Stickers.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse2007Stickers.

        Identifikator sborohnogo zadania  # noqa: E501

        :param order_id: The order_id of this InlineResponse2007Stickers.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def url(self):
        """Gets the url of this InlineResponse2007Stickers.  # noqa: E501

        Ssylka, po kotoroi mohno poluhit etiketku dla sborohnogo zadania  # noqa: E501

        :return: The url of this InlineResponse2007Stickers.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse2007Stickers.

        Ssylka, po kotoroi mohno poluhit etiketku dla sborohnogo zadania  # noqa: E501

        :param url: The url of this InlineResponse2007Stickers.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(InlineResponse2007Stickers, dict):
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
        if not isinstance(other, InlineResponse2007Stickers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
