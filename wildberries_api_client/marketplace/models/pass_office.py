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

class PassOffice(object):
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
        'name': 'str',
        'address': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'id': 'id'
    }

    def __init__(self, name=None, address=None, id=None):  # noqa: E501
        """PassOffice - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._address = None
        self._id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this PassOffice.  # noqa: E501

        Nazvanie  # noqa: E501

        :return: The name of this PassOffice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PassOffice.

        Nazvanie  # noqa: E501

        :param name: The name of this PassOffice.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this PassOffice.  # noqa: E501

        Adres  # noqa: E501

        :return: The address of this PassOffice.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PassOffice.

        Adres  # noqa: E501

        :param address: The address of this PassOffice.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def id(self):
        """Gets the id of this PassOffice.  # noqa: E501

        ID  # noqa: E501

        :return: The id of this PassOffice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PassOffice.

        ID  # noqa: E501

        :param id: The id of this PassOffice.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(PassOffice, dict):
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
        if not isinstance(other, PassOffice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
