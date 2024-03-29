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

class InlineResponse20026(object):
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
        'id': 'int',
        'name': 'str',
        'nms_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'nms_count': 'nmsCount'
    }

    def __init__(self, id=None, name=None, nms_count=None):  # noqa: E501
        """InlineResponse20026 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._nms_count = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if nms_count is not None:
            self.nms_count = nms_count

    @property
    def id(self):
        """Gets the id of this InlineResponse20026.  # noqa: E501

        Identifikator predmeta  # noqa: E501

        :return: The id of this InlineResponse20026.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20026.

        Identifikator predmeta  # noqa: E501

        :param id: The id of this InlineResponse20026.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20026.  # noqa: E501

        Nazvanie predmeta  # noqa: E501

        :return: The name of this InlineResponse20026.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20026.

        Nazvanie predmeta  # noqa: E501

        :param name: The name of this InlineResponse20026.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nms_count(self):
        """Gets the nms_count of this InlineResponse20026.  # noqa: E501

        Kolihestvo artikulov WB s etim predmetom  # noqa: E501

        :return: The nms_count of this InlineResponse20026.  # noqa: E501
        :rtype: int
        """
        return self._nms_count

    @nms_count.setter
    def nms_count(self, nms_count):
        """Sets the nms_count of this InlineResponse20026.

        Kolihestvo artikulov WB s etim predmetom  # noqa: E501

        :param nms_count: The nms_count of this InlineResponse20026.  # noqa: E501
        :type: int
        """

        self._nms_count = nms_count

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
        if issubclass(InlineResponse20026, dict):
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
        if not isinstance(other, InlineResponse20026):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
