# coding: utf-8

"""
    Opisanie API Rekomendacii

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V1DelBody(object):
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
        'nm': 'int',
        'recom': 'list[int]'
    }

    attribute_map = {
        'nm': 'nm',
        'recom': 'recom'
    }

    def __init__(self, nm=None, recom=None):  # noqa: E501
        """V1DelBody - a model defined in Swagger"""  # noqa: E501
        self._nm = None
        self._recom = None
        self.discriminator = None
        self.nm = nm
        self.recom = recom

    @property
    def nm(self):
        """Gets the nm of this V1DelBody.  # noqa: E501

        Identifikator tovara (`nmId`), u kotorogo neobhodimo udalit rekomendaciu  # noqa: E501

        :return: The nm of this V1DelBody.  # noqa: E501
        :rtype: int
        """
        return self._nm

    @nm.setter
    def nm(self, nm):
        """Sets the nm of this V1DelBody.

        Identifikator tovara (`nmId`), u kotorogo neobhodimo udalit rekomendaciu  # noqa: E501

        :param nm: The nm of this V1DelBody.  # noqa: E501
        :type: int
        """
        if nm is None:
            raise ValueError("Invalid value for `nm`, must not be `None`")  # noqa: E501

        self._nm = nm

    @property
    def recom(self):
        """Gets the recom of this V1DelBody.  # noqa: E501

        Spisok identifikatorov tovarov (`nmId`), kotorye neobhodimo udalit iz rekomenduemyh  # noqa: E501

        :return: The recom of this V1DelBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._recom

    @recom.setter
    def recom(self, recom):
        """Sets the recom of this V1DelBody.

        Spisok identifikatorov tovarov (`nmId`), kotorye neobhodimo udalit iz rekomenduemyh  # noqa: E501

        :param recom: The recom of this V1DelBody.  # noqa: E501
        :type: list[int]
        """
        if recom is None:
            raise ValueError("Invalid value for `recom`, must not be `None`")  # noqa: E501

        self._recom = recom

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
        if issubclass(V1DelBody, dict):
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
        if not isinstance(other, V1DelBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
