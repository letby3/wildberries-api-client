# coding: utf-8

"""
    Opisanie API Prodvihenie

    Sinhronizacia dannyh iz bd proishodit raz v 3 minuty.  <br>Izmenenie statusa proishodit raz v 1 minutu. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu statusa. <br>Izmenenie stavki proishodit raz v 30 sekund. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu stavki.   # noqa: E501

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StatsBlok1(object):
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
        'item_id': 'int',
        'item_name': 'str',
        'category_name': 'str',
        'advert_type': 'int',
        'place': 'int',
        'views': 'int',
        'clicks': 'int',
        'cr': 'float',
        'ctr': 'float',
        'date_from': 'datetime',
        'date_to': 'datetime',
        'subject_name': 'str',
        'atbs': 'int',
        'orders': 'int',
        'price': 'int',
        'cpc': 'float',
        'status': 'int',
        'daily_stats': 'DailyStats1',
        'expenses': 'int',
        'cr1': 'float',
        'cr2': 'int'
    }

    attribute_map = {
        'item_id': 'item_id',
        'item_name': 'item_name',
        'category_name': 'category_name',
        'advert_type': 'advert_type',
        'place': 'place',
        'views': 'views',
        'clicks': 'clicks',
        'cr': 'cr',
        'ctr': 'ctr',
        'date_from': 'date_from',
        'date_to': 'date_to',
        'subject_name': 'subject_name',
        'atbs': 'atbs',
        'orders': 'orders',
        'price': 'price',
        'cpc': 'cpc',
        'status': 'status',
        'daily_stats': 'daily_stats',
        'expenses': 'expenses',
        'cr1': 'cr1',
        'cr2': 'cr2'
    }

    def __init__(self, item_id=None, item_name=None, category_name=None, advert_type=None, place=None, views=None, clicks=None, cr=None, ctr=None, date_from=None, date_to=None, subject_name=None, atbs=None, orders=None, price=None, cpc=None, status=None, daily_stats=None, expenses=None, cr1=None, cr2=None):  # noqa: E501
        """StatsBlok1 - a model defined in Swagger"""  # noqa: E501
        self._item_id = None
        self._item_name = None
        self._category_name = None
        self._advert_type = None
        self._place = None
        self._views = None
        self._clicks = None
        self._cr = None
        self._ctr = None
        self._date_from = None
        self._date_to = None
        self._subject_name = None
        self._atbs = None
        self._orders = None
        self._price = None
        self._cpc = None
        self._status = None
        self._daily_stats = None
        self._expenses = None
        self._cr1 = None
        self._cr2 = None
        self.discriminator = None
        if item_id is not None:
            self.item_id = item_id
        if item_name is not None:
            self.item_name = item_name
        if category_name is not None:
            self.category_name = category_name
        if advert_type is not None:
            self.advert_type = advert_type
        if place is not None:
            self.place = place
        if views is not None:
            self.views = views
        if clicks is not None:
            self.clicks = clicks
        if cr is not None:
            self.cr = cr
        if ctr is not None:
            self.ctr = ctr
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to
        if subject_name is not None:
            self.subject_name = subject_name
        if atbs is not None:
            self.atbs = atbs
        if orders is not None:
            self.orders = orders
        if price is not None:
            self.price = price
        if cpc is not None:
            self.cpc = cpc
        if status is not None:
            self.status = status
        if daily_stats is not None:
            self.daily_stats = daily_stats
        if expenses is not None:
            self.expenses = expenses
        if cr1 is not None:
            self.cr1 = cr1
        if cr2 is not None:
            self.cr2 = cr2

    @property
    def item_id(self):
        """Gets the item_id of this StatsBlok1.  # noqa: E501

        ID bannera  # noqa: E501

        :return: The item_id of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this StatsBlok1.

        ID bannera  # noqa: E501

        :param item_id: The item_id of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._item_id = item_id

    @property
    def item_name(self):
        """Gets the item_name of this StatsBlok1.  # noqa: E501

        Nazvanie brenda  # noqa: E501

        :return: The item_name of this StatsBlok1.  # noqa: E501
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """Sets the item_name of this StatsBlok1.

        Nazvanie brenda  # noqa: E501

        :param item_name: The item_name of this StatsBlok1.  # noqa: E501
        :type: str
        """

        self._item_name = item_name

    @property
    def category_name(self):
        """Gets the category_name of this StatsBlok1.  # noqa: E501

        Nazvanie kategorii  # noqa: E501

        :return: The category_name of this StatsBlok1.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this StatsBlok1.

        Nazvanie kategorii  # noqa: E501

        :param category_name: The category_name of this StatsBlok1.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

    @property
    def advert_type(self):
        """Gets the advert_type of this StatsBlok1.  # noqa: E501

        <dl> <dt>Tip mediakampanii:</dt> <dd><code>1</code> - razmehenie po dnam</dd> <dd><code>2</code> - razmehenie po prosmotram</dd> </dl>   # noqa: E501

        :return: The advert_type of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._advert_type

    @advert_type.setter
    def advert_type(self, advert_type):
        """Sets the advert_type of this StatsBlok1.

        <dl> <dt>Tip mediakampanii:</dt> <dd><code>1</code> - razmehenie po dnam</dd> <dd><code>2</code> - razmehenie po prosmotram</dd> </dl>   # noqa: E501

        :param advert_type: The advert_type of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._advert_type = advert_type

    @property
    def place(self):
        """Gets the place of this StatsBlok1.  # noqa: E501

        Mesto na stranice  # noqa: E501

        :return: The place of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._place

    @place.setter
    def place(self, place):
        """Sets the place of this StatsBlok1.

        Mesto na stranice  # noqa: E501

        :param place: The place of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._place = place

    @property
    def views(self):
        """Gets the views of this StatsBlok1.  # noqa: E501

        Kolihestvo prosmotrov  # noqa: E501

        :return: The views of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._views

    @views.setter
    def views(self, views):
        """Sets the views of this StatsBlok1.

        Kolihestvo prosmotrov  # noqa: E501

        :param views: The views of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._views = views

    @property
    def clicks(self):
        """Gets the clicks of this StatsBlok1.  # noqa: E501

        Kolihestvo klikov  # noqa: E501

        :return: The clicks of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        """Sets the clicks of this StatsBlok1.

        Kolihestvo klikov  # noqa: E501

        :param clicks: The clicks of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._clicks = clicks

    @property
    def cr(self):
        """Gets the cr of this StatsBlok1.  # noqa: E501

        CR(conversion rate) — eto otnohenie kolihestva zakazov k obhemu kolihestvu posehenii mediakampanii.   # noqa: E501

        :return: The cr of this StatsBlok1.  # noqa: E501
        :rtype: float
        """
        return self._cr

    @cr.setter
    def cr(self, cr):
        """Sets the cr of this StatsBlok1.

        CR(conversion rate) — eto otnohenie kolihestva zakazov k obhemu kolihestvu posehenii mediakampanii.   # noqa: E501

        :param cr: The cr of this StatsBlok1.  # noqa: E501
        :type: float
        """

        self._cr = cr

    @property
    def ctr(self):
        """Gets the ctr of this StatsBlok1.  # noqa: E501

        CTR (click-through rate) — to pokazatel klikabelnosti, to est otnohenie hisla klikov k kolihestvu pokazov v ramkah mediakampanii.   # noqa: E501

        :return: The ctr of this StatsBlok1.  # noqa: E501
        :rtype: float
        """
        return self._ctr

    @ctr.setter
    def ctr(self, ctr):
        """Sets the ctr of this StatsBlok1.

        CTR (click-through rate) — to pokazatel klikabelnosti, to est otnohenie hisla klikov k kolihestvu pokazov v ramkah mediakampanii.   # noqa: E501

        :param ctr: The ctr of this StatsBlok1.  # noqa: E501
        :type: float
        """

        self._ctr = ctr

    @property
    def date_from(self):
        """Gets the date_from of this StatsBlok1.  # noqa: E501

        Vrema nahala razmehenia  # noqa: E501

        :return: The date_from of this StatsBlok1.  # noqa: E501
        :rtype: datetime
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this StatsBlok1.

        Vrema nahala razmehenia  # noqa: E501

        :param date_from: The date_from of this StatsBlok1.  # noqa: E501
        :type: datetime
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this StatsBlok1.  # noqa: E501

        Vrema zaverhenia razmehenia  # noqa: E501

        :return: The date_to of this StatsBlok1.  # noqa: E501
        :rtype: datetime
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this StatsBlok1.

        Vrema zaverhenia razmehenia  # noqa: E501

        :param date_to: The date_to of this StatsBlok1.  # noqa: E501
        :type: datetime
        """

        self._date_to = date_to

    @property
    def subject_name(self):
        """Gets the subject_name of this StatsBlok1.  # noqa: E501

        Roditelskaa kategoria predmeta  # noqa: E501

        :return: The subject_name of this StatsBlok1.  # noqa: E501
        :rtype: str
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        """Sets the subject_name of this StatsBlok1.

        Roditelskaa kategoria predmeta  # noqa: E501

        :param subject_name: The subject_name of this StatsBlok1.  # noqa: E501
        :type: str
        """

        self._subject_name = subject_name

    @property
    def atbs(self):
        """Gets the atbs of this StatsBlok1.  # noqa: E501

        Kolihestvo dobavlenii tovarov v korzinu  # noqa: E501

        :return: The atbs of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._atbs

    @atbs.setter
    def atbs(self, atbs):
        """Sets the atbs of this StatsBlok1.

        Kolihestvo dobavlenii tovarov v korzinu  # noqa: E501

        :param atbs: The atbs of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._atbs = atbs

    @property
    def orders(self):
        """Gets the orders of this StatsBlok1.  # noqa: E501

        Kolihestvo zakazov  # noqa: E501

        :return: The orders of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this StatsBlok1.

        Kolihestvo zakazov  # noqa: E501

        :param orders: The orders of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._orders = orders

    @property
    def price(self):
        """Gets the price of this StatsBlok1.  # noqa: E501

        Stoimost razmehenia  # noqa: E501

        :return: The price of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this StatsBlok1.

        Stoimost razmehenia  # noqa: E501

        :param price: The price of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._price = price

    @property
    def cpc(self):
        """Gets the cpc of this StatsBlok1.  # noqa: E501

        (cost per click) - cena klika po prodvigaemomu tovaru  # noqa: E501

        :return: The cpc of this StatsBlok1.  # noqa: E501
        :rtype: float
        """
        return self._cpc

    @cpc.setter
    def cpc(self, cpc):
        """Sets the cpc of this StatsBlok1.

        (cost per click) - cena klika po prodvigaemomu tovaru  # noqa: E501

        :param cpc: The cpc of this StatsBlok1.  # noqa: E501
        :type: float
        """

        self._cpc = cpc

    @property
    def status(self):
        """Gets the status of this StatsBlok1.  # noqa: E501

        Status mediakampanii  # noqa: E501

        :return: The status of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StatsBlok1.

        Status mediakampanii  # noqa: E501

        :param status: The status of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def daily_stats(self):
        """Gets the daily_stats of this StatsBlok1.  # noqa: E501


        :return: The daily_stats of this StatsBlok1.  # noqa: E501
        :rtype: DailyStats1
        """
        return self._daily_stats

    @daily_stats.setter
    def daily_stats(self, daily_stats):
        """Sets the daily_stats of this StatsBlok1.


        :param daily_stats: The daily_stats of this StatsBlok1.  # noqa: E501
        :type: DailyStats1
        """

        self._daily_stats = daily_stats

    @property
    def expenses(self):
        """Gets the expenses of this StatsBlok1.  # noqa: E501

        Stoimost razmehenia bannera  # noqa: E501

        :return: The expenses of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._expenses

    @expenses.setter
    def expenses(self, expenses):
        """Sets the expenses of this StatsBlok1.

        Stoimost razmehenia bannera  # noqa: E501

        :param expenses: The expenses of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._expenses = expenses

    @property
    def cr1(self):
        """Gets the cr1 of this StatsBlok1.  # noqa: E501

        Otnohenie kolihestva dobavlenii v korzinu k kolihestvu klikov  # noqa: E501

        :return: The cr1 of this StatsBlok1.  # noqa: E501
        :rtype: float
        """
        return self._cr1

    @cr1.setter
    def cr1(self, cr1):
        """Sets the cr1 of this StatsBlok1.

        Otnohenie kolihestva dobavlenii v korzinu k kolihestvu klikov  # noqa: E501

        :param cr1: The cr1 of this StatsBlok1.  # noqa: E501
        :type: float
        """

        self._cr1 = cr1

    @property
    def cr2(self):
        """Gets the cr2 of this StatsBlok1.  # noqa: E501

        Otnohenie kolihestva zakazov k kolihestvu dobavlenii v korzinu  # noqa: E501

        :return: The cr2 of this StatsBlok1.  # noqa: E501
        :rtype: int
        """
        return self._cr2

    @cr2.setter
    def cr2(self, cr2):
        """Sets the cr2 of this StatsBlok1.

        Otnohenie kolihestva zakazov k kolihestvu dobavlenii v korzinu  # noqa: E501

        :param cr2: The cr2 of this StatsBlok1.  # noqa: E501
        :type: int
        """

        self._cr2 = cr2

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
        if issubclass(StatsBlok1, dict):
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
        if not isinstance(other, StatsBlok1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other