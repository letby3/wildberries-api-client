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

class TaskCreated(object):
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
        'data': 'TaskCreatedData',
        'error': 'bool',
        'error_text': 'str'
    }

    attribute_map = {
        'data': 'data',
        'error': 'error',
        'error_text': 'errorText'
    }

    def __init__(self, data=None, error=None, error_text=None):  # noqa: E501
        """TaskCreated - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._error = None
        self._error_text = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if error is not None:
            self.error = error
        if error_text is not None:
            self.error_text = error_text

    @property
    def data(self):
        """Gets the data of this TaskCreated.  # noqa: E501


        :return: The data of this TaskCreated.  # noqa: E501
        :rtype: TaskCreatedData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TaskCreated.


        :param data: The data of this TaskCreated.  # noqa: E501
        :type: TaskCreatedData
        """

        self._data = data

    @property
    def error(self):
        """Gets the error of this TaskCreated.  # noqa: E501

        Flag ohibki  # noqa: E501

        :return: The error of this TaskCreated.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TaskCreated.

        Flag ohibki  # noqa: E501

        :param error: The error of this TaskCreated.  # noqa: E501
        :type: bool
        """

        self._error = error

    @property
    def error_text(self):
        """Gets the error_text of this TaskCreated.  # noqa: E501

        Tekst ohibki  # noqa: E501

        :return: The error_text of this TaskCreated.  # noqa: E501
        :rtype: str
        """
        return self._error_text

    @error_text.setter
    def error_text(self, error_text):
        """Sets the error_text of this TaskCreated.

        Tekst ohibki  # noqa: E501

        :param error_text: The error_text of this TaskCreated.  # noqa: E501
        :type: str
        """

        self._error_text = error_text

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
        if issubclass(TaskCreated, dict):
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
        if not isinstance(other, TaskCreated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
