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

class InlineResponse20016(object):
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
        'title': 'str',
        'nm': 'int',
        'subject_id': 'int'
    }

    attribute_map = {
        'title': 'title',
        'nm': 'nm',
        'subject_id': 'subjectId'
    }

    def __init__(self, title=None, nm=None, subject_id=None):  # noqa: E501
        """InlineResponse20016 - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._nm = None
        self._subject_id = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if nm is not None:
            self.nm = nm
        if subject_id is not None:
            self.subject_id = subject_id

    @property
    def title(self):
        """Gets the title of this InlineResponse20016.  # noqa: E501

        Nazvanie tovara  # noqa: E501

        :return: The title of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineResponse20016.

        Nazvanie tovara  # noqa: E501

        :param title: The title of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def nm(self):
        """Gets the nm of this InlineResponse20016.  # noqa: E501

        Artikul Wildberries (`nmId`)  # noqa: E501

        :return: The nm of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._nm

    @nm.setter
    def nm(self, nm):
        """Sets the nm of this InlineResponse20016.

        Artikul Wildberries (`nmId`)  # noqa: E501

        :param nm: The nm of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._nm = nm

    @property
    def subject_id(self):
        """Gets the subject_id of this InlineResponse20016.  # noqa: E501

        ID predmeta  # noqa: E501

        :return: The subject_id of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this InlineResponse20016.

        ID predmeta  # noqa: E501

        :param subject_id: The subject_id of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._subject_id = subject_id

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
        if issubclass(InlineResponse20016, dict):
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
        if not isinstance(other, InlineResponse20016):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
