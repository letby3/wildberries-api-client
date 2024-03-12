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

class InlineResponse2008(object):
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
        'next': 'Next',
        'supplies': 'list[Supply]'
    }

    attribute_map = {
        'next': 'next',
        'supplies': 'supplies'
    }

    def __init__(self, next=None, supplies=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger"""  # noqa: E501
        self._next = None
        self._supplies = None
        self.discriminator = None
        if next is not None:
            self.next = next
        if supplies is not None:
            self.supplies = supplies

    @property
    def next(self):
        """Gets the next of this InlineResponse2008.  # noqa: E501


        :return: The next of this InlineResponse2008.  # noqa: E501
        :rtype: Next
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this InlineResponse2008.


        :param next: The next of this InlineResponse2008.  # noqa: E501
        :type: Next
        """

        self._next = next

    @property
    def supplies(self):
        """Gets the supplies of this InlineResponse2008.  # noqa: E501

        Spisok postavok  # noqa: E501

        :return: The supplies of this InlineResponse2008.  # noqa: E501
        :rtype: list[Supply]
        """
        return self._supplies

    @supplies.setter
    def supplies(self, supplies):
        """Sets the supplies of this InlineResponse2008.

        Spisok postavok  # noqa: E501

        :param supplies: The supplies of this InlineResponse2008.  # noqa: E501
        :type: list[Supply]
        """

        self._supplies = supplies

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
        if issubclass(InlineResponse2008, dict):
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
        if not isinstance(other, InlineResponse2008):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
