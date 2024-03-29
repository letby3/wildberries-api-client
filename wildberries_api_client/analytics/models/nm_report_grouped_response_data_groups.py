# coding: utf-8

"""
    Opisanie API Analitika

    **Servis predostavlaet publihnyi API dla poluhenia analitiheskih dannyh.**          Analitiheskie dannye v istohnike hranatsa za poslednii god, pri vybore daty nahala perioda ranee hem god nazad, budet   vozvrahatsa ohibka, takim obrazom maksimalnoe kol-vo dnei v agregaciah — 365.  Takhe v dannyh, gde predostavlaetsa informacia po predyduhemu periodu:   1. V `previousPeriod` dannye za takoi he period, hto i v `selectedPeriod`.   2. Esli data nahala `previousPeriod` ranee, hem god nazad ot tekuhei daty, ona budet privedena k vidu:      `previousPeriod.start = tekuhaa data - 365 dnei.`  #### Taimzony  Format IANA, aktualnyi spisok mohno posmotret [zdes](https://nodatime.org/TimeZones). <br> <br> <br>   # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NmReportGroupedResponseDataGroups(object):
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
        'brand_name': 'str',
        'tags': 'list[NmReportDetailResponseDataTags]',
        'object': 'NmReportGroupedResponseDataObject',
        'statistics': 'NmReportGroupedResponseDataStatistics'
    }

    attribute_map = {
        'brand_name': 'brandName',
        'tags': 'tags',
        'object': 'object',
        'statistics': 'statistics'
    }

    def __init__(self, brand_name=None, tags=None, object=None, statistics=None):  # noqa: E501
        """NmReportGroupedResponseDataGroups - a model defined in Swagger"""  # noqa: E501
        self._brand_name = None
        self._tags = None
        self._object = None
        self._statistics = None
        self.discriminator = None
        if brand_name is not None:
            self.brand_name = brand_name
        if tags is not None:
            self.tags = tags
        if object is not None:
            self.object = object
        if statistics is not None:
            self.statistics = statistics

    @property
    def brand_name(self):
        """Gets the brand_name of this NmReportGroupedResponseDataGroups.  # noqa: E501

        Nazvanie brenda  # noqa: E501

        :return: The brand_name of this NmReportGroupedResponseDataGroups.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this NmReportGroupedResponseDataGroups.

        Nazvanie brenda  # noqa: E501

        :param brand_name: The brand_name of this NmReportGroupedResponseDataGroups.  # noqa: E501
        :type: str
        """

        self._brand_name = brand_name

    @property
    def tags(self):
        """Gets the tags of this NmReportGroupedResponseDataGroups.  # noqa: E501


        :return: The tags of this NmReportGroupedResponseDataGroups.  # noqa: E501
        :rtype: list[NmReportDetailResponseDataTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NmReportGroupedResponseDataGroups.


        :param tags: The tags of this NmReportGroupedResponseDataGroups.  # noqa: E501
        :type: list[NmReportDetailResponseDataTags]
        """

        self._tags = tags

    @property
    def object(self):
        """Gets the object of this NmReportGroupedResponseDataGroups.  # noqa: E501


        :return: The object of this NmReportGroupedResponseDataGroups.  # noqa: E501
        :rtype: NmReportGroupedResponseDataObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this NmReportGroupedResponseDataGroups.


        :param object: The object of this NmReportGroupedResponseDataGroups.  # noqa: E501
        :type: NmReportGroupedResponseDataObject
        """

        self._object = object

    @property
    def statistics(self):
        """Gets the statistics of this NmReportGroupedResponseDataGroups.  # noqa: E501


        :return: The statistics of this NmReportGroupedResponseDataGroups.  # noqa: E501
        :rtype: NmReportGroupedResponseDataStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this NmReportGroupedResponseDataGroups.


        :param statistics: The statistics of this NmReportGroupedResponseDataGroups.  # noqa: E501
        :type: NmReportGroupedResponseDataStatistics
        """

        self._statistics = statistics

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
        if issubclass(NmReportGroupedResponseDataGroups, dict):
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
        if not isinstance(other, NmReportGroupedResponseDataGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
