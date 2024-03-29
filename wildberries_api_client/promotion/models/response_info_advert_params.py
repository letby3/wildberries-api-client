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

class ResponseInfoAdvertParams(object):
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
        'subject_name': 'str',
        'active': 'bool',
        'intervals': 'list[ResponseInfoAdvertIntervals]',
        'price': 'int',
        'menu_id': 'int',
        'subject_id': 'int',
        'set_id': 'int',
        'set_name': 'str',
        'menu_name': 'str',
        'nms': 'list[ResponseInfoAdvertNms]'
    }

    attribute_map = {
        'subject_name': 'subjectName',
        'active': 'active',
        'intervals': 'intervals',
        'price': 'price',
        'menu_id': 'menuId',
        'subject_id': 'subjectId',
        'set_id': 'setId',
        'set_name': 'setName',
        'menu_name': 'menuName',
        'nms': 'nms'
    }

    def __init__(self, subject_name=None, active=None, intervals=None, price=None, menu_id=None, subject_id=None, set_id=None, set_name=None, menu_name=None, nms=None):  # noqa: E501
        """ResponseInfoAdvertParams - a model defined in Swagger"""  # noqa: E501
        self._subject_name = None
        self._active = None
        self._intervals = None
        self._price = None
        self._menu_id = None
        self._subject_id = None
        self._set_id = None
        self._set_name = None
        self._menu_name = None
        self._nms = None
        self.discriminator = None
        if subject_name is not None:
            self.subject_name = subject_name
        if active is not None:
            self.active = active
        if intervals is not None:
            self.intervals = intervals
        if price is not None:
            self.price = price
        if menu_id is not None:
            self.menu_id = menu_id
        if subject_id is not None:
            self.subject_id = subject_id
        if set_id is not None:
            self.set_id = set_id
        if set_name is not None:
            self.set_name = set_name
        if menu_name is not None:
            self.menu_name = menu_name
        if nms is not None:
            self.nms = nms

    @property
    def subject_name(self):
        """Gets the subject_name of this ResponseInfoAdvertParams.  # noqa: E501

        Nazvanie predmetnoi gruppy (dla kampanii v poiske i rekomendaciah)  # noqa: E501

        :return: The subject_name of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: str
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        """Sets the subject_name of this ResponseInfoAdvertParams.

        Nazvanie predmetnoi gruppy (dla kampanii v poiske i rekomendaciah)  # noqa: E501

        :param subject_name: The subject_name of this ResponseInfoAdvertParams.  # noqa: E501
        :type: str
        """

        self._subject_name = subject_name

    @property
    def active(self):
        """Gets the active of this ResponseInfoAdvertParams.  # noqa: E501

        Flag aktivnosti predmetnoi gruppy, <code>true</code> - aktivna, <code>false</code> - neaktivna  # noqa: E501

        :return: The active of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ResponseInfoAdvertParams.

        Flag aktivnosti predmetnoi gruppy, <code>true</code> - aktivna, <code>false</code> - neaktivna  # noqa: E501

        :param active: The active of this ResponseInfoAdvertParams.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def intervals(self):
        """Gets the intervals of this ResponseInfoAdvertParams.  # noqa: E501

        Intervaly hasov pokaza kampanii  # noqa: E501

        :return: The intervals of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: list[ResponseInfoAdvertIntervals]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """Sets the intervals of this ResponseInfoAdvertParams.

        Intervaly hasov pokaza kampanii  # noqa: E501

        :param intervals: The intervals of this ResponseInfoAdvertParams.  # noqa: E501
        :type: list[ResponseInfoAdvertIntervals]
        """

        self._intervals = intervals

    @property
    def price(self):
        """Gets the price of this ResponseInfoAdvertParams.  # noqa: E501

        Tekuhaa stavka  # noqa: E501

        :return: The price of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ResponseInfoAdvertParams.

        Tekuhaa stavka  # noqa: E501

        :param price: The price of this ResponseInfoAdvertParams.  # noqa: E501
        :type: int
        """

        self._price = price

    @property
    def menu_id(self):
        """Gets the menu_id of this ResponseInfoAdvertParams.  # noqa: E501

        Identifikator menu, gde razmehaetsa kampania (dla kampanii v kataloge)  # noqa: E501

        :return: The menu_id of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: int
        """
        return self._menu_id

    @menu_id.setter
    def menu_id(self, menu_id):
        """Sets the menu_id of this ResponseInfoAdvertParams.

        Identifikator menu, gde razmehaetsa kampania (dla kampanii v kataloge)  # noqa: E501

        :param menu_id: The menu_id of this ResponseInfoAdvertParams.  # noqa: E501
        :type: int
        """

        self._menu_id = menu_id

    @property
    def subject_id(self):
        """Gets the subject_id of this ResponseInfoAdvertParams.  # noqa: E501

        Identifikator predmetnoi gruppy, dla kotoroi sozdana kampania (dla kampanii v poiske i rekomendaciah)  # noqa: E501

        :return: The subject_id of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this ResponseInfoAdvertParams.

        Identifikator predmetnoi gruppy, dla kotoroi sozdana kampania (dla kampanii v poiske i rekomendaciah)  # noqa: E501

        :param subject_id: The subject_id of this ResponseInfoAdvertParams.  # noqa: E501
        :type: int
        """

        self._subject_id = subject_id

    @property
    def set_id(self):
        """Gets the set_id of this ResponseInfoAdvertParams.  # noqa: E501

        Identifikator sohetania predmeta i pola (dla kampanii v kartohke tovara)  # noqa: E501

        :return: The set_id of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: int
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this ResponseInfoAdvertParams.

        Identifikator sohetania predmeta i pola (dla kampanii v kartohke tovara)  # noqa: E501

        :param set_id: The set_id of this ResponseInfoAdvertParams.  # noqa: E501
        :type: int
        """

        self._set_id = set_id

    @property
    def set_name(self):
        """Gets the set_name of this ResponseInfoAdvertParams.  # noqa: E501

        Sohetanie predmeta i pola (dla kampanii v kartohke tovara)  # noqa: E501

        :return: The set_name of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: str
        """
        return self._set_name

    @set_name.setter
    def set_name(self, set_name):
        """Sets the set_name of this ResponseInfoAdvertParams.

        Sohetanie predmeta i pola (dla kampanii v kartohke tovara)  # noqa: E501

        :param set_name: The set_name of this ResponseInfoAdvertParams.  # noqa: E501
        :type: str
        """

        self._set_name = set_name

    @property
    def menu_name(self):
        """Gets the menu_name of this ResponseInfoAdvertParams.  # noqa: E501

        Nazvanie menu, gde razmehaetsa kampania (dla kampanii v kataloge)  # noqa: E501

        :return: The menu_name of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: str
        """
        return self._menu_name

    @menu_name.setter
    def menu_name(self, menu_name):
        """Sets the menu_name of this ResponseInfoAdvertParams.

        Nazvanie menu, gde razmehaetsa kampania (dla kampanii v kataloge)  # noqa: E501

        :param menu_name: The menu_name of this ResponseInfoAdvertParams.  # noqa: E501
        :type: str
        """

        self._menu_name = menu_name

    @property
    def nms(self):
        """Gets the nms of this ResponseInfoAdvertParams.  # noqa: E501

        Massiv nomenklatur kampanii  # noqa: E501

        :return: The nms of this ResponseInfoAdvertParams.  # noqa: E501
        :rtype: list[ResponseInfoAdvertNms]
        """
        return self._nms

    @nms.setter
    def nms(self, nms):
        """Sets the nms of this ResponseInfoAdvertParams.

        Massiv nomenklatur kampanii  # noqa: E501

        :param nms: The nms of this ResponseInfoAdvertParams.  # noqa: E501
        :type: list[ResponseInfoAdvertNms]
        """

        self._nms = nms

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
        if issubclass(ResponseInfoAdvertParams, dict):
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
        if not isinstance(other, ResponseInfoAdvertParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
