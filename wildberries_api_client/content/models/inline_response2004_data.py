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

class InlineResponse2004Data(object):
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
        'name': 'str',
        'id': 'int',
        'is_visible': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'is_visible': 'isVisible'
    }

    def __init__(self, name=None, id=None, is_visible=None):  # noqa: E501
        """InlineResponse2004Data - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._is_visible = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if is_visible is not None:
            self.is_visible = is_visible

    @property
    def name(self):
        """Gets the name of this InlineResponse2004Data.  # noqa: E501

        Nazvanie kategorii  # noqa: E501

        :return: The name of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2004Data.

        Nazvanie kategorii  # noqa: E501

        :param name: The name of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this InlineResponse2004Data.  # noqa: E501

        Identifikator roditelskoi kategorii  # noqa: E501

        :return: The id of this InlineResponse2004Data.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2004Data.

        Identifikator roditelskoi kategorii  # noqa: E501

        :param id: The id of this InlineResponse2004Data.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_visible(self):
        """Gets the is_visible of this InlineResponse2004Data.  # noqa: E501

        Viden na saite  # noqa: E501

        :return: The is_visible of this InlineResponse2004Data.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this InlineResponse2004Data.

        Viden na saite  # noqa: E501

        :param is_visible: The is_visible of this InlineResponse2004Data.  # noqa: E501
        :type: bool
        """

        self._is_visible = is_visible

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
        if issubclass(InlineResponse2004Data, dict):
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
        if not isinstance(other, InlineResponse2004Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other