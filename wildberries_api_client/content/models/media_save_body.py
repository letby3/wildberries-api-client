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

class MediaSaveBody(object):
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
        'nm_id': 'str',
        'data': 'list[str]'
    }

    attribute_map = {
        'nm_id': 'nmID',
        'data': 'data'
    }

    def __init__(self, nm_id=None, data=None):  # noqa: E501
        """MediaSaveBody - a model defined in Swagger"""  # noqa: E501
        self._nm_id = None
        self._data = None
        self.discriminator = None
        if nm_id is not None:
            self.nm_id = nm_id
        if data is not None:
            self.data = data

    @property
    def nm_id(self):
        """Gets the nm_id of this MediaSaveBody.  # noqa: E501

        Artikul Wildberries  # noqa: E501

        :return: The nm_id of this MediaSaveBody.  # noqa: E501
        :rtype: str
        """
        return self._nm_id

    @nm_id.setter
    def nm_id(self, nm_id):
        """Sets the nm_id of this MediaSaveBody.

        Artikul Wildberries  # noqa: E501

        :param nm_id: The nm_id of this MediaSaveBody.  # noqa: E501
        :type: str
        """

        self._nm_id = nm_id

    @property
    def data(self):
        """Gets the data of this MediaSaveBody.  # noqa: E501

        Ssylki na izobrahenia v tom poradke, v kotorom oni budut na kartohke tovara  # noqa: E501

        :return: The data of this MediaSaveBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MediaSaveBody.

        Ssylki na izobrahenia v tom poradke, v kotorom oni budut na kartohke tovara  # noqa: E501

        :param data: The data of this MediaSaveBody.  # noqa: E501
        :type: list[str]
        """

        self._data = data

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
        if issubclass(MediaSaveBody, dict):
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
        if not isinstance(other, MediaSaveBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
