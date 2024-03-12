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

class ModelsWarehousesBoxRates(object):
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
        'dt_from_min': 'str',
        'dt_next_box': 'str',
        'dt_till_max': 'str',
        'warehouse_list': 'list[ModelsWarehouseBoxRates]'
    }

    attribute_map = {
        'dt_from_min': 'dtFromMin',
        'dt_next_box': 'dtNextBox',
        'dt_till_max': 'dtTillMax',
        'warehouse_list': 'warehouseList'
    }

    def __init__(self, dt_from_min=None, dt_next_box=None, dt_till_max=None, warehouse_list=None):  # noqa: E501
        """ModelsWarehousesBoxRates - a model defined in Swagger"""  # noqa: E501
        self._dt_from_min = None
        self._dt_next_box = None
        self._dt_till_max = None
        self._warehouse_list = None
        self.discriminator = None
        if dt_from_min is not None:
            self.dt_from_min = dt_from_min
        if dt_next_box is not None:
            self.dt_next_box = dt_next_box
        if dt_till_max is not None:
            self.dt_till_max = dt_till_max
        if warehouse_list is not None:
            self.warehouse_list = warehouse_list

    @property
    def dt_from_min(self):
        """Gets the dt_from_min of this ModelsWarehousesBoxRates.  # noqa: E501

        Data nahala tarifa  # noqa: E501

        :return: The dt_from_min of this ModelsWarehousesBoxRates.  # noqa: E501
        :rtype: str
        """
        return self._dt_from_min

    @dt_from_min.setter
    def dt_from_min(self, dt_from_min):
        """Sets the dt_from_min of this ModelsWarehousesBoxRates.

        Data nahala tarifa  # noqa: E501

        :param dt_from_min: The dt_from_min of this ModelsWarehousesBoxRates.  # noqa: E501
        :type: str
        """

        self._dt_from_min = dt_from_min

    @property
    def dt_next_box(self):
        """Gets the dt_next_box of this ModelsWarehousesBoxRates.  # noqa: E501

        Data nahala sleduuhego tarifa  # noqa: E501

        :return: The dt_next_box of this ModelsWarehousesBoxRates.  # noqa: E501
        :rtype: str
        """
        return self._dt_next_box

    @dt_next_box.setter
    def dt_next_box(self, dt_next_box):
        """Sets the dt_next_box of this ModelsWarehousesBoxRates.

        Data nahala sleduuhego tarifa  # noqa: E501

        :param dt_next_box: The dt_next_box of this ModelsWarehousesBoxRates.  # noqa: E501
        :type: str
        """

        self._dt_next_box = dt_next_box

    @property
    def dt_till_max(self):
        """Gets the dt_till_max of this ModelsWarehousesBoxRates.  # noqa: E501

        Data okonhania tarifa  # noqa: E501

        :return: The dt_till_max of this ModelsWarehousesBoxRates.  # noqa: E501
        :rtype: str
        """
        return self._dt_till_max

    @dt_till_max.setter
    def dt_till_max(self, dt_till_max):
        """Sets the dt_till_max of this ModelsWarehousesBoxRates.

        Data okonhania tarifa  # noqa: E501

        :param dt_till_max: The dt_till_max of this ModelsWarehousesBoxRates.  # noqa: E501
        :type: str
        """

        self._dt_till_max = dt_till_max

    @property
    def warehouse_list(self):
        """Gets the warehouse_list of this ModelsWarehousesBoxRates.  # noqa: E501

        Tarify dla korobov, sgruppirovannye po skladam  # noqa: E501

        :return: The warehouse_list of this ModelsWarehousesBoxRates.  # noqa: E501
        :rtype: list[ModelsWarehouseBoxRates]
        """
        return self._warehouse_list

    @warehouse_list.setter
    def warehouse_list(self, warehouse_list):
        """Sets the warehouse_list of this ModelsWarehousesBoxRates.

        Tarify dla korobov, sgruppirovannye po skladam  # noqa: E501

        :param warehouse_list: The warehouse_list of this ModelsWarehousesBoxRates.  # noqa: E501
        :type: list[ModelsWarehouseBoxRates]
        """

        self._warehouse_list = warehouse_list

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
        if issubclass(ModelsWarehousesBoxRates, dict):
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
        if not isinstance(other, ModelsWarehousesBoxRates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
