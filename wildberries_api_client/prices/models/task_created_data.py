# coding: utf-8

"""
    API cen i skidok

    S pomohu etih metodov mohno ustanavlivat ceny i skidki. Maksimum — 10 zaprosov za 6 sekund summarno dla vseh metodov.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TaskCreatedData(object):
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
        'already_exists': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'already_exists': 'alreadyExists'
    }

    def __init__(self, id=None, already_exists=None):  # noqa: E501
        """TaskCreatedData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._already_exists = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if already_exists is not None:
            self.already_exists = already_exists

    @property
    def id(self):
        """Gets the id of this TaskCreatedData.  # noqa: E501

        ID zagruzki  # noqa: E501

        :return: The id of this TaskCreatedData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskCreatedData.

        ID zagruzki  # noqa: E501

        :param id: The id of this TaskCreatedData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def already_exists(self):
        """Gets the already_exists of this TaskCreatedData.  # noqa: E501

        Flag dublirovania zagruzki: `true` — takaa zagruzka uhe est   # noqa: E501

        :return: The already_exists of this TaskCreatedData.  # noqa: E501
        :rtype: bool
        """
        return self._already_exists

    @already_exists.setter
    def already_exists(self, already_exists):
        """Sets the already_exists of this TaskCreatedData.

        Flag dublirovania zagruzki: `true` — takaa zagruzka uhe est   # noqa: E501

        :param already_exists: The already_exists of this TaskCreatedData.  # noqa: E501
        :type: bool
        """

        self._already_exists = already_exists

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
        if issubclass(TaskCreatedData, dict):
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
        if not isinstance(other, TaskCreatedData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
