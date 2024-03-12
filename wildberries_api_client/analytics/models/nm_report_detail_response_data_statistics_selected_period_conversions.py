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

class NmReportDetailResponseDataStatisticsSelectedPeriodConversions(object):
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
        'add_to_cart_percent': 'int',
        'cart_to_order_percent': 'int',
        'buyouts_percent': 'int'
    }

    attribute_map = {
        'add_to_cart_percent': 'addToCartPercent',
        'cart_to_order_percent': 'cartToOrderPercent',
        'buyouts_percent': 'buyoutsPercent'
    }

    def __init__(self, add_to_cart_percent=None, cart_to_order_percent=None, buyouts_percent=None):  # noqa: E501
        """NmReportDetailResponseDataStatisticsSelectedPeriodConversions - a model defined in Swagger"""  # noqa: E501
        self._add_to_cart_percent = None
        self._cart_to_order_percent = None
        self._buyouts_percent = None
        self.discriminator = None
        if add_to_cart_percent is not None:
            self.add_to_cart_percent = add_to_cart_percent
        if cart_to_order_percent is not None:
            self.cart_to_order_percent = cart_to_order_percent
        if buyouts_percent is not None:
            self.buyouts_percent = buyouts_percent

    @property
    def add_to_cart_percent(self):
        """Gets the add_to_cart_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.  # noqa: E501

        Konversia v korzinu, % (Kakoi procent posetitelei, otkryvhih kartohku tovara, dobavili tovar v korzinu)  # noqa: E501

        :return: The add_to_cart_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.  # noqa: E501
        :rtype: int
        """
        return self._add_to_cart_percent

    @add_to_cart_percent.setter
    def add_to_cart_percent(self, add_to_cart_percent):
        """Sets the add_to_cart_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.

        Konversia v korzinu, % (Kakoi procent posetitelei, otkryvhih kartohku tovara, dobavili tovar v korzinu)  # noqa: E501

        :param add_to_cart_percent: The add_to_cart_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.  # noqa: E501
        :type: int
        """

        self._add_to_cart_percent = add_to_cart_percent

    @property
    def cart_to_order_percent(self):
        """Gets the cart_to_order_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.  # noqa: E501

        Konversia v zakaz, % (Kakoi procent posititelei, dobavivhih tovar v korzinu, sdelali zakaz)  # noqa: E501

        :return: The cart_to_order_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.  # noqa: E501
        :rtype: int
        """
        return self._cart_to_order_percent

    @cart_to_order_percent.setter
    def cart_to_order_percent(self, cart_to_order_percent):
        """Sets the cart_to_order_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.

        Konversia v zakaz, % (Kakoi procent posititelei, dobavivhih tovar v korzinu, sdelali zakaz)  # noqa: E501

        :param cart_to_order_percent: The cart_to_order_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.  # noqa: E501
        :type: int
        """

        self._cart_to_order_percent = cart_to_order_percent

    @property
    def buyouts_percent(self):
        """Gets the buyouts_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.  # noqa: E501

        Procent vykupa, % ( Kakoi procent posetitelei, zakazvhih tovar, ego vykupili. Bez uheta tovarov, kotorye ehe dostavlautsa pokupatelu.)  # noqa: E501

        :return: The buyouts_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.  # noqa: E501
        :rtype: int
        """
        return self._buyouts_percent

    @buyouts_percent.setter
    def buyouts_percent(self, buyouts_percent):
        """Sets the buyouts_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.

        Procent vykupa, % ( Kakoi procent posetitelei, zakazvhih tovar, ego vykupili. Bez uheta tovarov, kotorye ehe dostavlautsa pokupatelu.)  # noqa: E501

        :param buyouts_percent: The buyouts_percent of this NmReportDetailResponseDataStatisticsSelectedPeriodConversions.  # noqa: E501
        :type: int
        """

        self._buyouts_percent = buyouts_percent

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
        if issubclass(NmReportDetailResponseDataStatisticsSelectedPeriodConversions, dict):
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
        if not isinstance(other, NmReportDetailResponseDataStatisticsSelectedPeriodConversions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
