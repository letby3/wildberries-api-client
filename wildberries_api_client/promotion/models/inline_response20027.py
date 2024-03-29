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

class InlineResponse20027(object):
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
        'name': 'object',
        'subject': 'Advv1searchsupplierproductsSubject',
        'brand': 'str',
        'kind': 'Advv1searchsupplierproductsKind'
    }

    attribute_map = {
        'nm': 'nm',
        'name': 'name',
        'subject': 'subject',
        'brand': 'brand',
        'kind': 'kind'
    }

    def __init__(self, nm=None, name=None, subject=None, brand=None, kind=None):  # noqa: E501
        """InlineResponse20027 - a model defined in Swagger"""  # noqa: E501
        self._nm = None
        self._name = None
        self._subject = None
        self._brand = None
        self._kind = None
        self.discriminator = None
        if nm is not None:
            self.nm = nm
        if name is not None:
            self.name = name
        if subject is not None:
            self.subject = subject
        if brand is not None:
            self.brand = brand
        if kind is not None:
            self.kind = kind

    @property
    def nm(self):
        """Gets the nm of this InlineResponse20027.  # noqa: E501

        Artikul WB.  # noqa: E501

        :return: The nm of this InlineResponse20027.  # noqa: E501
        :rtype: int
        """
        return self._nm

    @nm.setter
    def nm(self, nm):
        """Sets the nm of this InlineResponse20027.

        Artikul WB.  # noqa: E501

        :param nm: The nm of this InlineResponse20027.  # noqa: E501
        :type: int
        """

        self._nm = nm

    @property
    def name(self):
        """Gets the name of this InlineResponse20027.  # noqa: E501

        Naimenovanie tovara.  # noqa: E501

        :return: The name of this InlineResponse20027.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20027.

        Naimenovanie tovara.  # noqa: E501

        :param name: The name of this InlineResponse20027.  # noqa: E501
        :type: object
        """

        self._name = name

    @property
    def subject(self):
        """Gets the subject of this InlineResponse20027.  # noqa: E501


        :return: The subject of this InlineResponse20027.  # noqa: E501
        :rtype: Advv1searchsupplierproductsSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this InlineResponse20027.


        :param subject: The subject of this InlineResponse20027.  # noqa: E501
        :type: Advv1searchsupplierproductsSubject
        """

        self._subject = subject

    @property
    def brand(self):
        """Gets the brand of this InlineResponse20027.  # noqa: E501

        Brend.  # noqa: E501

        :return: The brand of this InlineResponse20027.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this InlineResponse20027.

        Brend.  # noqa: E501

        :param brand: The brand of this InlineResponse20027.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def kind(self):
        """Gets the kind of this InlineResponse20027.  # noqa: E501


        :return: The kind of this InlineResponse20027.  # noqa: E501
        :rtype: Advv1searchsupplierproductsKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this InlineResponse20027.


        :param kind: The kind of this InlineResponse20027.  # noqa: E501
        :type: Advv1searchsupplierproductsKind
        """

        self._kind = kind

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
        if issubclass(InlineResponse20027, dict):
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
        if not isinstance(other, InlineResponse20027):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
