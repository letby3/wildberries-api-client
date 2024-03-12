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

class NomenclatureLinkBody(object):
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
        'nm_id': 'int',
        'tags_i_ds': 'list[int]'
    }

    attribute_map = {
        'nm_id': 'nmID',
        'tags_i_ds': 'tagsIDs'
    }

    def __init__(self, nm_id=None, tags_i_ds=None):  # noqa: E501
        """NomenclatureLinkBody - a model defined in Swagger"""  # noqa: E501
        self._nm_id = None
        self._tags_i_ds = None
        self.discriminator = None
        if nm_id is not None:
            self.nm_id = nm_id
        if tags_i_ds is not None:
            self.tags_i_ds = tags_i_ds

    @property
    def nm_id(self):
        """Gets the nm_id of this NomenclatureLinkBody.  # noqa: E501

        Artikul WB  # noqa: E501

        :return: The nm_id of this NomenclatureLinkBody.  # noqa: E501
        :rtype: int
        """
        return self._nm_id

    @nm_id.setter
    def nm_id(self, nm_id):
        """Sets the nm_id of this NomenclatureLinkBody.

        Artikul WB  # noqa: E501

        :param nm_id: The nm_id of this NomenclatureLinkBody.  # noqa: E501
        :type: int
        """

        self._nm_id = nm_id

    @property
    def tags_i_ds(self):
        """Gets the tags_i_ds of this NomenclatureLinkBody.  # noqa: E501

        Massiv hislovyh identifikatorov tegov.<br>   hto by snat tegi s KT, neobhodimo peredat pustoi massiv.<br> htoby dobavit tegi k uhe imeuhimsa v KT, neobhodimo v zaprose peredat novye tegi i tegi, kotorye uhe est v KT.   # noqa: E501

        :return: The tags_i_ds of this NomenclatureLinkBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._tags_i_ds

    @tags_i_ds.setter
    def tags_i_ds(self, tags_i_ds):
        """Sets the tags_i_ds of this NomenclatureLinkBody.

        Massiv hislovyh identifikatorov tegov.<br>   hto by snat tegi s KT, neobhodimo peredat pustoi massiv.<br> htoby dobavit tegi k uhe imeuhimsa v KT, neobhodimo v zaprose peredat novye tegi i tegi, kotorye uhe est v KT.   # noqa: E501

        :param tags_i_ds: The tags_i_ds of this NomenclatureLinkBody.  # noqa: E501
        :type: list[int]
        """

        self._tags_i_ds = tags_i_ds

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
        if issubclass(NomenclatureLinkBody, dict):
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
        if not isinstance(other, NomenclatureLinkBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other