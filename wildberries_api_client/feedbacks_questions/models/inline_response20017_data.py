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

class InlineResponse20017Data(object):
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
        'valuation': 'str',
        'feedbacks_count': 'int'
    }

    attribute_map = {
        'valuation': 'valuation',
        'feedbacks_count': 'feedbacksCount'
    }

    def __init__(self, valuation=None, feedbacks_count=None):  # noqa: E501
        """InlineResponse20017Data - a model defined in Swagger"""  # noqa: E501
        self._valuation = None
        self._feedbacks_count = None
        self.discriminator = None
        if valuation is not None:
            self.valuation = valuation
        if feedbacks_count is not None:
            self.feedbacks_count = feedbacks_count

    @property
    def valuation(self):
        """Gets the valuation of this InlineResponse20017Data.  # noqa: E501

        Srednaa ocenka tovara  # noqa: E501

        :return: The valuation of this InlineResponse20017Data.  # noqa: E501
        :rtype: str
        """
        return self._valuation

    @valuation.setter
    def valuation(self, valuation):
        """Sets the valuation of this InlineResponse20017Data.

        Srednaa ocenka tovara  # noqa: E501

        :param valuation: The valuation of this InlineResponse20017Data.  # noqa: E501
        :type: str
        """

        self._valuation = valuation

    @property
    def feedbacks_count(self):
        """Gets the feedbacks_count of this InlineResponse20017Data.  # noqa: E501

        Kolihestvo otzyvov na dannyi tovar  # noqa: E501

        :return: The feedbacks_count of this InlineResponse20017Data.  # noqa: E501
        :rtype: int
        """
        return self._feedbacks_count

    @feedbacks_count.setter
    def feedbacks_count(self, feedbacks_count):
        """Sets the feedbacks_count of this InlineResponse20017Data.

        Kolihestvo otzyvov na dannyi tovar  # noqa: E501

        :param feedbacks_count: The feedbacks_count of this InlineResponse20017Data.  # noqa: E501
        :type: int
        """

        self._feedbacks_count = feedbacks_count

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
        if issubclass(InlineResponse20017Data, dict):
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
        if not isinstance(other, InlineResponse20017Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
