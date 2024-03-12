# coding: utf-8

"""
    Opisanie API Kontenta

     <dl> <dt>Slovar sokrahenii:</dt> <dd>KT — kartohka tovara</dd> <dd>NM—- nomenklatura</dd> </dl> Ogranihenia po kolihestvu zaprosov: <dd>Dopuskaetsa maksimum 100 zaprosov v minutu na metody kontenta v celom.</dd> <br> Publihnoe API Kontenta sozdano dla sinhronizacii dannyh mehdu serverami Wildberries i serverami prodavcov. <br> Vy zagruhaete dannye na svoi nositeli, rabotaete s nimi na svoih mohnostah i sinhroniziruetes s nahimi serverami po mere neobhodimosti. <br> <code>Ne dopuskaetsa ispolzovanie API Kontenta v kahestve vnehnei bazy dannyh. Pri prevyhenii limitov na zaprosy dostup k API budet ogranihen.</code> <br> <br> <br>   # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Contentv2cardsuploadDimensions(object):
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
        'length': 'int',
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'length': 'length',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, length=None, width=None, height=None):  # noqa: E501
        """Contentv2cardsuploadDimensions - a model defined in Swagger"""  # noqa: E501
        self._length = None
        self._width = None
        self._height = None
        self.discriminator = None
        if length is not None:
            self.length = length
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def length(self):
        """Gets the length of this Contentv2cardsuploadDimensions.  # noqa: E501

        Dlina  # noqa: E501

        :return: The length of this Contentv2cardsuploadDimensions.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Contentv2cardsuploadDimensions.

        Dlina  # noqa: E501

        :param length: The length of this Contentv2cardsuploadDimensions.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def width(self):
        """Gets the width of this Contentv2cardsuploadDimensions.  # noqa: E501

        hirina  # noqa: E501

        :return: The width of this Contentv2cardsuploadDimensions.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Contentv2cardsuploadDimensions.

        hirina  # noqa: E501

        :param width: The width of this Contentv2cardsuploadDimensions.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this Contentv2cardsuploadDimensions.  # noqa: E501

        Vysota  # noqa: E501

        :return: The height of this Contentv2cardsuploadDimensions.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Contentv2cardsuploadDimensions.

        Vysota  # noqa: E501

        :param height: The height of this Contentv2cardsuploadDimensions.  # noqa: E501
        :type: int
        """

        self._height = height

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
        if issubclass(Contentv2cardsuploadDimensions, dict):
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
        if not isinstance(other, Contentv2cardsuploadDimensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other