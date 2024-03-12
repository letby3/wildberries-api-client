# coding: utf-8

"""
    Opisanie API Kontenta

     <dl> <dt>Slovar sokrahenii:</dt> <dd>KT — kartohka tovara</dd> <dd>NM—- nomenklatura</dd> </dl> Ogranihenia po kolihestvu zaprosov: <dd>Dopuskaetsa maksimum 100 zaprosov v minutu na metody kontenta v celom.</dd> <br> Publihnoe API Kontenta sozdano dla sinhronizacii dannyh mehdu serverami Wildberries i serverami prodavcov. <br> Vy zagruhaete dannye na svoi nositeli, rabotaete s nimi na svoih mohnostah i sinhroniziruetes s nahimi serverami po mere neobhodimosti. <br> <code>Ne dopuskaetsa ispolzovanie API Kontenta v kahestve vnehnei bazy dannyh. Pri prevyhenii limitov na zaprosy dostup k API budet ogranihen.</code> <br> <br> <br>   # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UploadAddBody(object):
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
        'imt_id': 'int',
        'cards_to_add': 'list[Contentv2cardsuploadaddCardsToAdd]'
    }

    attribute_map = {
        'imt_id': 'imtID',
        'cards_to_add': 'cardsToAdd'
    }

    def __init__(self, imt_id=None, cards_to_add=None):  # noqa: E501
        """UploadAddBody - a model defined in Swagger"""  # noqa: E501
        self._imt_id = None
        self._cards_to_add = None
        self.discriminator = None
        if imt_id is not None:
            self.imt_id = imt_id
        if cards_to_add is not None:
            self.cards_to_add = cards_to_add

    @property
    def imt_id(self):
        """Gets the imt_id of this UploadAddBody.  # noqa: E501

        imtID KT, k kotoroi dobavlaetsa NM  # noqa: E501

        :return: The imt_id of this UploadAddBody.  # noqa: E501
        :rtype: int
        """
        return self._imt_id

    @imt_id.setter
    def imt_id(self, imt_id):
        """Sets the imt_id of this UploadAddBody.

        imtID KT, k kotoroi dobavlaetsa NM  # noqa: E501

        :param imt_id: The imt_id of this UploadAddBody.  # noqa: E501
        :type: int
        """

        self._imt_id = imt_id

    @property
    def cards_to_add(self):
        """Gets the cards_to_add of this UploadAddBody.  # noqa: E501

        Struktura dobavlaemoi NM  # noqa: E501

        :return: The cards_to_add of this UploadAddBody.  # noqa: E501
        :rtype: list[Contentv2cardsuploadaddCardsToAdd]
        """
        return self._cards_to_add

    @cards_to_add.setter
    def cards_to_add(self, cards_to_add):
        """Sets the cards_to_add of this UploadAddBody.

        Struktura dobavlaemoi NM  # noqa: E501

        :param cards_to_add: The cards_to_add of this UploadAddBody.  # noqa: E501
        :type: list[Contentv2cardsuploadaddCardsToAdd]
        """

        self._cards_to_add = cards_to_add

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
        if issubclass(UploadAddBody, dict):
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
        if not isinstance(other, UploadAddBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
