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

class SeacatSaveadBody(object):
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
        'campaign_name': 'str',
        'nms': 'list[int]'
    }

    attribute_map = {
        'campaign_name': 'campaignName',
        'nms': 'nms'
    }

    def __init__(self, campaign_name=None, nms=None):  # noqa: E501
        """SeacatSaveadBody - a model defined in Swagger"""  # noqa: E501
        self._campaign_name = None
        self._nms = None
        self.discriminator = None
        if campaign_name is not None:
            self.campaign_name = campaign_name
        self.nms = nms

    @property
    def campaign_name(self):
        """Gets the campaign_name of this SeacatSaveadBody.  # noqa: E501

        Nazvanie kampanii  # noqa: E501

        :return: The campaign_name of this SeacatSaveadBody.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this SeacatSaveadBody.

        Nazvanie kampanii  # noqa: E501

        :param campaign_name: The campaign_name of this SeacatSaveadBody.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def nms(self):
        """Gets the nms of this SeacatSaveadBody.  # noqa: E501

        Nomenklatury dla kampanii. Dostupnye nomenklatury mohno poluhit s pomohu metoda [Nomenklatury dla kampanii](./#tag/Slovari/paths/~1adv~1v2~1supplier~1nms/post). Maksimum 50 tovarov (`nm`)   # noqa: E501

        :return: The nms of this SeacatSaveadBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._nms

    @nms.setter
    def nms(self, nms):
        """Sets the nms of this SeacatSaveadBody.

        Nomenklatury dla kampanii. Dostupnye nomenklatury mohno poluhit s pomohu metoda [Nomenklatury dla kampanii](./#tag/Slovari/paths/~1adv~1v2~1supplier~1nms/post). Maksimum 50 tovarov (`nm`)   # noqa: E501

        :param nms: The nms of this SeacatSaveadBody.  # noqa: E501
        :type: list[int]
        """
        if nms is None:
            raise ValueError("Invalid value for `nms`, must not be `None`")  # noqa: E501

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
        if issubclass(SeacatSaveadBody, dict):
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
        if not isinstance(other, SeacatSaveadBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
