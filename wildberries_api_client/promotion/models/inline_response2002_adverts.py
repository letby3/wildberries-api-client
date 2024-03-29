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

class InlineResponse2002Adverts(object):
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
        'type': 'int',
        'status': 'int',
        'count': 'int'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'count': 'count'
    }

    def __init__(self, type=None, status=None, count=None):  # noqa: E501
        """InlineResponse2002Adverts - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._status = None
        self._count = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if count is not None:
            self.count = count

    @property
    def type(self):
        """Gets the type of this InlineResponse2002Adverts.  # noqa: E501

        <dl> <dt>Tip mediakampanii:</dt> <dd><code>1</code> - razmehenie po dnam</dd> <dd><code>2</code> - razmehenie po prosmotram</dd> </dl>   # noqa: E501

        :return: The type of this InlineResponse2002Adverts.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2002Adverts.

        <dl> <dt>Tip mediakampanii:</dt> <dd><code>1</code> - razmehenie po dnam</dd> <dd><code>2</code> - razmehenie po prosmotram</dd> </dl>   # noqa: E501

        :param type: The type of this InlineResponse2002Adverts.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this InlineResponse2002Adverts.  # noqa: E501

        <dl> <dt>Status mediakampanii:</dt>   <dd><code>1</code> - hernovik</dd>   <dd><code>2</code> - moderacia   <dd><code>3</code> - otkloneno (s vozmohnostu vernut na moderaciu)</dd>   <dd><code>4</code> - odobreno</dd>   <dd><code>5</code> - zaplanirovano</dd>   <dd><code>6</code> - na pokazah</dd>   <dd><code>7</code> - zaverheno</dd>   <dd><code>8</code> - otkazalsa</dd>   <dd><code>9</code> - priostanovlena prodavcom</dd>   <dd><code>10</code> - pauza po dnevnomu limitu</dd>   <dd><code>11</code> - pauza po rashodu budheta</dd> </dl>   # noqa: E501

        :return: The status of this InlineResponse2002Adverts.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2002Adverts.

        <dl> <dt>Status mediakampanii:</dt>   <dd><code>1</code> - hernovik</dd>   <dd><code>2</code> - moderacia   <dd><code>3</code> - otkloneno (s vozmohnostu vernut na moderaciu)</dd>   <dd><code>4</code> - odobreno</dd>   <dd><code>5</code> - zaplanirovano</dd>   <dd><code>6</code> - na pokazah</dd>   <dd><code>7</code> - zaverheno</dd>   <dd><code>8</code> - otkazalsa</dd>   <dd><code>9</code> - priostanovlena prodavcom</dd>   <dd><code>10</code> - pauza po dnevnomu limitu</dd>   <dd><code>11</code> - pauza po rashodu budheta</dd> </dl>   # noqa: E501

        :param status: The status of this InlineResponse2002Adverts.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def count(self):
        """Gets the count of this InlineResponse2002Adverts.  # noqa: E501

        Kolihestvo mediakampanii  # noqa: E501

        :return: The count of this InlineResponse2002Adverts.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this InlineResponse2002Adverts.

        Kolihestvo mediakampanii  # noqa: E501

        :param count: The count of this InlineResponse2002Adverts.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(InlineResponse2002Adverts, dict):
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
        if not isinstance(other, InlineResponse2002Adverts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
