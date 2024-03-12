# coding: utf-8

"""
    Opisanie API Marketplace

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StocksWarehouseIdBody(object):
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
        'stocks': 'list[Apiv3stockswarehouseIdStocks]'
    }

    attribute_map = {
        'stocks': 'stocks'
    }

    def __init__(self, stocks=None):  # noqa: E501
        """StocksWarehouseIdBody - a model defined in Swagger"""  # noqa: E501
        self._stocks = None
        self.discriminator = None
        self.stocks = stocks

    @property
    def stocks(self):
        """Gets the stocks of this StocksWarehouseIdBody.  # noqa: E501

        Massiv barkodov tovarov i ih ostatkov  # noqa: E501

        :return: The stocks of this StocksWarehouseIdBody.  # noqa: E501
        :rtype: list[Apiv3stockswarehouseIdStocks]
        """
        return self._stocks

    @stocks.setter
    def stocks(self, stocks):
        """Sets the stocks of this StocksWarehouseIdBody.

        Massiv barkodov tovarov i ih ostatkov  # noqa: E501

        :param stocks: The stocks of this StocksWarehouseIdBody.  # noqa: E501
        :type: list[Apiv3stockswarehouseIdStocks]
        """
        if stocks is None:
            raise ValueError("Invalid value for `stocks`, must not be `None`")  # noqa: E501

        self._stocks = stocks

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
        if issubclass(StocksWarehouseIdBody, dict):
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
        if not isinstance(other, StocksWarehouseIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
