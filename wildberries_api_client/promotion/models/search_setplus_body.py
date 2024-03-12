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

class SearchSetplusBody(object):
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
        'pluse': 'list[str]'
    }

    attribute_map = {
        'pluse': 'pluse'
    }

    def __init__(self, pluse=None):  # noqa: E501
        """SearchSetplusBody - a model defined in Swagger"""  # noqa: E501
        self._pluse = None
        self.discriminator = None
        if pluse is not None:
            self.pluse = pluse

    @property
    def pluse(self):
        """Gets the pluse of this SearchSetplusBody.  # noqa: E501

        Spisok fiksirovannyh fraz (max. 100)  # noqa: E501

        :return: The pluse of this SearchSetplusBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._pluse

    @pluse.setter
    def pluse(self, pluse):
        """Sets the pluse of this SearchSetplusBody.

        Spisok fiksirovannyh fraz (max. 100)  # noqa: E501

        :param pluse: The pluse of this SearchSetplusBody.  # noqa: E501
        :type: list[str]
        """

        self._pluse = pluse

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
        if issubclass(SearchSetplusBody, dict):
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
        if not isinstance(other, SearchSetplusBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
