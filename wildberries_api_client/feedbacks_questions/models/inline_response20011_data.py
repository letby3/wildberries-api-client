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

class InlineResponse20011Data(object):
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
        'product_max_rating': 'ProductRating',
        'product_min_rating': 'ProductRating'
    }

    attribute_map = {
        'product_max_rating': 'productMaxRating',
        'product_min_rating': 'productMinRating'
    }

    def __init__(self, product_max_rating=None, product_min_rating=None):  # noqa: E501
        """InlineResponse20011Data - a model defined in Swagger"""  # noqa: E501
        self._product_max_rating = None
        self._product_min_rating = None
        self.discriminator = None
        if product_max_rating is not None:
            self.product_max_rating = product_max_rating
        if product_min_rating is not None:
            self.product_min_rating = product_min_rating

    @property
    def product_max_rating(self):
        """Gets the product_max_rating of this InlineResponse20011Data.  # noqa: E501


        :return: The product_max_rating of this InlineResponse20011Data.  # noqa: E501
        :rtype: ProductRating
        """
        return self._product_max_rating

    @product_max_rating.setter
    def product_max_rating(self, product_max_rating):
        """Sets the product_max_rating of this InlineResponse20011Data.


        :param product_max_rating: The product_max_rating of this InlineResponse20011Data.  # noqa: E501
        :type: ProductRating
        """

        self._product_max_rating = product_max_rating

    @property
    def product_min_rating(self):
        """Gets the product_min_rating of this InlineResponse20011Data.  # noqa: E501


        :return: The product_min_rating of this InlineResponse20011Data.  # noqa: E501
        :rtype: ProductRating
        """
        return self._product_min_rating

    @product_min_rating.setter
    def product_min_rating(self, product_min_rating):
        """Sets the product_min_rating of this InlineResponse20011Data.


        :param product_min_rating: The product_min_rating of this InlineResponse20011Data.  # noqa: E501
        :type: ProductRating
        """

        self._product_min_rating = product_min_rating

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
        if issubclass(InlineResponse20011Data, dict):
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
        if not isinstance(other, InlineResponse20011Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
