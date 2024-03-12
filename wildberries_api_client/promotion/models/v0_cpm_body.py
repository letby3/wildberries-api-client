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

class V0CpmBody(object):
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
        'type': 'int',
        'cpm': 'int',
        'param': 'int',
        'instrument': 'int'
    }

    attribute_map = {
        'advert_id': 'advertId',
        'type': 'type',
        'cpm': 'cpm',
        'param': 'param',
        'instrument': 'instrument'
    }

    def __init__(self, advert_id=None, type=None, cpm=None, param=None, instrument=None):  # noqa: E501
        """V0CpmBody - a model defined in Swagger"""  # noqa: E501
        self._advert_id = None
        self._type = None
        self._cpm = None
        self._param = None
        self._instrument = None
        self.discriminator = None
        self.advert_id = advert_id
        self.type = type
        self.cpm = cpm
        self.param = param
        if instrument is not None:
            self.instrument = instrument

    @property
    def advert_id(self):
        """Gets the advert_id of this V0CpmBody.  # noqa: E501

        Identifikator kampanii, gde menaetsa stavka  # noqa: E501

        :return: The advert_id of this V0CpmBody.  # noqa: E501
        :rtype: int
        """
        return self._advert_id

    @advert_id.setter
    def advert_id(self, advert_id):
        """Sets the advert_id of this V0CpmBody.

        Identifikator kampanii, gde menaetsa stavka  # noqa: E501

        :param advert_id: The advert_id of this V0CpmBody.  # noqa: E501
        :type: int
        """
        if advert_id is None:
            raise ValueError("Invalid value for `advert_id`, must not be `None`")  # noqa: E501

        self._advert_id = advert_id

    @property
    def type(self):
        """Gets the type of this V0CpmBody.  # noqa: E501

        <dl> <dt>kampanii, gde menaetsa stavka:</dt> <dd><code>4</code> - kampania v kataloge </dd>  <dd><code>5</code> - kampania v kartohke tovara</dd> <dd><code>6</code> - kampania v poiske</dd> <dd><code>7</code> - kampania v rekomendaciah na glavnoi stranice</dd> <dd><code>8</code> - avtomatiheskaa kampania</dd> <dd><code>9</code> - kampania poisk + katalog </dd> </dl>   # noqa: E501

        :return: The type of this V0CpmBody.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V0CpmBody.

        <dl> <dt>kampanii, gde menaetsa stavka:</dt> <dd><code>4</code> - kampania v kataloge </dd>  <dd><code>5</code> - kampania v kartohke tovara</dd> <dd><code>6</code> - kampania v poiske</dd> <dd><code>7</code> - kampania v rekomendaciah na glavnoi stranice</dd> <dd><code>8</code> - avtomatiheskaa kampania</dd> <dd><code>9</code> - kampania poisk + katalog </dd> </dl>   # noqa: E501

        :param type: The type of this V0CpmBody.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = [5, 6, 7, 8, 9]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def cpm(self):
        """Gets the cpm of this V0CpmBody.  # noqa: E501

        Novoe znahenie stavki  # noqa: E501

        :return: The cpm of this V0CpmBody.  # noqa: E501
        :rtype: int
        """
        return self._cpm

    @cpm.setter
    def cpm(self, cpm):
        """Sets the cpm of this V0CpmBody.

        Novoe znahenie stavki  # noqa: E501

        :param cpm: The cpm of this V0CpmBody.  # noqa: E501
        :type: int
        """
        if cpm is None:
            raise ValueError("Invalid value for `cpm`, must not be `None`")  # noqa: E501

        self._cpm = cpm

    @property
    def param(self):
        """Gets the param of this V0CpmBody.  # noqa: E501

        Parametr, dla kotorogo budet vneseno izmenenie. avlaetsa znaheniem `subjectId` (dla kampanii v poiske i rekomendaciah), `setId` (dla kampanii v kartohke tovara) ili `menuId` (dla kampanii v kataloge).  <br> Dla avtomatiheskoi kampanii ukazyvat etot parametr ne trebuetsa.   # noqa: E501

        :return: The param of this V0CpmBody.  # noqa: E501
        :rtype: int
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this V0CpmBody.

        Parametr, dla kotorogo budet vneseno izmenenie. avlaetsa znaheniem `subjectId` (dla kampanii v poiske i rekomendaciah), `setId` (dla kampanii v kartohke tovara) ili `menuId` (dla kampanii v kataloge).  <br> Dla avtomatiheskoi kampanii ukazyvat etot parametr ne trebuetsa.   # noqa: E501

        :param param: The param of this V0CpmBody.  # noqa: E501
        :type: int
        """
        if param is None:
            raise ValueError("Invalid value for `param`, must not be `None`")  # noqa: E501

        self._param = param

    @property
    def instrument(self):
        """Gets the instrument of this V0CpmBody.  # noqa: E501

        tip kampanii dla izmenenia stavki v Poisk + Katalog (4 - katalog, 6 - poisk)  # noqa: E501

        :return: The instrument of this V0CpmBody.  # noqa: E501
        :rtype: int
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this V0CpmBody.

        tip kampanii dla izmenenia stavki v Poisk + Katalog (4 - katalog, 6 - poisk)  # noqa: E501

        :param instrument: The instrument of this V0CpmBody.  # noqa: E501
        :type: int
        """

        self._instrument = instrument

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
        if issubclass(V0CpmBody, dict):
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
        if not isinstance(other, V0CpmBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
