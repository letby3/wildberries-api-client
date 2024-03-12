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

class NmReportGroupedRequest(object):
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
        'object_i_ds': 'list[int]',
        'brand_names': 'list[str]',
        'tag_i_ds': 'list[int]',
        'timezone': 'str',
        'period': 'NmReportGroupedRequestPeriod',
        'order_by': 'NmReportGroupedRequestOrderBy',
        'page': 'int'
    }

    attribute_map = {
        'object_i_ds': 'objectIDs',
        'brand_names': 'brandNames',
        'tag_i_ds': 'tagIDs',
        'timezone': 'timezone',
        'period': 'period',
        'order_by': 'orderBy',
        'page': 'page'
    }

    def __init__(self, object_i_ds=None, brand_names=None, tag_i_ds=None, timezone=None, period=None, order_by=None, page=None):  # noqa: E501
        """NmReportGroupedRequest - a model defined in Swagger"""  # noqa: E501
        self._object_i_ds = None
        self._brand_names = None
        self._tag_i_ds = None
        self._timezone = None
        self._period = None
        self._order_by = None
        self._page = None
        self.discriminator = None
        if object_i_ds is not None:
            self.object_i_ds = object_i_ds
        if brand_names is not None:
            self.brand_names = brand_names
        if tag_i_ds is not None:
            self.tag_i_ds = tag_i_ds
        if timezone is not None:
            self.timezone = timezone
        self.period = period
        if order_by is not None:
            self.order_by = order_by
        self.page = page

    @property
    def object_i_ds(self):
        """Gets the object_i_ds of this NmReportGroupedRequest.  # noqa: E501

        Identifikator predmeta  # noqa: E501

        :return: The object_i_ds of this NmReportGroupedRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._object_i_ds

    @object_i_ds.setter
    def object_i_ds(self, object_i_ds):
        """Sets the object_i_ds of this NmReportGroupedRequest.

        Identifikator predmeta  # noqa: E501

        :param object_i_ds: The object_i_ds of this NmReportGroupedRequest.  # noqa: E501
        :type: list[int]
        """

        self._object_i_ds = object_i_ds

    @property
    def brand_names(self):
        """Gets the brand_names of this NmReportGroupedRequest.  # noqa: E501

        Nazvanie brenda  # noqa: E501

        :return: The brand_names of this NmReportGroupedRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._brand_names

    @brand_names.setter
    def brand_names(self, brand_names):
        """Sets the brand_names of this NmReportGroupedRequest.

        Nazvanie brenda  # noqa: E501

        :param brand_names: The brand_names of this NmReportGroupedRequest.  # noqa: E501
        :type: list[str]
        """

        self._brand_names = brand_names

    @property
    def tag_i_ds(self):
        """Gets the tag_i_ds of this NmReportGroupedRequest.  # noqa: E501

        Identifikator tega  # noqa: E501

        :return: The tag_i_ds of this NmReportGroupedRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._tag_i_ds

    @tag_i_ds.setter
    def tag_i_ds(self, tag_i_ds):
        """Sets the tag_i_ds of this NmReportGroupedRequest.

        Identifikator tega  # noqa: E501

        :param tag_i_ds: The tag_i_ds of this NmReportGroupedRequest.  # noqa: E501
        :type: list[int]
        """

        self._tag_i_ds = tag_i_ds

    @property
    def timezone(self):
        """Gets the timezone of this NmReportGroupedRequest.  # noqa: E501

        Vremennaa zona.<br> Esli ne ukazano, to po umolhaniu ispolzuetsa Europe/Moscow.   # noqa: E501

        :return: The timezone of this NmReportGroupedRequest.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this NmReportGroupedRequest.

        Vremennaa zona.<br> Esli ne ukazano, to po umolhaniu ispolzuetsa Europe/Moscow.   # noqa: E501

        :param timezone: The timezone of this NmReportGroupedRequest.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def period(self):
        """Gets the period of this NmReportGroupedRequest.  # noqa: E501


        :return: The period of this NmReportGroupedRequest.  # noqa: E501
        :rtype: NmReportGroupedRequestPeriod
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this NmReportGroupedRequest.


        :param period: The period of this NmReportGroupedRequest.  # noqa: E501
        :type: NmReportGroupedRequestPeriod
        """
        if period is None:
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501

        self._period = period

    @property
    def order_by(self):
        """Gets the order_by of this NmReportGroupedRequest.  # noqa: E501


        :return: The order_by of this NmReportGroupedRequest.  # noqa: E501
        :rtype: NmReportGroupedRequestOrderBy
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this NmReportGroupedRequest.


        :param order_by: The order_by of this NmReportGroupedRequest.  # noqa: E501
        :type: NmReportGroupedRequestOrderBy
        """

        self._order_by = order_by

    @property
    def page(self):
        """Gets the page of this NmReportGroupedRequest.  # noqa: E501

        Stranica  # noqa: E501

        :return: The page of this NmReportGroupedRequest.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this NmReportGroupedRequest.

        Stranica  # noqa: E501

        :param page: The page of this NmReportGroupedRequest.  # noqa: E501
        :type: int
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

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
        if issubclass(NmReportGroupedRequest, dict):
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
        if not isinstance(other, NmReportGroupedRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
