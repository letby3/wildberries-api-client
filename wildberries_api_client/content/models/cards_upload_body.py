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

class CardsUploadBody(object):
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
        'subject_id': 'int',
        'variants': 'list[Contentv2cardsuploadVariants]'
    }

    attribute_map = {
        'subject_id': 'subjectID',
        'variants': 'variants'
    }

    def __init__(self, subject_id=None, variants=None):  # noqa: E501
        """CardsUploadBody - a model defined in Swagger"""  # noqa: E501
        self._subject_id = None
        self._variants = None
        self.discriminator = None
        self.subject_id = subject_id
        self.variants = variants

    @property
    def subject_id(self):
        """Gets the subject_id of this CardsUploadBody.  # noqa: E501

        ID predmeta  # noqa: E501

        :return: The subject_id of this CardsUploadBody.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this CardsUploadBody.

        ID predmeta  # noqa: E501

        :param subject_id: The subject_id of this CardsUploadBody.  # noqa: E501
        :type: int
        """
        if subject_id is None:
            raise ValueError("Invalid value for `subject_id`, must not be `None`")  # noqa: E501

        self._subject_id = subject_id

    @property
    def variants(self):
        """Gets the variants of this CardsUploadBody.  # noqa: E501

        Massiv variantov tovara. V kahdoi KT mohet byt ne bolee 30 variantov (NM)  # noqa: E501

        :return: The variants of this CardsUploadBody.  # noqa: E501
        :rtype: list[Contentv2cardsuploadVariants]
        """
        return self._variants

    @variants.setter
    def variants(self, variants):
        """Sets the variants of this CardsUploadBody.

        Massiv variantov tovara. V kahdoi KT mohet byt ne bolee 30 variantov (NM)  # noqa: E501

        :param variants: The variants of this CardsUploadBody.  # noqa: E501
        :type: list[Contentv2cardsuploadVariants]
        """
        if variants is None:
            raise ValueError("Invalid value for `variants`, must not be `None`")  # noqa: E501

        self._variants = variants

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
        if issubclass(CardsUploadBody, dict):
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
        if not isinstance(other, CardsUploadBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other