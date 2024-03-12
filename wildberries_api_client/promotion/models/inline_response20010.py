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

class InlineResponse20010(object):
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
        'upd_num': 'int',
        'upd_time': 'str',
        'upd_sum': 'int',
        'advert_id': 'int',
        'camp_name': 'str',
        'advert_type': 'int',
        'payment_type': 'str',
        'advert_status': 'int'
    }

    attribute_map = {
        'upd_num': 'updNum',
        'upd_time': 'updTime',
        'upd_sum': 'updSum',
        'advert_id': 'advertId',
        'camp_name': 'campName',
        'advert_type': 'advertType',
        'payment_type': 'paymentType',
        'advert_status': 'advertStatus'
    }

    def __init__(self, upd_num=None, upd_time=None, upd_sum=None, advert_id=None, camp_name=None, advert_type=None, payment_type=None, advert_status=None):  # noqa: E501
        """InlineResponse20010 - a model defined in Swagger"""  # noqa: E501
        self._upd_num = None
        self._upd_time = None
        self._upd_sum = None
        self._advert_id = None
        self._camp_name = None
        self._advert_type = None
        self._payment_type = None
        self._advert_status = None
        self.discriminator = None
        if upd_num is not None:
            self.upd_num = upd_num
        if upd_time is not None:
            self.upd_time = upd_time
        if upd_sum is not None:
            self.upd_sum = upd_sum
        if advert_id is not None:
            self.advert_id = advert_id
        if camp_name is not None:
            self.camp_name = camp_name
        if advert_type is not None:
            self.advert_type = advert_type
        if payment_type is not None:
            self.payment_type = payment_type
        if advert_status is not None:
            self.advert_status = advert_status

    @property
    def upd_num(self):
        """Gets the upd_num of this InlineResponse20010.  # noqa: E501

        Nomer vystavlennogo dokumenta (pri nalihii)  # noqa: E501

        :return: The upd_num of this InlineResponse20010.  # noqa: E501
        :rtype: int
        """
        return self._upd_num

    @upd_num.setter
    def upd_num(self, upd_num):
        """Sets the upd_num of this InlineResponse20010.

        Nomer vystavlennogo dokumenta (pri nalihii)  # noqa: E501

        :param upd_num: The upd_num of this InlineResponse20010.  # noqa: E501
        :type: int
        """

        self._upd_num = upd_num

    @property
    def upd_time(self):
        """Gets the upd_time of this InlineResponse20010.  # noqa: E501

        Vrema spisania  # noqa: E501

        :return: The upd_time of this InlineResponse20010.  # noqa: E501
        :rtype: str
        """
        return self._upd_time

    @upd_time.setter
    def upd_time(self, upd_time):
        """Sets the upd_time of this InlineResponse20010.

        Vrema spisania  # noqa: E501

        :param upd_time: The upd_time of this InlineResponse20010.  # noqa: E501
        :type: str
        """

        self._upd_time = upd_time

    @property
    def upd_sum(self):
        """Gets the upd_sum of this InlineResponse20010.  # noqa: E501

        Vystavlennaa summa  # noqa: E501

        :return: The upd_sum of this InlineResponse20010.  # noqa: E501
        :rtype: int
        """
        return self._upd_sum

    @upd_sum.setter
    def upd_sum(self, upd_sum):
        """Sets the upd_sum of this InlineResponse20010.

        Vystavlennaa summa  # noqa: E501

        :param upd_sum: The upd_sum of this InlineResponse20010.  # noqa: E501
        :type: int
        """

        self._upd_sum = upd_sum

    @property
    def advert_id(self):
        """Gets the advert_id of this InlineResponse20010.  # noqa: E501

        Identifikator kampanii  # noqa: E501

        :return: The advert_id of this InlineResponse20010.  # noqa: E501
        :rtype: int
        """
        return self._advert_id

    @advert_id.setter
    def advert_id(self, advert_id):
        """Sets the advert_id of this InlineResponse20010.

        Identifikator kampanii  # noqa: E501

        :param advert_id: The advert_id of this InlineResponse20010.  # noqa: E501
        :type: int
        """

        self._advert_id = advert_id

    @property
    def camp_name(self):
        """Gets the camp_name of this InlineResponse20010.  # noqa: E501

        Nazvanie kampanii  # noqa: E501

        :return: The camp_name of this InlineResponse20010.  # noqa: E501
        :rtype: str
        """
        return self._camp_name

    @camp_name.setter
    def camp_name(self, camp_name):
        """Sets the camp_name of this InlineResponse20010.

        Nazvanie kampanii  # noqa: E501

        :param camp_name: The camp_name of this InlineResponse20010.  # noqa: E501
        :type: str
        """

        self._camp_name = camp_name

    @property
    def advert_type(self):
        """Gets the advert_type of this InlineResponse20010.  # noqa: E501

        Tip kampanii  # noqa: E501

        :return: The advert_type of this InlineResponse20010.  # noqa: E501
        :rtype: int
        """
        return self._advert_type

    @advert_type.setter
    def advert_type(self, advert_type):
        """Sets the advert_type of this InlineResponse20010.

        Tip kampanii  # noqa: E501

        :param advert_type: The advert_type of this InlineResponse20010.  # noqa: E501
        :type: int
        """

        self._advert_type = advert_type

    @property
    def payment_type(self):
        """Gets the payment_type of this InlineResponse20010.  # noqa: E501

        <dl> <dt>Istohnik spisania:</dt> <dd>Balans</dd> <dd>Bonusy</dd> <dd>Shet</dd> </dl>   # noqa: E501

        :return: The payment_type of this InlineResponse20010.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this InlineResponse20010.

        <dl> <dt>Istohnik spisania:</dt> <dd>Balans</dd> <dd>Bonusy</dd> <dd>Shet</dd> </dl>   # noqa: E501

        :param payment_type: The payment_type of this InlineResponse20010.  # noqa: E501
        :type: str
        """

        self._payment_type = payment_type

    @property
    def advert_status(self):
        """Gets the advert_status of this InlineResponse20010.  # noqa: E501

        <dl>   <dt>Status kampanii:</dt>   <dd><code>4</code> - gotova k zapusku </dd>   <dd><code>7</code> - zaverhena</dd>   <dd><code>8</code> - otkazalsa</dd>   <dd><code>9</code> - aktivna</dd>   <dd><code>11</code> - priostanovlena</dd> </dl>   # noqa: E501

        :return: The advert_status of this InlineResponse20010.  # noqa: E501
        :rtype: int
        """
        return self._advert_status

    @advert_status.setter
    def advert_status(self, advert_status):
        """Sets the advert_status of this InlineResponse20010.

        <dl>   <dt>Status kampanii:</dt>   <dd><code>4</code> - gotova k zapusku </dd>   <dd><code>7</code> - zaverhena</dd>   <dd><code>8</code> - otkazalsa</dd>   <dd><code>9</code> - aktivna</dd>   <dd><code>11</code> - priostanovlena</dd> </dl>   # noqa: E501

        :param advert_status: The advert_status of this InlineResponse20010.  # noqa: E501
        :type: int
        """

        self._advert_status = advert_status

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
        if issubclass(InlineResponse20010, dict):
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
        if not isinstance(other, InlineResponse20010):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
