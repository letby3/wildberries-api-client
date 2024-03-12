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

class InlineResponse2004(object):
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
        'advert_id': 'int',
        'name': 'str',
        'brand': 'str',
        'type': 'int',
        'status': 'int',
        'create_time': 'datetime',
        'extended': 'InlineResponse2004Extended',
        'items': 'list[InlineResponse2004Items]'
    }

    attribute_map = {
        'advert_id': 'advertId',
        'name': 'name',
        'brand': 'brand',
        'type': 'type',
        'status': 'status',
        'create_time': 'createTime',
        'extended': 'extended',
        'items': 'items'
    }

    def __init__(self, advert_id=None, name=None, brand=None, type=None, status=None, create_time=None, extended=None, items=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger"""  # noqa: E501
        self._advert_id = None
        self._name = None
        self._brand = None
        self._type = None
        self._status = None
        self._create_time = None
        self._extended = None
        self._items = None
        self.discriminator = None
        if advert_id is not None:
            self.advert_id = advert_id
        if name is not None:
            self.name = name
        if brand is not None:
            self.brand = brand
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if extended is not None:
            self.extended = extended
        if items is not None:
            self.items = items

    @property
    def advert_id(self):
        """Gets the advert_id of this InlineResponse2004.  # noqa: E501

        Identifikator mediakampanii  # noqa: E501

        :return: The advert_id of this InlineResponse2004.  # noqa: E501
        :rtype: int
        """
        return self._advert_id

    @advert_id.setter
    def advert_id(self, advert_id):
        """Sets the advert_id of this InlineResponse2004.

        Identifikator mediakampanii  # noqa: E501

        :param advert_id: The advert_id of this InlineResponse2004.  # noqa: E501
        :type: int
        """

        self._advert_id = advert_id

    @property
    def name(self):
        """Gets the name of this InlineResponse2004.  # noqa: E501

        Nazvanie mediakampanii  # noqa: E501

        :return: The name of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2004.

        Nazvanie mediakampanii  # noqa: E501

        :param name: The name of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def brand(self):
        """Gets the brand of this InlineResponse2004.  # noqa: E501

        Nazvanie brenda  # noqa: E501

        :return: The brand of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this InlineResponse2004.

        Nazvanie brenda  # noqa: E501

        :param brand: The brand of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def type(self):
        """Gets the type of this InlineResponse2004.  # noqa: E501

        <dl> <dt>Tip mediakampanii:</dt> <dd><code>1</code> - razmehenie po dnam</dd> <dd><code>2</code> - razmehenie po prosmotram</dd> </dl>   # noqa: E501

        :return: The type of this InlineResponse2004.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2004.

        <dl> <dt>Tip mediakampanii:</dt> <dd><code>1</code> - razmehenie po dnam</dd> <dd><code>2</code> - razmehenie po prosmotram</dd> </dl>   # noqa: E501

        :param type: The type of this InlineResponse2004.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this InlineResponse2004.  # noqa: E501

        <dl> <dt>Status mediakampanii:</dt>   <dd><code>1</code> - hernovik</dd>   <dd><code>2</code> - moderacia   <dd><code>3</code> - otkloneno (s vozmohnostu vernut na moderaciu)</dd>   <dd><code>4</code> - odobreno</dd>   <dd><code>5</code> - zaplanirovano</dd>   <dd><code>6</code> - na pokazah</dd>   <dd><code>7</code> - zaverheno</dd>   <dd><code>8</code> - otkazalsa</dd>   <dd><code>9</code> - priostanovlena prodavcom</dd>   <dd><code>10</code> - pauza po dnevnomu limitu</dd>   <dd><code>11</code> - pauza po rashodu budheta</dd> </dl>   # noqa: E501

        :return: The status of this InlineResponse2004.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2004.

        <dl> <dt>Status mediakampanii:</dt>   <dd><code>1</code> - hernovik</dd>   <dd><code>2</code> - moderacia   <dd><code>3</code> - otkloneno (s vozmohnostu vernut na moderaciu)</dd>   <dd><code>4</code> - odobreno</dd>   <dd><code>5</code> - zaplanirovano</dd>   <dd><code>6</code> - na pokazah</dd>   <dd><code>7</code> - zaverheno</dd>   <dd><code>8</code> - otkazalsa</dd>   <dd><code>9</code> - priostanovlena prodavcom</dd>   <dd><code>10</code> - pauza po dnevnomu limitu</dd>   <dd><code>11</code> - pauza po rashodu budheta</dd> </dl>   # noqa: E501

        :param status: The status of this InlineResponse2004.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this InlineResponse2004.  # noqa: E501

        Vrema sozdania mediakampanii  # noqa: E501

        :return: The create_time of this InlineResponse2004.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InlineResponse2004.

        Vrema sozdania mediakampanii  # noqa: E501

        :param create_time: The create_time of this InlineResponse2004.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def extended(self):
        """Gets the extended of this InlineResponse2004.  # noqa: E501


        :return: The extended of this InlineResponse2004.  # noqa: E501
        :rtype: InlineResponse2004Extended
        """
        return self._extended

    @extended.setter
    def extended(self, extended):
        """Sets the extended of this InlineResponse2004.


        :param extended: The extended of this InlineResponse2004.  # noqa: E501
        :type: InlineResponse2004Extended
        """

        self._extended = extended

    @property
    def items(self):
        """Gets the items of this InlineResponse2004.  # noqa: E501

        Informacia o bannere. <br> Nalihie v otvete teh ili inyh polei zavisit ot konfiguracii mediakampanii.   # noqa: E501

        :return: The items of this InlineResponse2004.  # noqa: E501
        :rtype: list[InlineResponse2004Items]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InlineResponse2004.

        Informacia o bannere. <br> Nalihie v otvete teh ili inyh polei zavisit ot konfiguracii mediakampanii.   # noqa: E501

        :param items: The items of this InlineResponse2004.  # noqa: E501
        :type: list[InlineResponse2004Items]
        """

        self._items = items

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
        if issubclass(InlineResponse2004, dict):
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
        if not isinstance(other, InlineResponse2004):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
