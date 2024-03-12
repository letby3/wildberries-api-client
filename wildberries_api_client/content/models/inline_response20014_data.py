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

class InlineResponse20014Data(object):
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
        'id': 'int',
        'color': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'color': 'color',
        'name': 'name'
    }

    def __init__(self, id=None, color=None, name=None):  # noqa: E501
        """InlineResponse20014Data - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._color = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if color is not None:
            self.color = color
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this InlineResponse20014Data.  # noqa: E501

        hislovoi identifikator tega  # noqa: E501

        :return: The id of this InlineResponse20014Data.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20014Data.

        hislovoi identifikator tega  # noqa: E501

        :param id: The id of this InlineResponse20014Data.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def color(self):
        """Gets the color of this InlineResponse20014Data.  # noqa: E501

        cvet tega  # noqa: E501

        :return: The color of this InlineResponse20014Data.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this InlineResponse20014Data.

        cvet tega  # noqa: E501

        :param color: The color of this InlineResponse20014Data.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def name(self):
        """Gets the name of this InlineResponse20014Data.  # noqa: E501

        Ima tega  # noqa: E501

        :return: The name of this InlineResponse20014Data.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20014Data.

        Ima tega  # noqa: E501

        :param name: The name of this InlineResponse20014Data.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(InlineResponse20014Data, dict):
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
        if not isinstance(other, InlineResponse20014Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other