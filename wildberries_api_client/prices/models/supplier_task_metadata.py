# coding: utf-8

"""
    API cen i skidok

    S pomohu etih metodov mohno ustanavlivat ceny i skidki. Maksimum — 10 zaprosov za 6 sekund summarno dla vseh metodov.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SupplierTaskMetadata(object):
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
        'upload_id': 'int',
        'status': 'TaskStatus',
        'upload_date': 'ModelDate',
        'activation_date': 'Date1',
        'over_all_goods_number': 'int',
        'success_goods_number': 'int'
    }

    attribute_map = {
        'upload_id': 'uploadID',
        'status': 'status',
        'upload_date': 'uploadDate',
        'activation_date': 'activationDate',
        'over_all_goods_number': 'overAllGoodsNumber',
        'success_goods_number': 'successGoodsNumber'
    }

    def __init__(self, upload_id=None, status=None, upload_date=None, activation_date=None, over_all_goods_number=None, success_goods_number=None):  # noqa: E501
        """SupplierTaskMetadata - a model defined in Swagger"""  # noqa: E501
        self._upload_id = None
        self._status = None
        self._upload_date = None
        self._activation_date = None
        self._over_all_goods_number = None
        self._success_goods_number = None
        self.discriminator = None
        if upload_id is not None:
            self.upload_id = upload_id
        if status is not None:
            self.status = status
        if upload_date is not None:
            self.upload_date = upload_date
        if activation_date is not None:
            self.activation_date = activation_date
        if over_all_goods_number is not None:
            self.over_all_goods_number = over_all_goods_number
        if success_goods_number is not None:
            self.success_goods_number = success_goods_number

    @property
    def upload_id(self):
        """Gets the upload_id of this SupplierTaskMetadata.  # noqa: E501

        ID zagruzki  # noqa: E501

        :return: The upload_id of this SupplierTaskMetadata.  # noqa: E501
        :rtype: int
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this SupplierTaskMetadata.

        ID zagruzki  # noqa: E501

        :param upload_id: The upload_id of this SupplierTaskMetadata.  # noqa: E501
        :type: int
        """

        self._upload_id = upload_id

    @property
    def status(self):
        """Gets the status of this SupplierTaskMetadata.  # noqa: E501


        :return: The status of this SupplierTaskMetadata.  # noqa: E501
        :rtype: TaskStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SupplierTaskMetadata.


        :param status: The status of this SupplierTaskMetadata.  # noqa: E501
        :type: TaskStatus
        """

        self._status = status

    @property
    def upload_date(self):
        """Gets the upload_date of this SupplierTaskMetadata.  # noqa: E501


        :return: The upload_date of this SupplierTaskMetadata.  # noqa: E501
        :rtype: ModelDate
        """
        return self._upload_date

    @upload_date.setter
    def upload_date(self, upload_date):
        """Sets the upload_date of this SupplierTaskMetadata.


        :param upload_date: The upload_date of this SupplierTaskMetadata.  # noqa: E501
        :type: ModelDate
        """

        self._upload_date = upload_date

    @property
    def activation_date(self):
        """Gets the activation_date of this SupplierTaskMetadata.  # noqa: E501


        :return: The activation_date of this SupplierTaskMetadata.  # noqa: E501
        :rtype: Date1
        """
        return self._activation_date

    @activation_date.setter
    def activation_date(self, activation_date):
        """Sets the activation_date of this SupplierTaskMetadata.


        :param activation_date: The activation_date of this SupplierTaskMetadata.  # noqa: E501
        :type: Date1
        """

        self._activation_date = activation_date

    @property
    def over_all_goods_number(self):
        """Gets the over_all_goods_number of this SupplierTaskMetadata.  # noqa: E501

        Vsego tovarov  # noqa: E501

        :return: The over_all_goods_number of this SupplierTaskMetadata.  # noqa: E501
        :rtype: int
        """
        return self._over_all_goods_number

    @over_all_goods_number.setter
    def over_all_goods_number(self, over_all_goods_number):
        """Sets the over_all_goods_number of this SupplierTaskMetadata.

        Vsego tovarov  # noqa: E501

        :param over_all_goods_number: The over_all_goods_number of this SupplierTaskMetadata.  # noqa: E501
        :type: int
        """

        self._over_all_goods_number = over_all_goods_number

    @property
    def success_goods_number(self):
        """Gets the success_goods_number of this SupplierTaskMetadata.  # noqa: E501

        Tovarov bez ohibok  # noqa: E501

        :return: The success_goods_number of this SupplierTaskMetadata.  # noqa: E501
        :rtype: int
        """
        return self._success_goods_number

    @success_goods_number.setter
    def success_goods_number(self, success_goods_number):
        """Sets the success_goods_number of this SupplierTaskMetadata.

        Tovarov bez ohibok  # noqa: E501

        :param success_goods_number: The success_goods_number of this SupplierTaskMetadata.  # noqa: E501
        :type: int
        """

        self._success_goods_number = success_goods_number

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
        if issubclass(SupplierTaskMetadata, dict):
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
        if not isinstance(other, SupplierTaskMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
