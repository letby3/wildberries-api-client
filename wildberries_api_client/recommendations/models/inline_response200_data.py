# coding: utf-8

"""
    Opisanie API Rekomendacii

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse200Data(object):
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
        'nm': 'int',
        'list': 'list[int]'
    }

    attribute_map = {
        'nm': 'nm',
        'list': 'list'
    }

    def __init__(self, nm=None, list=None):  # noqa: E501
        """InlineResponse200Data - a model defined in Swagger"""  # noqa: E501
        self._nm = None
        self._list = None
        self.discriminator = None
        if nm is not None:
            self.nm = nm
        if list is not None:
            self.list = list

    @property
    def nm(self):
        """Gets the nm of this InlineResponse200Data.  # noqa: E501

        Artikul WB, po kotoromu zaproheny rekomendacii.  # noqa: E501

        :return: The nm of this InlineResponse200Data.  # noqa: E501
        :rtype: int
        """
        return self._nm

    @nm.setter
    def nm(self, nm):
        """Sets the nm of this InlineResponse200Data.

        Artikul WB, po kotoromu zaproheny rekomendacii.  # noqa: E501

        :param nm: The nm of this InlineResponse200Data.  # noqa: E501
        :type: int
        """

        self._nm = nm

    @property
    def list(self):
        """Gets the list of this InlineResponse200Data.  # noqa: E501

        Spisok rekomendacii  # noqa: E501

        :return: The list of this InlineResponse200Data.  # noqa: E501
        :rtype: list[int]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this InlineResponse200Data.

        Spisok rekomendacii  # noqa: E501

        :param list: The list of this InlineResponse200Data.  # noqa: E501
        :type: list[int]
        """

        self._list = list

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
        if issubclass(InlineResponse200Data, dict):
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
        if not isinstance(other, InlineResponse200Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
