# coding: utf-8

"""
    Opisanie API Voprosov i Otzyvov

    `Vahno!` Dopuskaetsa 1 zapros v sekundu na metody voprosov i otzyvov v celom. Pri prevyhenii limita do 3 zaprosov v sekundu posleduet blokirovka na 60 sekund.   # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrderReturnBody(object):
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
        'feedback_id': 'str'
    }

    attribute_map = {
        'feedback_id': 'feedbackId'
    }

    def __init__(self, feedback_id=None):  # noqa: E501
        """OrderReturnBody - a model defined in Swagger"""  # noqa: E501
        self._feedback_id = None
        self.discriminator = None
        if feedback_id is not None:
            self.feedback_id = feedback_id

    @property
    def feedback_id(self):
        """Gets the feedback_id of this OrderReturnBody.  # noqa: E501

        Identifikator otzyva  # noqa: E501

        :return: The feedback_id of this OrderReturnBody.  # noqa: E501
        :rtype: str
        """
        return self._feedback_id

    @feedback_id.setter
    def feedback_id(self, feedback_id):
        """Sets the feedback_id of this OrderReturnBody.

        Identifikator otzyva  # noqa: E501

        :param feedback_id: The feedback_id of this OrderReturnBody.  # noqa: E501
        :type: str
        """

        self._feedback_id = feedback_id

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
        if issubclass(OrderReturnBody, dict):
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
        if not isinstance(other, OrderReturnBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other