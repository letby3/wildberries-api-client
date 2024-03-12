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

class V1SaveadBody(object):
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
        'name': 'str',
        'subject_id': 'int',
        'sum': 'int',
        'btype': 'int',
        'on_pause': 'bool',
        'nms': 'list[int]',
        'cpm': 'int'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'subject_id': 'subjectId',
        'sum': 'sum',
        'btype': 'btype',
        'on_pause': 'on_pause',
        'nms': 'nms',
        'cpm': 'cpm'
    }

    def __init__(self, type=None, name=None, subject_id=None, sum=None, btype=None, on_pause=None, nms=None, cpm=None):  # noqa: E501
        """V1SaveadBody - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._name = None
        self._subject_id = None
        self._sum = None
        self._btype = None
        self._on_pause = None
        self._nms = None
        self._cpm = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if subject_id is not None:
            self.subject_id = subject_id
        if sum is not None:
            self.sum = sum
        if btype is not None:
            self.btype = btype
        if on_pause is not None:
            self.on_pause = on_pause
        if nms is not None:
            self.nms = nms
        if cpm is not None:
            self.cpm = cpm

    @property
    def type(self):
        """Gets the type of this V1SaveadBody.  # noqa: E501

        <dl> <dt>Tip avtomatiheskoi kampanii:</dt> <dd><code>8</code> </dl>   # noqa: E501

        :return: The type of this V1SaveadBody.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1SaveadBody.

        <dl> <dt>Tip avtomatiheskoi kampanii:</dt> <dd><code>8</code> </dl>   # noqa: E501

        :param type: The type of this V1SaveadBody.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this V1SaveadBody.  # noqa: E501

        Nazvanie kampanii (max. 128 simvolov)  # noqa: E501

        :return: The name of this V1SaveadBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1SaveadBody.

        Nazvanie kampanii (max. 128 simvolov)  # noqa: E501

        :param name: The name of this V1SaveadBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def subject_id(self):
        """Gets the subject_id of this V1SaveadBody.  # noqa: E501

        ID predmeta, dla kotorogo sozdaetsa kampania.<br> Suhestvuuhie u prodavca identifikatory mohno poluhit metodom iz razdela \"Kontent / Prosmotr\" - \"Spisok NM\", pole otveta - `objectID`.   # noqa: E501

        :return: The subject_id of this V1SaveadBody.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this V1SaveadBody.

        ID predmeta, dla kotorogo sozdaetsa kampania.<br> Suhestvuuhie u prodavca identifikatory mohno poluhit metodom iz razdela \"Kontent / Prosmotr\" - \"Spisok NM\", pole otveta - `objectID`.   # noqa: E501

        :param subject_id: The subject_id of this V1SaveadBody.  # noqa: E501
        :type: int
        """

        self._subject_id = subject_id

    @property
    def sum(self):
        """Gets the sum of this V1SaveadBody.  # noqa: E501

        Summa popolnenia  # noqa: E501

        :return: The sum of this V1SaveadBody.  # noqa: E501
        :rtype: int
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this V1SaveadBody.

        Summa popolnenia  # noqa: E501

        :param sum: The sum of this V1SaveadBody.  # noqa: E501
        :type: int
        """

        self._sum = sum

    @property
    def btype(self):
        """Gets the btype of this V1SaveadBody.  # noqa: E501

        <dl> <dt>Tip spisania.</dt> <dd><code>0</code> - balance</dd> <dd><code>1</code> - net</dd> <dd><code>3</code> - bonus</dd> </dl>   # noqa: E501

        :return: The btype of this V1SaveadBody.  # noqa: E501
        :rtype: int
        """
        return self._btype

    @btype.setter
    def btype(self, btype):
        """Sets the btype of this V1SaveadBody.

        <dl> <dt>Tip spisania.</dt> <dd><code>0</code> - balance</dd> <dd><code>1</code> - net</dd> <dd><code>3</code> - bonus</dd> </dl>   # noqa: E501

        :param btype: The btype of this V1SaveadBody.  # noqa: E501
        :type: int
        """

        self._btype = btype

    @property
    def on_pause(self):
        """Gets the on_pause of this V1SaveadBody.  # noqa: E501

        <dl> <dt>Posle sozdania kampania:</dt>  <dd>   <dl>     <dt><code>true</code> - budet na pauze.</dt>     <dd>Zapusk kampanii budet dostupen herez 3 minuty posle sozdania kampanii.</dd>   </dl> </dd>  <dd><code>false</code> - budet srazu zapuhena</dd>  </dl>   # noqa: E501

        :return: The on_pause of this V1SaveadBody.  # noqa: E501
        :rtype: bool
        """
        return self._on_pause

    @on_pause.setter
    def on_pause(self, on_pause):
        """Sets the on_pause of this V1SaveadBody.

        <dl> <dt>Posle sozdania kampania:</dt>  <dd>   <dl>     <dt><code>true</code> - budet na pauze.</dt>     <dd>Zapusk kampanii budet dostupen herez 3 minuty posle sozdania kampanii.</dd>   </dl> </dd>  <dd><code>false</code> - budet srazu zapuhena</dd>  </dl>   # noqa: E501

        :param on_pause: The on_pause of this V1SaveadBody.  # noqa: E501
        :type: bool
        """

        self._on_pause = on_pause

    @property
    def nms(self):
        """Gets the nms of this V1SaveadBody.  # noqa: E501

        Massiv artikulov WB. <span class=\"new\">new</span><br> Maksimum 100 artikulov.    # noqa: E501

        :return: The nms of this V1SaveadBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._nms

    @nms.setter
    def nms(self, nms):
        """Sets the nms of this V1SaveadBody.

        Massiv artikulov WB. <span class=\"new\">new</span><br> Maksimum 100 artikulov.    # noqa: E501

        :param nms: The nms of this V1SaveadBody.  # noqa: E501
        :type: list[int]
        """

        self._nms = nms

    @property
    def cpm(self):
        """Gets the cpm of this V1SaveadBody.  # noqa: E501

        Stavka. <span class=\"new\">new</span><br> Esli budet ukazana stavka menhe dopustimogo razmera, to avtomatiheski ustanovitsa stavka minimalno dopustimogo razmera.   # noqa: E501

        :return: The cpm of this V1SaveadBody.  # noqa: E501
        :rtype: int
        """
        return self._cpm

    @cpm.setter
    def cpm(self, cpm):
        """Sets the cpm of this V1SaveadBody.

        Stavka. <span class=\"new\">new</span><br> Esli budet ukazana stavka menhe dopustimogo razmera, to avtomatiheski ustanovitsa stavka minimalno dopustimogo razmera.   # noqa: E501

        :param cpm: The cpm of this V1SaveadBody.  # noqa: E501
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
        if issubclass(V1SaveadBody, dict):
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
        if not isinstance(other, V1SaveadBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
