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

class Contentv2getcardstrashSettings(object):
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
        'sort': 'Contentv2getcardstrashSettingsSort',
        'cursor': 'Contentv2getcardstrashSettingsCursor',
        'filter': 'Contentv2getcardstrashSettingsFilter'
    }

    attribute_map = {
        'sort': 'sort',
        'cursor': 'cursor',
        'filter': 'filter'
    }

    def __init__(self, sort=None, cursor=None, filter=None):  # noqa: E501
        """Contentv2getcardstrashSettings - a model defined in Swagger"""  # noqa: E501
        self._sort = None
        self._cursor = None
        self._filter = None
        self.discriminator = None
        if sort is not None:
            self.sort = sort
        if cursor is not None:
            self.cursor = cursor
        if filter is not None:
            self.filter = filter

    @property
    def sort(self):
        """Gets the sort of this Contentv2getcardstrashSettings.  # noqa: E501


        :return: The sort of this Contentv2getcardstrashSettings.  # noqa: E501
        :rtype: Contentv2getcardstrashSettingsSort
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this Contentv2getcardstrashSettings.


        :param sort: The sort of this Contentv2getcardstrashSettings.  # noqa: E501
        :type: Contentv2getcardstrashSettingsSort
        """

        self._sort = sort

    @property
    def cursor(self):
        """Gets the cursor of this Contentv2getcardstrashSettings.  # noqa: E501


        :return: The cursor of this Contentv2getcardstrashSettings.  # noqa: E501
        :rtype: Contentv2getcardstrashSettingsCursor
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this Contentv2getcardstrashSettings.


        :param cursor: The cursor of this Contentv2getcardstrashSettings.  # noqa: E501
        :type: Contentv2getcardstrashSettingsCursor
        """

        self._cursor = cursor

    @property
    def filter(self):
        """Gets the filter of this Contentv2getcardstrashSettings.  # noqa: E501


        :return: The filter of this Contentv2getcardstrashSettings.  # noqa: E501
        :rtype: Contentv2getcardstrashSettingsFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Contentv2getcardstrashSettings.


        :param filter: The filter of this Contentv2getcardstrashSettings.  # noqa: E501
        :type: Contentv2getcardstrashSettingsFilter
        """

        self._filter = filter

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
        if issubclass(Contentv2getcardstrashSettings, dict):
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
        if not isinstance(other, Contentv2getcardstrashSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
