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

class OrderAddress(object):
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
        'full_address': 'str',
        'province': 'str',
        'area': 'str',
        'city': 'str',
        'street': 'str',
        'home': 'str',
        'flat': 'str',
        'entrance': 'str',
        'longitude': 'float',
        'latitude': 'float'
    }

    attribute_map = {
        'full_address': 'fullAddress',
        'province': 'province',
        'area': 'area',
        'city': 'city',
        'street': 'street',
        'home': 'home',
        'flat': 'flat',
        'entrance': 'entrance',
        'longitude': 'longitude',
        'latitude': 'latitude'
    }

    def __init__(self, full_address=None, province=None, area=None, city=None, street=None, home=None, flat=None, entrance=None, longitude=None, latitude=None):  # noqa: E501
        """OrderAddress - a model defined in Swagger"""  # noqa: E501
        self._full_address = None
        self._province = None
        self._area = None
        self._city = None
        self._street = None
        self._home = None
        self._flat = None
        self._entrance = None
        self._longitude = None
        self._latitude = None
        self.discriminator = None
        if full_address is not None:
            self.full_address = full_address
        if province is not None:
            self.province = province
        if area is not None:
            self.area = area
        if city is not None:
            self.city = city
        if street is not None:
            self.street = street
        if home is not None:
            self.home = home
        if flat is not None:
            self.flat = flat
        if entrance is not None:
            self.entrance = entrance
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude

    @property
    def full_address(self):
        """Gets the full_address of this OrderAddress.  # noqa: E501

        Adres dostavki.  # noqa: E501

        :return: The full_address of this OrderAddress.  # noqa: E501
        :rtype: str
        """
        return self._full_address

    @full_address.setter
    def full_address(self, full_address):
        """Sets the full_address of this OrderAddress.

        Adres dostavki.  # noqa: E501

        :param full_address: The full_address of this OrderAddress.  # noqa: E501
        :type: str
        """

        self._full_address = full_address

    @property
    def province(self):
        """Gets the province of this OrderAddress.  # noqa: E501

        Oblast  # noqa: E501

        :return: The province of this OrderAddress.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this OrderAddress.

        Oblast  # noqa: E501

        :param province: The province of this OrderAddress.  # noqa: E501
        :type: str
        """

        self._province = province

    @property
    def area(self):
        """Gets the area of this OrderAddress.  # noqa: E501

        Raion  # noqa: E501

        :return: The area of this OrderAddress.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this OrderAddress.

        Raion  # noqa: E501

        :param area: The area of this OrderAddress.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def city(self):
        """Gets the city of this OrderAddress.  # noqa: E501

        Gorod  # noqa: E501

        :return: The city of this OrderAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OrderAddress.

        Gorod  # noqa: E501

        :param city: The city of this OrderAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def street(self):
        """Gets the street of this OrderAddress.  # noqa: E501

        Ulica  # noqa: E501

        :return: The street of this OrderAddress.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this OrderAddress.

        Ulica  # noqa: E501

        :param street: The street of this OrderAddress.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def home(self):
        """Gets the home of this OrderAddress.  # noqa: E501

        Nomer doma  # noqa: E501

        :return: The home of this OrderAddress.  # noqa: E501
        :rtype: str
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this OrderAddress.

        Nomer doma  # noqa: E501

        :param home: The home of this OrderAddress.  # noqa: E501
        :type: str
        """

        self._home = home

    @property
    def flat(self):
        """Gets the flat of this OrderAddress.  # noqa: E501

        Nomer kvartiry  # noqa: E501

        :return: The flat of this OrderAddress.  # noqa: E501
        :rtype: str
        """
        return self._flat

    @flat.setter
    def flat(self, flat):
        """Sets the flat of this OrderAddress.

        Nomer kvartiry  # noqa: E501

        :param flat: The flat of this OrderAddress.  # noqa: E501
        :type: str
        """

        self._flat = flat

    @property
    def entrance(self):
        """Gets the entrance of this OrderAddress.  # noqa: E501

        Podezd  # noqa: E501

        :return: The entrance of this OrderAddress.  # noqa: E501
        :rtype: str
        """
        return self._entrance

    @entrance.setter
    def entrance(self, entrance):
        """Sets the entrance of this OrderAddress.

        Podezd  # noqa: E501

        :param entrance: The entrance of this OrderAddress.  # noqa: E501
        :type: str
        """

        self._entrance = entrance

    @property
    def longitude(self):
        """Gets the longitude of this OrderAddress.  # noqa: E501

        Koordinata dolgoty  # noqa: E501

        :return: The longitude of this OrderAddress.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this OrderAddress.

        Koordinata dolgoty  # noqa: E501

        :param longitude: The longitude of this OrderAddress.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this OrderAddress.  # noqa: E501

        Koordinaty hiroty  # noqa: E501

        :return: The latitude of this OrderAddress.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this OrderAddress.

        Koordinaty hiroty  # noqa: E501

        :param latitude: The latitude of this OrderAddress.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

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
        if issubclass(OrderAddress, dict):
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
        if not isinstance(other, OrderAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other