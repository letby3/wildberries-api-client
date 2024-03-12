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

class ModelsWarehousePalletRates(object):
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
        'pallet_delivery_expr': 'str',
        'pallet_delivery_value_base': 'str',
        'pallet_delivery_value_liter': 'str',
        'pallet_storage_expr': 'str',
        'pallet_storage_value_expr': 'str',
        'warehouse_name': 'str'
    }

    attribute_map = {
        'pallet_delivery_expr': 'palletDeliveryExpr',
        'pallet_delivery_value_base': 'palletDeliveryValueBase',
        'pallet_delivery_value_liter': 'palletDeliveryValueLiter',
        'pallet_storage_expr': 'palletStorageExpr',
        'pallet_storage_value_expr': 'palletStorageValueExpr',
        'warehouse_name': 'warehouseName'
    }

    def __init__(self, pallet_delivery_expr=None, pallet_delivery_value_base=None, pallet_delivery_value_liter=None, pallet_storage_expr=None, pallet_storage_value_expr=None, warehouse_name=None):  # noqa: E501
        """ModelsWarehousePalletRates - a model defined in Swagger"""  # noqa: E501
        self._pallet_delivery_expr = None
        self._pallet_delivery_value_base = None
        self._pallet_delivery_value_liter = None
        self._pallet_storage_expr = None
        self._pallet_storage_value_expr = None
        self._warehouse_name = None
        self.discriminator = None
        if pallet_delivery_expr is not None:
            self.pallet_delivery_expr = pallet_delivery_expr
        if pallet_delivery_value_base is not None:
            self.pallet_delivery_value_base = pallet_delivery_value_base
        if pallet_delivery_value_liter is not None:
            self.pallet_delivery_value_liter = pallet_delivery_value_liter
        if pallet_storage_expr is not None:
            self.pallet_storage_expr = pallet_storage_expr
        if pallet_storage_value_expr is not None:
            self.pallet_storage_value_expr = pallet_storage_value_expr
        if warehouse_name is not None:
            self.warehouse_name = warehouse_name

    @property
    def pallet_delivery_expr(self):
        """Gets the pallet_delivery_expr of this ModelsWarehousePalletRates.  # noqa: E501

        Koefficient dostavki, %. Na nego umnohaetsa stoimost dostavki. Vo vseh tarifah etot koefficient uhe uhten  # noqa: E501

        :return: The pallet_delivery_expr of this ModelsWarehousePalletRates.  # noqa: E501
        :rtype: str
        """
        return self._pallet_delivery_expr

    @pallet_delivery_expr.setter
    def pallet_delivery_expr(self, pallet_delivery_expr):
        """Sets the pallet_delivery_expr of this ModelsWarehousePalletRates.

        Koefficient dostavki, %. Na nego umnohaetsa stoimost dostavki. Vo vseh tarifah etot koefficient uhe uhten  # noqa: E501

        :param pallet_delivery_expr: The pallet_delivery_expr of this ModelsWarehousePalletRates.  # noqa: E501
        :type: str
        """

        self._pallet_delivery_expr = pallet_delivery_expr

    @property
    def pallet_delivery_value_base(self):
        """Gets the pallet_delivery_value_base of this ModelsWarehousePalletRates.  # noqa: E501

        Dostavka 1 litra, ₽  # noqa: E501

        :return: The pallet_delivery_value_base of this ModelsWarehousePalletRates.  # noqa: E501
        :rtype: str
        """
        return self._pallet_delivery_value_base

    @pallet_delivery_value_base.setter
    def pallet_delivery_value_base(self, pallet_delivery_value_base):
        """Sets the pallet_delivery_value_base of this ModelsWarehousePalletRates.

        Dostavka 1 litra, ₽  # noqa: E501

        :param pallet_delivery_value_base: The pallet_delivery_value_base of this ModelsWarehousePalletRates.  # noqa: E501
        :type: str
        """

        self._pallet_delivery_value_base = pallet_delivery_value_base

    @property
    def pallet_delivery_value_liter(self):
        """Gets the pallet_delivery_value_liter of this ModelsWarehousePalletRates.  # noqa: E501

        Dostavka kahdogo dopolnitelnogo litra, ₽  # noqa: E501

        :return: The pallet_delivery_value_liter of this ModelsWarehousePalletRates.  # noqa: E501
        :rtype: str
        """
        return self._pallet_delivery_value_liter

    @pallet_delivery_value_liter.setter
    def pallet_delivery_value_liter(self, pallet_delivery_value_liter):
        """Sets the pallet_delivery_value_liter of this ModelsWarehousePalletRates.

        Dostavka kahdogo dopolnitelnogo litra, ₽  # noqa: E501

        :param pallet_delivery_value_liter: The pallet_delivery_value_liter of this ModelsWarehousePalletRates.  # noqa: E501
        :type: str
        """

        self._pallet_delivery_value_liter = pallet_delivery_value_liter

    @property
    def pallet_storage_expr(self):
        """Gets the pallet_storage_expr of this ModelsWarehousePalletRates.  # noqa: E501

        Koefficient hranenia, %. Na nego umnohaetsa stoimost hranenia. Vo vseh tarifah etot koefficient uhe uhten  # noqa: E501

        :return: The pallet_storage_expr of this ModelsWarehousePalletRates.  # noqa: E501
        :rtype: str
        """
        return self._pallet_storage_expr

    @pallet_storage_expr.setter
    def pallet_storage_expr(self, pallet_storage_expr):
        """Sets the pallet_storage_expr of this ModelsWarehousePalletRates.

        Koefficient hranenia, %. Na nego umnohaetsa stoimost hranenia. Vo vseh tarifah etot koefficient uhe uhten  # noqa: E501

        :param pallet_storage_expr: The pallet_storage_expr of this ModelsWarehousePalletRates.  # noqa: E501
        :type: str
        """

        self._pallet_storage_expr = pallet_storage_expr

    @property
    def pallet_storage_value_expr(self):
        """Gets the pallet_storage_value_expr of this ModelsWarehousePalletRates.  # noqa: E501

        hranenie 1 monopalety, ₽  # noqa: E501

        :return: The pallet_storage_value_expr of this ModelsWarehousePalletRates.  # noqa: E501
        :rtype: str
        """
        return self._pallet_storage_value_expr

    @pallet_storage_value_expr.setter
    def pallet_storage_value_expr(self, pallet_storage_value_expr):
        """Sets the pallet_storage_value_expr of this ModelsWarehousePalletRates.

        hranenie 1 monopalety, ₽  # noqa: E501

        :param pallet_storage_value_expr: The pallet_storage_value_expr of this ModelsWarehousePalletRates.  # noqa: E501
        :type: str
        """

        self._pallet_storage_value_expr = pallet_storage_value_expr

    @property
    def warehouse_name(self):
        """Gets the warehouse_name of this ModelsWarehousePalletRates.  # noqa: E501

        Nazvanie sklada  # noqa: E501

        :return: The warehouse_name of this ModelsWarehousePalletRates.  # noqa: E501
        :rtype: str
        """
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, warehouse_name):
        """Sets the warehouse_name of this ModelsWarehousePalletRates.

        Nazvanie sklada  # noqa: E501

        :param warehouse_name: The warehouse_name of this ModelsWarehousePalletRates.  # noqa: E501
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
        if issubclass(ModelsWarehousePalletRates, dict):
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
        if not isinstance(other, ModelsWarehousePalletRates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other