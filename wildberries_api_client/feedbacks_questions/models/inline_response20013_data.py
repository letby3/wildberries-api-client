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

class InlineResponse20013Data(object):
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
        'feedback_valuations': 'InlineResponse20013DataFeedbackValuations',
        'product_valuations': 'InlineResponse20013DataProductValuations'
    }

    attribute_map = {
        'feedback_valuations': 'feedbackValuations',
        'product_valuations': 'productValuations'
    }

    def __init__(self, feedback_valuations=None, product_valuations=None):  # noqa: E501
        """InlineResponse20013Data - a model defined in Swagger"""  # noqa: E501
        self._feedback_valuations = None
        self._product_valuations = None
        self.discriminator = None
        if feedback_valuations is not None:
            self.feedback_valuations = feedback_valuations
        if product_valuations is not None:
            self.product_valuations = product_valuations

    @property
    def feedback_valuations(self):
        """Gets the feedback_valuations of this InlineResponse20013Data.  # noqa: E501


        :return: The feedback_valuations of this InlineResponse20013Data.  # noqa: E501
        :rtype: InlineResponse20013DataFeedbackValuations
        """
        return self._feedback_valuations

    @feedback_valuations.setter
    def feedback_valuations(self, feedback_valuations):
        """Sets the feedback_valuations of this InlineResponse20013Data.


        :param feedback_valuations: The feedback_valuations of this InlineResponse20013Data.  # noqa: E501
        :type: InlineResponse20013DataFeedbackValuations
        """

        self._feedback_valuations = feedback_valuations

    @property
    def product_valuations(self):
        """Gets the product_valuations of this InlineResponse20013Data.  # noqa: E501


        :return: The product_valuations of this InlineResponse20013Data.  # noqa: E501
        :rtype: InlineResponse20013DataProductValuations
        """
        return self._product_valuations

    @product_valuations.setter
    def product_valuations(self, product_valuations):
        """Sets the product_valuations of this InlineResponse20013Data.


        :param product_valuations: The product_valuations of this InlineResponse20013Data.  # noqa: E501
        :type: InlineResponse20013DataProductValuations
        """

        self._product_valuations = product_valuations

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
        if issubclass(InlineResponse20013Data, dict):
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
        if not isinstance(other, InlineResponse20013Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
