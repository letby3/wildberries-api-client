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

class InlineResponse20019DataAnswer(object):
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
        'text': 'str',
        'state': 'str'
    }

    attribute_map = {
        'text': 'text',
        'state': 'state'
    }

    def __init__(self, text=None, state=None):  # noqa: E501
        """InlineResponse20019DataAnswer - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self._state = None
        self.discriminator = None
        if text is not None:
            self.text = text
        if state is not None:
            self.state = state

    @property
    def text(self):
        """Gets the text of this InlineResponse20019DataAnswer.  # noqa: E501

        Tekst otveta  # noqa: E501

        :return: The text of this InlineResponse20019DataAnswer.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this InlineResponse20019DataAnswer.

        Tekst otveta  # noqa: E501

        :param text: The text of this InlineResponse20019DataAnswer.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def state(self):
        """Gets the state of this InlineResponse20019DataAnswer.  # noqa: E501

        <dt>Status:</dt> <dd>`none` - novyi</dd>  <dd>`wbRu`- otobrahaetsa na saite</dd>  <dd>`reviewRequired` - otvet prohodit proverku</dd> <dd>`rejected` - otvet otklonen</dd>   # noqa: E501

        :return: The state of this InlineResponse20019DataAnswer.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineResponse20019DataAnswer.

        <dt>Status:</dt> <dd>`none` - novyi</dd>  <dd>`wbRu`- otobrahaetsa na saite</dd>  <dd>`reviewRequired` - otvet prohodit proverku</dd> <dd>`rejected` - otvet otklonen</dd>   # noqa: E501

        :param state: The state of this InlineResponse20019DataAnswer.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(InlineResponse20019DataAnswer, dict):
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
        if not isinstance(other, InlineResponse20019DataAnswer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
