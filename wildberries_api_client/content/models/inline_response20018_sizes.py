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

class InlineResponse20018Sizes(object):
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
        'chrt_id': 'int',
        'tech_size': 'str',
        'wb_size': 'str',
        'skus': 'list[str]'
    }

    attribute_map = {
        'chrt_id': 'chrtID',
        'tech_size': 'techSize',
        'wb_size': 'wbSize',
        'skus': 'skus'
    }

    def __init__(self, chrt_id=None, tech_size=None, wb_size=None, skus=None):  # noqa: E501
        """InlineResponse20018Sizes - a model defined in Swagger"""  # noqa: E501
        self._chrt_id = None
        self._tech_size = None
        self._wb_size = None
        self._skus = None
        self.discriminator = None
        if chrt_id is not None:
            self.chrt_id = chrt_id
        if tech_size is not None:
            self.tech_size = tech_size
        if wb_size is not None:
            self.wb_size = wb_size
        if skus is not None:
            self.skus = skus

    @property
    def chrt_id(self):
        """Gets the chrt_id of this InlineResponse20018Sizes.  # noqa: E501

        ID razmera  # noqa: E501

        :return: The chrt_id of this InlineResponse20018Sizes.  # noqa: E501
        :rtype: int
        """
        return self._chrt_id

    @chrt_id.setter
    def chrt_id(self, chrt_id):
        """Sets the chrt_id of this InlineResponse20018Sizes.

        ID razmera  # noqa: E501

        :param chrt_id: The chrt_id of this InlineResponse20018Sizes.  # noqa: E501
        :type: int
        """

        self._chrt_id = chrt_id

    @property
    def tech_size(self):
        """Gets the tech_size of this InlineResponse20018Sizes.  # noqa: E501

        Razmer tovara  # noqa: E501

        :return: The tech_size of this InlineResponse20018Sizes.  # noqa: E501
        :rtype: str
        """
        return self._tech_size

    @tech_size.setter
    def tech_size(self, tech_size):
        """Sets the tech_size of this InlineResponse20018Sizes.

        Razmer tovara  # noqa: E501

        :param tech_size: The tech_size of this InlineResponse20018Sizes.  # noqa: E501
        :type: str
        """

        self._tech_size = tech_size

    @property
    def wb_size(self):
        """Gets the wb_size of this InlineResponse20018Sizes.  # noqa: E501

        Rossiiskii razmer tovara  # noqa: E501

        :return: The wb_size of this InlineResponse20018Sizes.  # noqa: E501
        :rtype: str
        """
        return self._wb_size

    @wb_size.setter
    def wb_size(self, wb_size):
        """Sets the wb_size of this InlineResponse20018Sizes.

        Rossiiskii razmer tovara  # noqa: E501

        :param wb_size: The wb_size of this InlineResponse20018Sizes.  # noqa: E501
        :type: str
        """

        self._wb_size = wb_size

    @property
    def skus(self):
        """Gets the skus of this InlineResponse20018Sizes.  # noqa: E501

        Massiv barkodov  # noqa: E501

        :return: The skus of this InlineResponse20018Sizes.  # noqa: E501
        :rtype: list[str]
        """
        return self._skus

    @skus.setter
    def skus(self, skus):
        """Sets the skus of this InlineResponse20018Sizes.

        Massiv barkodov  # noqa: E501

        :param skus: The skus of this InlineResponse20018Sizes.  # noqa: E501
        :type: list[str]
        """

        self._skus = skus

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
        if issubclass(InlineResponse20018Sizes, dict):
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
        if not isinstance(other, InlineResponse20018Sizes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other