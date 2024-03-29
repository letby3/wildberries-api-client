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

class AutoUpdatenmBody(object):
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
        'add': 'list[int]',
        'delete': 'list[int]'
    }

    attribute_map = {
        'add': 'add',
        'delete': 'delete'
    }

    def __init__(self, add=None, delete=None):  # noqa: E501
        """AutoUpdatenmBody - a model defined in Swagger"""  # noqa: E501
        self._add = None
        self._delete = None
        self.discriminator = None
        if add is not None:
            self.add = add
        if delete is not None:
            self.delete = delete

    @property
    def add(self):
        """Gets the add of this AutoUpdatenmBody.  # noqa: E501

        Nomenklatury, kotorye neobhodimo dobavit.  # noqa: E501

        :return: The add of this AutoUpdatenmBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._add

    @add.setter
    def add(self, add):
        """Sets the add of this AutoUpdatenmBody.

        Nomenklatury, kotorye neobhodimo dobavit.  # noqa: E501

        :param add: The add of this AutoUpdatenmBody.  # noqa: E501
        :type: list[int]
        """

        self._add = add

    @property
    def delete(self):
        """Gets the delete of this AutoUpdatenmBody.  # noqa: E501

        Nomenklatury, kotorye neobhodimo udalit.  # noqa: E501

        :return: The delete of this AutoUpdatenmBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this AutoUpdatenmBody.

        Nomenklatury, kotorye neobhodimo udalit.  # noqa: E501

        :param delete: The delete of this AutoUpdatenmBody.  # noqa: E501
        :type: list[int]
        """

        self._delete = delete

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
        if issubclass(AutoUpdatenmBody, dict):
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
        if not isinstance(other, AutoUpdatenmBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
