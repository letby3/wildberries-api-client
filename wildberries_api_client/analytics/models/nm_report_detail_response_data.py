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

class NmReportDetailResponseData(object):
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
        'page': 'int',
        'is_next_page': 'bool',
        'cards': 'list[NmReportDetailResponseDataCards]'
    }

    attribute_map = {
        'page': 'page',
        'is_next_page': 'isNextPage',
        'cards': 'cards'
    }

    def __init__(self, page=None, is_next_page=None, cards=None):  # noqa: E501
        """NmReportDetailResponseData - a model defined in Swagger"""  # noqa: E501
        self._page = None
        self._is_next_page = None
        self._cards = None
        self.discriminator = None
        if page is not None:
            self.page = page
        if is_next_page is not None:
            self.is_next_page = is_next_page
        if cards is not None:
            self.cards = cards

    @property
    def page(self):
        """Gets the page of this NmReportDetailResponseData.  # noqa: E501

        Stranica  # noqa: E501

        :return: The page of this NmReportDetailResponseData.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this NmReportDetailResponseData.

        Stranica  # noqa: E501

        :param page: The page of this NmReportDetailResponseData.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def is_next_page(self):
        """Gets the is_next_page of this NmReportDetailResponseData.  # noqa: E501

        Est li sleduuhaa stranica (false - net, true - est)  # noqa: E501

        :return: The is_next_page of this NmReportDetailResponseData.  # noqa: E501
        :rtype: bool
        """
        return self._is_next_page

    @is_next_page.setter
    def is_next_page(self, is_next_page):
        """Sets the is_next_page of this NmReportDetailResponseData.

        Est li sleduuhaa stranica (false - net, true - est)  # noqa: E501

        :param is_next_page: The is_next_page of this NmReportDetailResponseData.  # noqa: E501
        :type: bool
        """

        self._is_next_page = is_next_page

    @property
    def cards(self):
        """Gets the cards of this NmReportDetailResponseData.  # noqa: E501


        :return: The cards of this NmReportDetailResponseData.  # noqa: E501
        :rtype: list[NmReportDetailResponseDataCards]
        """
        return self._cards

    @cards.setter
    def cards(self, cards):
        """Sets the cards of this NmReportDetailResponseData.


        :param cards: The cards of this NmReportDetailResponseData.  # noqa: E501
        :type: list[NmReportDetailResponseDataCards]
        """

        self._cards = cards

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
        if issubclass(NmReportDetailResponseData, dict):
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
        if not isinstance(other, NmReportDetailResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
