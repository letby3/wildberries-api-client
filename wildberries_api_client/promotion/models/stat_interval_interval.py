# coding: utf-8

"""
    Opisanie API Prodvihenie

    Sinhronizacia dannyh iz bd proishodit raz v 3 minuty.  <br>Izmenenie statusa proishodit raz v 1 minutu. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu statusa. <br>Izmenenie stavki proishodit raz v 30 sekund. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu stavki.   # noqa: E501

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StatIntervalInterval(object):
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
        'begin': 'date',
        'end': 'date'
    }

    attribute_map = {
        'begin': 'begin',
        'end': 'end'
    }

    def __init__(self, begin=None, end=None):  # noqa: E501
        """StatIntervalInterval - a model defined in Swagger"""  # noqa: E501
        self._begin = None
        self._end = None
        self.discriminator = None
        if begin is not None:
            self.begin = begin
        if end is not None:
            self.end = end

    @property
    def begin(self):
        """Gets the begin of this StatIntervalInterval.  # noqa: E501

        Nahalo zaprahivaemogo perioda  # noqa: E501

        :return: The begin of this StatIntervalInterval.  # noqa: E501
        :rtype: date
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this StatIntervalInterval.

        Nahalo zaprahivaemogo perioda  # noqa: E501

        :param begin: The begin of this StatIntervalInterval.  # noqa: E501
        :type: date
        """

        self._begin = begin

    @property
    def end(self):
        """Gets the end of this StatIntervalInterval.  # noqa: E501

        Konec zaprahivaemogo perioda  # noqa: E501

        :return: The end of this StatIntervalInterval.  # noqa: E501
        :rtype: date
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this StatIntervalInterval.

        Konec zaprahivaemogo perioda  # noqa: E501

        :param end: The end of this StatIntervalInterval.  # noqa: E501
        :type: date
        """

        self._end = end

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
        if issubclass(StatIntervalInterval, dict):
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
        if not isinstance(other, StatIntervalInterval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
