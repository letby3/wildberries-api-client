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

class InlineResponse2008Data(object):
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
        'upload_id': 'int',
        'buffer_goods': 'list[GoodBufferHistory]'
    }

    attribute_map = {
        'upload_id': 'uploadID',
        'buffer_goods': 'bufferGoods'
    }

    def __init__(self, upload_id=None, buffer_goods=None):  # noqa: E501
        """InlineResponse2008Data - a model defined in Swagger"""  # noqa: E501
        self._upload_id = None
        self._buffer_goods = None
        self.discriminator = None
        if upload_id is not None:
            self.upload_id = upload_id
        if buffer_goods is not None:
            self.buffer_goods = buffer_goods

    @property
    def upload_id(self):
        """Gets the upload_id of this InlineResponse2008Data.  # noqa: E501

        ID zagruzki  # noqa: E501

        :return: The upload_id of this InlineResponse2008Data.  # noqa: E501
        :rtype: int
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this InlineResponse2008Data.

        ID zagruzki  # noqa: E501

        :param upload_id: The upload_id of this InlineResponse2008Data.  # noqa: E501
        :type: int
        """

        self._upload_id = upload_id

    @property
    def buffer_goods(self):
        """Gets the buffer_goods of this InlineResponse2008Data.  # noqa: E501

        Informacia o tovarah v zagruzke  # noqa: E501

        :return: The buffer_goods of this InlineResponse2008Data.  # noqa: E501
        :rtype: list[GoodBufferHistory]
        """
        return self._buffer_goods

    @buffer_goods.setter
    def buffer_goods(self, buffer_goods):
        """Sets the buffer_goods of this InlineResponse2008Data.

        Informacia o tovarah v zagruzke  # noqa: E501

        :param buffer_goods: The buffer_goods of this InlineResponse2008Data.  # noqa: E501
        :type: list[GoodBufferHistory]
        """

        self._buffer_goods = buffer_goods

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
        if issubclass(InlineResponse2008Data, dict):
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
        if not isinstance(other, InlineResponse2008Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other