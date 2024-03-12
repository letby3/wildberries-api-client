# coding: utf-8

"""
    Tarify

    <p>Tarify na logistiku i hranenie na sklade. Tarify mohno poluhit s lubym tokenom, u kotorogo ne vybrana opcia Testovyi kontur.</p>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ModelsWarehouseBoxRates(object):
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
        'box_delivery_and_storage_expr': 'str',
        'box_delivery_base': 'str',
        'box_delivery_liter': 'str',
        'box_storage_base': 'str',
        'box_storage_liter': 'str',
        'warehouse_name': 'str'
    }

    attribute_map = {
        'box_delivery_and_storage_expr': 'boxDeliveryAndStorageExpr',
        'box_delivery_base': 'boxDeliveryBase',
        'box_delivery_liter': 'boxDeliveryLiter',
        'box_storage_base': 'boxStorageBase',
        'box_storage_liter': 'boxStorageLiter',
        'warehouse_name': 'warehouseName'
    }

    def __init__(self, box_delivery_and_storage_expr=None, box_delivery_base=None, box_delivery_liter=None, box_storage_base=None, box_storage_liter=None, warehouse_name=None):  # noqa: E501
        """ModelsWarehouseBoxRates - a model defined in Swagger"""  # noqa: E501
        self._box_delivery_and_storage_expr = None
        self._box_delivery_base = None
        self._box_delivery_liter = None
        self._box_storage_base = None
        self._box_storage_liter = None
        self._warehouse_name = None
        self.discriminator = None
        if box_delivery_and_storage_expr is not None:
            self.box_delivery_and_storage_expr = box_delivery_and_storage_expr
        if box_delivery_base is not None:
            self.box_delivery_base = box_delivery_base
        if box_delivery_liter is not None:
            self.box_delivery_liter = box_delivery_liter
        if box_storage_base is not None:
            self.box_storage_base = box_storage_base
        if box_storage_liter is not None:
            self.box_storage_liter = box_storage_liter
        if warehouse_name is not None:
            self.warehouse_name = warehouse_name

    @property
    def box_delivery_and_storage_expr(self):
        """Gets the box_delivery_and_storage_expr of this ModelsWarehouseBoxRates.  # noqa: E501

        Koefficient, %. Na nego umnohaetsa stoimost dostavki i hranenia. Vo vseh tarifah etot koefficient uhe uhten  # noqa: E501

        :return: The box_delivery_and_storage_expr of this ModelsWarehouseBoxRates.  # noqa: E501
        :rtype: str
        """
        return self._box_delivery_and_storage_expr

    @box_delivery_and_storage_expr.setter
    def box_delivery_and_storage_expr(self, box_delivery_and_storage_expr):
        """Sets the box_delivery_and_storage_expr of this ModelsWarehouseBoxRates.

        Koefficient, %. Na nego umnohaetsa stoimost dostavki i hranenia. Vo vseh tarifah etot koefficient uhe uhten  # noqa: E501

        :param box_delivery_and_storage_expr: The box_delivery_and_storage_expr of this ModelsWarehouseBoxRates.  # noqa: E501
        :type: str
        """

        self._box_delivery_and_storage_expr = box_delivery_and_storage_expr

    @property
    def box_delivery_base(self):
        """Gets the box_delivery_base of this ModelsWarehouseBoxRates.  # noqa: E501

        Dostavka 1 litra, ₽  # noqa: E501

        :return: The box_delivery_base of this ModelsWarehouseBoxRates.  # noqa: E501
        :rtype: str
        """
        return self._box_delivery_base

    @box_delivery_base.setter
    def box_delivery_base(self, box_delivery_base):
        """Sets the box_delivery_base of this ModelsWarehouseBoxRates.

        Dostavka 1 litra, ₽  # noqa: E501

        :param box_delivery_base: The box_delivery_base of this ModelsWarehouseBoxRates.  # noqa: E501
        :type: str
        """

        self._box_delivery_base = box_delivery_base

    @property
    def box_delivery_liter(self):
        """Gets the box_delivery_liter of this ModelsWarehouseBoxRates.  # noqa: E501

        Dostavka kahdogo dopolnitelnogo litra, ₽  # noqa: E501

        :return: The box_delivery_liter of this ModelsWarehouseBoxRates.  # noqa: E501
        :rtype: str
        """
        return self._box_delivery_liter

    @box_delivery_liter.setter
    def box_delivery_liter(self, box_delivery_liter):
        """Sets the box_delivery_liter of this ModelsWarehouseBoxRates.

        Dostavka kahdogo dopolnitelnogo litra, ₽  # noqa: E501

        :param box_delivery_liter: The box_delivery_liter of this ModelsWarehouseBoxRates.  # noqa: E501
        :type: str
        """

        self._box_delivery_liter = box_delivery_liter

    @property
    def box_storage_base(self):
        """Gets the box_storage_base of this ModelsWarehouseBoxRates.  # noqa: E501

        hranenie 1 litra, ₽  # noqa: E501

        :return: The box_storage_base of this ModelsWarehouseBoxRates.  # noqa: E501
        :rtype: str
        """
        return self._box_storage_base

    @box_storage_base.setter
    def box_storage_base(self, box_storage_base):
        """Sets the box_storage_base of this ModelsWarehouseBoxRates.

        hranenie 1 litra, ₽  # noqa: E501

        :param box_storage_base: The box_storage_base of this ModelsWarehouseBoxRates.  # noqa: E501
        :type: str
        """

        self._box_storage_base = box_storage_base

    @property
    def box_storage_liter(self):
        """Gets the box_storage_liter of this ModelsWarehouseBoxRates.  # noqa: E501

        hranenie kahdogo dopolnitelnogo litra, ₽  # noqa: E501

        :return: The box_storage_liter of this ModelsWarehouseBoxRates.  # noqa: E501
        :rtype: str
        """
        return self._box_storage_liter

    @box_storage_liter.setter
    def box_storage_liter(self, box_storage_liter):
        """Sets the box_storage_liter of this ModelsWarehouseBoxRates.

        hranenie kahdogo dopolnitelnogo litra, ₽  # noqa: E501

        :param box_storage_liter: The box_storage_liter of this ModelsWarehouseBoxRates.  # noqa: E501
        :type: str
        """

        self._box_storage_liter = box_storage_liter

    @property
    def warehouse_name(self):
        """Gets the warehouse_name of this ModelsWarehouseBoxRates.  # noqa: E501

        Nazvanie sklada  # noqa: E501

        :return: The warehouse_name of this ModelsWarehouseBoxRates.  # noqa: E501
        :rtype: str
        """
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, warehouse_name):
        """Sets the warehouse_name of this ModelsWarehouseBoxRates.

        Nazvanie sklada  # noqa: E501

        :param warehouse_name: The warehouse_name of this ModelsWarehouseBoxRates.  # noqa: E501
        :type: str
        """

        self._warehouse_name = warehouse_name

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
        if issubclass(ModelsWarehouseBoxRates, dict):
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
        if not isinstance(other, ModelsWarehouseBoxRates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other