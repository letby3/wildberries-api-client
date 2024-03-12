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

class ResponseInfoAdvertType8AutoParams(object):
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
        'subject': 'ResponseInfoAdvertType8AutoParamsSubject',
        'sets': 'list[ResponseInfoAdvertType8AutoParamsSets]',
        'menus': 'list[ResponseInfoAdvertType8AutoParamsMenus]',
        'active': 'ResponseInfoAdvertType8AutoParamsActive',
        'nms': 'list[int]',
        'cpm': 'int'
    }

    attribute_map = {
        'subject': 'subject',
        'sets': 'sets',
        'menus': 'menus',
        'active': 'active',
        'nms': 'nms',
        'cpm': 'cpm'
    }

    def __init__(self, subject=None, sets=None, menus=None, active=None, nms=None, cpm=None):  # noqa: E501
        """ResponseInfoAdvertType8AutoParams - a model defined in Swagger"""  # noqa: E501
        self._subject = None
        self._sets = None
        self._menus = None
        self._active = None
        self._nms = None
        self._cpm = None
        self.discriminator = None
        if subject is not None:
            self.subject = subject
        if sets is not None:
            self.sets = sets
        if menus is not None:
            self.menus = menus
        if active is not None:
            self.active = active
        if nms is not None:
            self.nms = nms
        if cpm is not None:
            self.cpm = cpm

    @property
    def subject(self):
        """Gets the subject of this ResponseInfoAdvertType8AutoParams.  # noqa: E501


        :return: The subject of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :rtype: ResponseInfoAdvertType8AutoParamsSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ResponseInfoAdvertType8AutoParams.


        :param subject: The subject of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :type: ResponseInfoAdvertType8AutoParamsSubject
        """

        self._subject = subject

    @property
    def sets(self):
        """Gets the sets of this ResponseInfoAdvertType8AutoParams.  # noqa: E501

        Vnutrennaa (sistemnaa) suhnost (pol + predmet)  # noqa: E501

        :return: The sets of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :rtype: list[ResponseInfoAdvertType8AutoParamsSets]
        """
        return self._sets

    @sets.setter
    def sets(self, sets):
        """Sets the sets of this ResponseInfoAdvertType8AutoParams.

        Vnutrennaa (sistemnaa) suhnost (pol + predmet)  # noqa: E501

        :param sets: The sets of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :type: list[ResponseInfoAdvertType8AutoParamsSets]
        """

        self._sets = sets

    @property
    def menus(self):
        """Gets the menus of this ResponseInfoAdvertType8AutoParams.  # noqa: E501


        :return: The menus of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :rtype: list[ResponseInfoAdvertType8AutoParamsMenus]
        """
        return self._menus

    @menus.setter
    def menus(self, menus):
        """Sets the menus of this ResponseInfoAdvertType8AutoParams.


        :param menus: The menus of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :type: list[ResponseInfoAdvertType8AutoParamsMenus]
        """

        self._menus = menus

    @property
    def active(self):
        """Gets the active of this ResponseInfoAdvertType8AutoParams.  # noqa: E501


        :return: The active of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :rtype: ResponseInfoAdvertType8AutoParamsActive
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ResponseInfoAdvertType8AutoParams.


        :param active: The active of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :type: ResponseInfoAdvertType8AutoParamsActive
        """

        self._active = active

    @property
    def nms(self):
        """Gets the nms of this ResponseInfoAdvertType8AutoParams.  # noqa: E501

        Artikuly WB  # noqa: E501

        :return: The nms of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._nms

    @nms.setter
    def nms(self, nms):
        """Sets the nms of this ResponseInfoAdvertType8AutoParams.

        Artikuly WB  # noqa: E501

        :param nms: The nms of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :type: list[int]
        """

        self._nms = nms

    @property
    def cpm(self):
        """Gets the cpm of this ResponseInfoAdvertType8AutoParams.  # noqa: E501

        Stavka (Otobrahaetsa tolko pri nalihii)  # noqa: E501

        :return: The cpm of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :rtype: int
        """
        return self._cpm

    @cpm.setter
    def cpm(self, cpm):
        """Sets the cpm of this ResponseInfoAdvertType8AutoParams.

        Stavka (Otobrahaetsa tolko pri nalihii)  # noqa: E501

        :param cpm: The cpm of this ResponseInfoAdvertType8AutoParams.  # noqa: E501
        :type: int
        """

        self._cpm = cpm

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
        if issubclass(ResponseInfoAdvertType8AutoParams, dict):
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
        if not isinstance(other, ResponseInfoAdvertType8AutoParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
