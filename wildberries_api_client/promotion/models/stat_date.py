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

class StatDate(object):
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
        'dates': 'list[date]',
        'stats': 'list[StatsBlok2]'
    }

    attribute_map = {
        'dates': 'dates',
        'stats': 'stats'
    }

    def __init__(self, dates=None, stats=None):  # noqa: E501
        """StatDate - a model defined in Swagger"""  # noqa: E501
        self._dates = None
        self._stats = None
        self.discriminator = None
        if dates is not None:
            self.dates = dates
        if stats is not None:
            self.stats = stats

    @property
    def dates(self):
        """Gets the dates of this StatDate.  # noqa: E501

        Daty, za kotorye neobhodimo vydat informaciu.  # noqa: E501

        :return: The dates of this StatDate.  # noqa: E501
        :rtype: list[date]
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this StatDate.

        Daty, za kotorye neobhodimo vydat informaciu.  # noqa: E501

        :param dates: The dates of this StatDate.  # noqa: E501
        :type: list[date]
        """

        self._dates = dates

    @property
    def stats(self):
        """Gets the stats of this StatDate.  # noqa: E501

        Blok statistiki  # noqa: E501

        :return: The stats of this StatDate.  # noqa: E501
        :rtype: list[StatsBlok2]
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this StatDate.

        Blok statistiki  # noqa: E501

        :param stats: The stats of this StatDate.  # noqa: E501
        :type: list[StatsBlok2]
        """

        self._stats = stats

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
        if issubclass(StatDate, dict):
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
        if not isinstance(other, StatDate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
