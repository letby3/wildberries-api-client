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

class NmReportDetailResponseDataStatisticsSelectedPeriod(object):
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
        'begin': 'str',
        'end': 'str',
        'open_card_count': 'int',
        'add_to_cart_count': 'int',
        'orders_count': 'int',
        'orders_sum_rub': 'int',
        'buyouts_count': 'int',
        'buyouts_sum_rub': 'int',
        'cancel_count': 'int',
        'cancel_sum_rub': 'int',
        'avg_price_rub': 'int',
        'avg_orders_count_per_day': 'int',
        'conversions': 'NmReportDetailResponseDataStatisticsSelectedPeriodConversions'
    }

    attribute_map = {
        'begin': 'begin',
        'end': 'end',
        'open_card_count': 'openCardCount',
        'add_to_cart_count': 'addToCartCount',
        'orders_count': 'ordersCount',
        'orders_sum_rub': 'ordersSumRub',
        'buyouts_count': 'buyoutsCount',
        'buyouts_sum_rub': 'buyoutsSumRub',
        'cancel_count': 'cancelCount',
        'cancel_sum_rub': 'cancelSumRub',
        'avg_price_rub': 'avgPriceRub',
        'avg_orders_count_per_day': 'avgOrdersCountPerDay',
        'conversions': 'conversions'
    }

    def __init__(self, begin=None, end=None, open_card_count=None, add_to_cart_count=None, orders_count=None, orders_sum_rub=None, buyouts_count=None, buyouts_sum_rub=None, cancel_count=None, cancel_sum_rub=None, avg_price_rub=None, avg_orders_count_per_day=None, conversions=None):  # noqa: E501
        """NmReportDetailResponseDataStatisticsSelectedPeriod - a model defined in Swagger"""  # noqa: E501
        self._begin = None
        self._end = None
        self._open_card_count = None
        self._add_to_cart_count = None
        self._orders_count = None
        self._orders_sum_rub = None
        self._buyouts_count = None
        self._buyouts_sum_rub = None
        self._cancel_count = None
        self._cancel_sum_rub = None
        self._avg_price_rub = None
        self._avg_orders_count_per_day = None
        self._conversions = None
        self.discriminator = None
        if begin is not None:
            self.begin = begin
        if end is not None:
            self.end = end
        if open_card_count is not None:
            self.open_card_count = open_card_count
        if add_to_cart_count is not None:
            self.add_to_cart_count = add_to_cart_count
        if orders_count is not None:
            self.orders_count = orders_count
        if orders_sum_rub is not None:
            self.orders_sum_rub = orders_sum_rub
        if buyouts_count is not None:
            self.buyouts_count = buyouts_count
        if buyouts_sum_rub is not None:
            self.buyouts_sum_rub = buyouts_sum_rub
        if cancel_count is not None:
            self.cancel_count = cancel_count
        if cancel_sum_rub is not None:
            self.cancel_sum_rub = cancel_sum_rub
        if avg_price_rub is not None:
            self.avg_price_rub = avg_price_rub
        if avg_orders_count_per_day is not None:
            self.avg_orders_count_per_day = avg_orders_count_per_day
        if conversions is not None:
            self.conversions = conversions

    @property
    def begin(self):
        """Gets the begin of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Nahalo perioda  # noqa: E501

        :return: The begin of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: str
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Nahalo perioda  # noqa: E501

        :param begin: The begin of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: str
        """

        self._begin = begin

    @property
    def end(self):
        """Gets the end of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Konec perioda  # noqa: E501

        :return: The end of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Konec perioda  # noqa: E501

        :param end: The end of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def open_card_count(self):
        """Gets the open_card_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Kolihestvo perehodov v kartohku tovara  # noqa: E501

        :return: The open_card_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._open_card_count

    @open_card_count.setter
    def open_card_count(self, open_card_count):
        """Sets the open_card_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Kolihestvo perehodov v kartohku tovara  # noqa: E501

        :param open_card_count: The open_card_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._open_card_count = open_card_count

    @property
    def add_to_cart_count(self):
        """Gets the add_to_cart_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Polohili v korzinu, htuk  # noqa: E501

        :return: The add_to_cart_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._add_to_cart_count

    @add_to_cart_count.setter
    def add_to_cart_count(self, add_to_cart_count):
        """Sets the add_to_cart_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Polohili v korzinu, htuk  # noqa: E501

        :param add_to_cart_count: The add_to_cart_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._add_to_cart_count = add_to_cart_count

    @property
    def orders_count(self):
        """Gets the orders_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Zakazali tovarov, ht  # noqa: E501

        :return: The orders_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._orders_count

    @orders_count.setter
    def orders_count(self, orders_count):
        """Sets the orders_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Zakazali tovarov, ht  # noqa: E501

        :param orders_count: The orders_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._orders_count = orders_count

    @property
    def orders_sum_rub(self):
        """Gets the orders_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Zakazali na summu, rub.  # noqa: E501

        :return: The orders_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._orders_sum_rub

    @orders_sum_rub.setter
    def orders_sum_rub(self, orders_sum_rub):
        """Sets the orders_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Zakazali na summu, rub.  # noqa: E501

        :param orders_sum_rub: The orders_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._orders_sum_rub = orders_sum_rub

    @property
    def buyouts_count(self):
        """Gets the buyouts_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Vykupili tovarov, ht.  # noqa: E501

        :return: The buyouts_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._buyouts_count

    @buyouts_count.setter
    def buyouts_count(self, buyouts_count):
        """Sets the buyouts_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Vykupili tovarov, ht.  # noqa: E501

        :param buyouts_count: The buyouts_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._buyouts_count = buyouts_count

    @property
    def buyouts_sum_rub(self):
        """Gets the buyouts_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Vykupili na summu, rub.  # noqa: E501

        :return: The buyouts_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._buyouts_sum_rub

    @buyouts_sum_rub.setter
    def buyouts_sum_rub(self, buyouts_sum_rub):
        """Sets the buyouts_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Vykupili na summu, rub.  # noqa: E501

        :param buyouts_sum_rub: The buyouts_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._buyouts_sum_rub = buyouts_sum_rub

    @property
    def cancel_count(self):
        """Gets the cancel_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Otmenili tovarov, ht.  # noqa: E501

        :return: The cancel_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._cancel_count

    @cancel_count.setter
    def cancel_count(self, cancel_count):
        """Sets the cancel_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Otmenili tovarov, ht.  # noqa: E501

        :param cancel_count: The cancel_count of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._cancel_count = cancel_count

    @property
    def cancel_sum_rub(self):
        """Gets the cancel_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Otmenili na summu, rub.  # noqa: E501

        :return: The cancel_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._cancel_sum_rub

    @cancel_sum_rub.setter
    def cancel_sum_rub(self, cancel_sum_rub):
        """Sets the cancel_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Otmenili na summu, rub.  # noqa: E501

        :param cancel_sum_rub: The cancel_sum_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._cancel_sum_rub = cancel_sum_rub

    @property
    def avg_price_rub(self):
        """Gets the avg_price_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Srednaa cena, rub.  # noqa: E501

        :return: The avg_price_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._avg_price_rub

    @avg_price_rub.setter
    def avg_price_rub(self, avg_price_rub):
        """Sets the avg_price_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Srednaa cena, rub.  # noqa: E501

        :param avg_price_rub: The avg_price_rub of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._avg_price_rub = avg_price_rub

    @property
    def avg_orders_count_per_day(self):
        """Gets the avg_orders_count_per_day of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501

        Srednee kolihestvo zakazov v den, ht.  # noqa: E501

        :return: The avg_orders_count_per_day of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: int
        """
        return self._avg_orders_count_per_day

    @avg_orders_count_per_day.setter
    def avg_orders_count_per_day(self, avg_orders_count_per_day):
        """Sets the avg_orders_count_per_day of this NmReportDetailResponseDataStatisticsSelectedPeriod.

        Srednee kolihestvo zakazov v den, ht.  # noqa: E501

        :param avg_orders_count_per_day: The avg_orders_count_per_day of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: int
        """

        self._avg_orders_count_per_day = avg_orders_count_per_day

    @property
    def conversions(self):
        """Gets the conversions of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501


        :return: The conversions of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :rtype: NmReportDetailResponseDataStatisticsSelectedPeriodConversions
        """
        return self._conversions

    @conversions.setter
    def conversions(self, conversions):
        """Sets the conversions of this NmReportDetailResponseDataStatisticsSelectedPeriod.


        :param conversions: The conversions of this NmReportDetailResponseDataStatisticsSelectedPeriod.  # noqa: E501
        :type: NmReportDetailResponseDataStatisticsSelectedPeriodConversions
        """

        self._conversions = conversions

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
        if issubclass(NmReportDetailResponseDataStatisticsSelectedPeriod, dict):
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
        if not isinstance(other, NmReportDetailResponseDataStatisticsSelectedPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
