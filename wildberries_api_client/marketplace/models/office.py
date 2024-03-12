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

class Office(object):
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
        'address': 'str',
        'name': 'str',
        'city': 'str',
        'id': 'int',
        'longitude': 'float',
        'latitude': 'float',
        'selected': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'name': 'name',
        'city': 'city',
        'id': 'id',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'selected': 'selected'
    }

    def __init__(self, address=None, name=None, city=None, id=None, longitude=None, latitude=None, selected=None):  # noqa: E501
        """Office - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._name = None
        self._city = None
        self._id = None
        self._longitude = None
        self._latitude = None
        self._selected = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if name is not None:
            self.name = name
        if city is not None:
            self.city = city
        if id is not None:
            self.id = id
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude
        if selected is not None:
            self.selected = selected

    @property
    def address(self):
        """Gets the address of this Office.  # noqa: E501

        Adres  # noqa: E501

        :return: The address of this Office.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Office.

        Adres  # noqa: E501

        :param address: The address of this Office.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def name(self):
        """Gets the name of this Office.  # noqa: E501

        Nazvanie  # noqa: E501

        :return: The name of this Office.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Office.

        Nazvanie  # noqa: E501

        :param name: The name of this Office.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def city(self):
        """Gets the city of this Office.  # noqa: E501

        Gorod  # noqa: E501

        :return: The city of this Office.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Office.

        Gorod  # noqa: E501

        :param city: The city of this Office.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def id(self):
        """Gets the id of this Office.  # noqa: E501

        ID  # noqa: E501

        :return: The id of this Office.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Office.

        ID  # noqa: E501

        :param id: The id of this Office.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def longitude(self):
        """Gets the longitude of this Office.  # noqa: E501

        Dolgota  # noqa: E501

        :return: The longitude of this Office.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Office.

        Dolgota  # noqa: E501

        :param longitude: The longitude of this Office.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this Office.  # noqa: E501

        hirota  # noqa: E501

        :return: The latitude of this Office.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Office.

        hirota  # noqa: E501

        :param latitude: The latitude of this Office.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def selected(self):
        """Gets the selected of this Office.  # noqa: E501

        Priznak togo, hto sklad uhe vybran prodavcom  # noqa: E501

        :return: The selected of this Office.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this Office.

        Priznak togo, hto sklad uhe vybran prodavcom  # noqa: E501

        :param selected: The selected of this Office.  # noqa: E501
        :type: bool
        """

        self._selected = selected

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
        if issubclass(Office, dict):
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
        if not isinstance(other, Office):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other