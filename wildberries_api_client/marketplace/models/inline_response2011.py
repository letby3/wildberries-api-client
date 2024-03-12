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

class InlineResponse2011(object):
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
        'trbx_ids': 'list[str]'
    }

    attribute_map = {
        'trbx_ids': 'trbxIds'
    }

    def __init__(self, trbx_ids=None):  # noqa: E501
        """InlineResponse2011 - a model defined in Swagger"""  # noqa: E501
        self._trbx_ids = None
        self.discriminator = None
        if trbx_ids is not None:
            self.trbx_ids = trbx_ids

    @property
    def trbx_ids(self):
        """Gets the trbx_ids of this InlineResponse2011.  # noqa: E501

        Spisok ID korobov, kotorye byli sozdany.  # noqa: E501

        :return: The trbx_ids of this InlineResponse2011.  # noqa: E501
        :rtype: list[str]
        """
        return self._trbx_ids

    @trbx_ids.setter
    def trbx_ids(self, trbx_ids):
        """Sets the trbx_ids of this InlineResponse2011.

        Spisok ID korobov, kotorye byli sozdany.  # noqa: E501

        :param trbx_ids: The trbx_ids of this InlineResponse2011.  # noqa: E501
        :type: list[str]
        """

        self._trbx_ids = trbx_ids

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
        if issubclass(InlineResponse2011, dict):
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
        if not isinstance(other, InlineResponse2011):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
