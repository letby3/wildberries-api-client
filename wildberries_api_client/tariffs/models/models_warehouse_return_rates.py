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

class ModelsWarehouseReturnRates(object):
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
        'delivery_dump_kgt_office_base': 'str',
        'delivery_dump_kgt_office_liter': 'str',
        'delivery_dump_kgt_return_expr': 'str',
        'delivery_dump_srg_office_expr': 'str',
        'delivery_dump_srg_return_expr': 'str',
        'delivery_dump_sup_courier_base': 'str',
        'delivery_dump_sup_courier_liter': 'str',
        'delivery_dump_sup_office_base': 'str',
        'delivery_dump_sup_office_liter': 'str',
        'delivery_dump_sup_return_expr': 'str',
        'warehouse_name': 'str'
    }

    attribute_map = {
        'delivery_dump_kgt_office_base': 'deliveryDumpKgtOfficeBase',
        'delivery_dump_kgt_office_liter': 'deliveryDumpKgtOfficeLiter',
        'delivery_dump_kgt_return_expr': 'deliveryDumpKgtReturnExpr',
        'delivery_dump_srg_office_expr': 'deliveryDumpSrgOfficeExpr',
        'delivery_dump_srg_return_expr': 'deliveryDumpSrgReturnExpr',
        'delivery_dump_sup_courier_base': 'deliveryDumpSupCourierBase',
        'delivery_dump_sup_courier_liter': 'deliveryDumpSupCourierLiter',
        'delivery_dump_sup_office_base': 'deliveryDumpSupOfficeBase',
        'delivery_dump_sup_office_liter': 'deliveryDumpSupOfficeLiter',
        'delivery_dump_sup_return_expr': 'deliveryDumpSupReturnExpr',
        'warehouse_name': 'warehouseName'
    }

    def __init__(self, delivery_dump_kgt_office_base=None, delivery_dump_kgt_office_liter=None, delivery_dump_kgt_return_expr=None, delivery_dump_srg_office_expr=None, delivery_dump_srg_return_expr=None, delivery_dump_sup_courier_base=None, delivery_dump_sup_courier_liter=None, delivery_dump_sup_office_base=None, delivery_dump_sup_office_liter=None, delivery_dump_sup_return_expr=None, warehouse_name=None):  # noqa: E501
        """ModelsWarehouseReturnRates - a model defined in Swagger"""  # noqa: E501
        self._delivery_dump_kgt_office_base = None
        self._delivery_dump_kgt_office_liter = None
        self._delivery_dump_kgt_return_expr = None
        self._delivery_dump_srg_office_expr = None
        self._delivery_dump_srg_return_expr = None
        self._delivery_dump_sup_courier_base = None
        self._delivery_dump_sup_courier_liter = None
        self._delivery_dump_sup_office_base = None
        self._delivery_dump_sup_office_liter = None
        self._delivery_dump_sup_return_expr = None
        self._warehouse_name = None
        self.discriminator = None
        if delivery_dump_kgt_office_base is not None:
            self.delivery_dump_kgt_office_base = delivery_dump_kgt_office_base
        if delivery_dump_kgt_office_liter is not None:
            self.delivery_dump_kgt_office_liter = delivery_dump_kgt_office_liter
        if delivery_dump_kgt_return_expr is not None:
            self.delivery_dump_kgt_return_expr = delivery_dump_kgt_return_expr
        if delivery_dump_srg_office_expr is not None:
            self.delivery_dump_srg_office_expr = delivery_dump_srg_office_expr
        if delivery_dump_srg_return_expr is not None:
            self.delivery_dump_srg_return_expr = delivery_dump_srg_return_expr
        if delivery_dump_sup_courier_base is not None:
            self.delivery_dump_sup_courier_base = delivery_dump_sup_courier_base
        if delivery_dump_sup_courier_liter is not None:
            self.delivery_dump_sup_courier_liter = delivery_dump_sup_courier_liter
        if delivery_dump_sup_office_base is not None:
            self.delivery_dump_sup_office_base = delivery_dump_sup_office_base
        if delivery_dump_sup_office_liter is not None:
            self.delivery_dump_sup_office_liter = delivery_dump_sup_office_liter
        if delivery_dump_sup_return_expr is not None:
            self.delivery_dump_sup_return_expr = delivery_dump_sup_return_expr
        if warehouse_name is not None:
            self.warehouse_name = warehouse_name

    @property
    def delivery_dump_kgt_office_base(self):
        """Gets the delivery_dump_kgt_office_base of this ModelsWarehouseReturnRates.  # noqa: E501

        <p><b>Stoimost vozvrata pri gruzovoi dostavke, dostavka na PVZ (bazovaa cena za 1 l), ₽</b></p> <p>Primenaetsa dla krupnogabaritnyh tovarov, kogda:<p> <ul>   <li>prodavec hohet vyvezti tovary so sklada Wildberries;</li>   <li>na sklade obnaruhili brakovannye tovary;</li>   <li>pokupatel vozvrahaet tovar, no ego nelza vernut v prodahu.</li> </ul>   # noqa: E501

        :return: The delivery_dump_kgt_office_base of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_kgt_office_base

    @delivery_dump_kgt_office_base.setter
    def delivery_dump_kgt_office_base(self, delivery_dump_kgt_office_base):
        """Sets the delivery_dump_kgt_office_base of this ModelsWarehouseReturnRates.

        <p><b>Stoimost vozvrata pri gruzovoi dostavke, dostavka na PVZ (bazovaa cena za 1 l), ₽</b></p> <p>Primenaetsa dla krupnogabaritnyh tovarov, kogda:<p> <ul>   <li>prodavec hohet vyvezti tovary so sklada Wildberries;</li>   <li>na sklade obnaruhili brakovannye tovary;</li>   <li>pokupatel vozvrahaet tovar, no ego nelza vernut v prodahu.</li> </ul>   # noqa: E501

        :param delivery_dump_kgt_office_base: The delivery_dump_kgt_office_base of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_kgt_office_base = delivery_dump_kgt_office_base

    @property
    def delivery_dump_kgt_office_liter(self):
        """Gets the delivery_dump_kgt_office_liter of this ModelsWarehouseReturnRates.  # noqa: E501

        <p><b>Stoimost vozvrata pri gruzovoi dostavke, dostavka na PVZ (dop. litr), ₽</b></p> <p>Stoimost za kahdyi dopolnitelnyi litr.</p>   # noqa: E501

        :return: The delivery_dump_kgt_office_liter of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_kgt_office_liter

    @delivery_dump_kgt_office_liter.setter
    def delivery_dump_kgt_office_liter(self, delivery_dump_kgt_office_liter):
        """Sets the delivery_dump_kgt_office_liter of this ModelsWarehouseReturnRates.

        <p><b>Stoimost vozvrata pri gruzovoi dostavke, dostavka na PVZ (dop. litr), ₽</b></p> <p>Stoimost za kahdyi dopolnitelnyi litr.</p>   # noqa: E501

        :param delivery_dump_kgt_office_liter: The delivery_dump_kgt_office_liter of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_kgt_office_liter = delivery_dump_kgt_office_liter

    @property
    def delivery_dump_kgt_return_expr(self):
        """Gets the delivery_dump_kgt_return_expr of this ModelsWarehouseReturnRates.  # noqa: E501

        <p><b>Stoimost vozvrata pri gruzovoi dostavke, obratnaa logistika nevostrebovannogo vozvrata, ₽</b><p> <p>Gruzovaa dostavka nevostrebovannogo vozvrata obratno na sklad Wildberries. Za edinicu tovara.</p>   # noqa: E501

        :return: The delivery_dump_kgt_return_expr of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_kgt_return_expr

    @delivery_dump_kgt_return_expr.setter
    def delivery_dump_kgt_return_expr(self, delivery_dump_kgt_return_expr):
        """Sets the delivery_dump_kgt_return_expr of this ModelsWarehouseReturnRates.

        <p><b>Stoimost vozvrata pri gruzovoi dostavke, obratnaa logistika nevostrebovannogo vozvrata, ₽</b><p> <p>Gruzovaa dostavka nevostrebovannogo vozvrata obratno na sklad Wildberries. Za edinicu tovara.</p>   # noqa: E501

        :param delivery_dump_kgt_return_expr: The delivery_dump_kgt_return_expr of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_kgt_return_expr = delivery_dump_kgt_return_expr

    @property
    def delivery_dump_srg_office_expr(self):
        """Gets the delivery_dump_srg_office_expr of this ModelsWarehouseReturnRates.  # noqa: E501

        <p><b>Stoimost vozvrata neopoznannogo skladom tovara za kahduu edinicu, dostavka na PVZ, ₽</b></p> <p>Primenaetsa dla tovarov, kotorye ne smogli prinat na sklade</p>.   # noqa: E501

        :return: The delivery_dump_srg_office_expr of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_srg_office_expr

    @delivery_dump_srg_office_expr.setter
    def delivery_dump_srg_office_expr(self, delivery_dump_srg_office_expr):
        """Sets the delivery_dump_srg_office_expr of this ModelsWarehouseReturnRates.

        <p><b>Stoimost vozvrata neopoznannogo skladom tovara za kahduu edinicu, dostavka na PVZ, ₽</b></p> <p>Primenaetsa dla tovarov, kotorye ne smogli prinat na sklade</p>.   # noqa: E501

        :param delivery_dump_srg_office_expr: The delivery_dump_srg_office_expr of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_srg_office_expr = delivery_dump_srg_office_expr

    @property
    def delivery_dump_srg_return_expr(self):
        """Gets the delivery_dump_srg_return_expr of this ModelsWarehouseReturnRates.  # noqa: E501

        <p><b>Stoimost vozvrata neopoznannogo skladom tovara za kahduu edinicu, obratnaa logistika nevostrebovannogo vozvrata</b></p> <p>Dostavka nevostrebovannogo vozvrata obratno na sklad Wildberries.</p>  # noqa: E501

        :return: The delivery_dump_srg_return_expr of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_srg_return_expr

    @delivery_dump_srg_return_expr.setter
    def delivery_dump_srg_return_expr(self, delivery_dump_srg_return_expr):
        """Sets the delivery_dump_srg_return_expr of this ModelsWarehouseReturnRates.

        <p><b>Stoimost vozvrata neopoznannogo skladom tovara za kahduu edinicu, obratnaa logistika nevostrebovannogo vozvrata</b></p> <p>Dostavka nevostrebovannogo vozvrata obratno na sklad Wildberries.</p>  # noqa: E501

        :param delivery_dump_srg_return_expr: The delivery_dump_srg_return_expr of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_srg_return_expr = delivery_dump_srg_return_expr

    @property
    def delivery_dump_sup_courier_base(self):
        """Gets the delivery_dump_sup_courier_base of this ModelsWarehouseReturnRates.  # noqa: E501

        Stoimost vozvrata, dostavka kurerom (bazovaa cena za 1 l). Seihas etot tarif ne primenaetsa  # noqa: E501

        :return: The delivery_dump_sup_courier_base of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_sup_courier_base

    @delivery_dump_sup_courier_base.setter
    def delivery_dump_sup_courier_base(self, delivery_dump_sup_courier_base):
        """Sets the delivery_dump_sup_courier_base of this ModelsWarehouseReturnRates.

        Stoimost vozvrata, dostavka kurerom (bazovaa cena za 1 l). Seihas etot tarif ne primenaetsa  # noqa: E501

        :param delivery_dump_sup_courier_base: The delivery_dump_sup_courier_base of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_sup_courier_base = delivery_dump_sup_courier_base

    @property
    def delivery_dump_sup_courier_liter(self):
        """Gets the delivery_dump_sup_courier_liter of this ModelsWarehouseReturnRates.  # noqa: E501

        Stoimost vozvrata, dostavka kurerom (dop. l). Seihas etot tarif ne primenaetsa  # noqa: E501

        :return: The delivery_dump_sup_courier_liter of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_sup_courier_liter

    @delivery_dump_sup_courier_liter.setter
    def delivery_dump_sup_courier_liter(self, delivery_dump_sup_courier_liter):
        """Sets the delivery_dump_sup_courier_liter of this ModelsWarehouseReturnRates.

        Stoimost vozvrata, dostavka kurerom (dop. l). Seihas etot tarif ne primenaetsa  # noqa: E501

        :param delivery_dump_sup_courier_liter: The delivery_dump_sup_courier_liter of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_sup_courier_liter = delivery_dump_sup_courier_liter

    @property
    def delivery_dump_sup_office_base(self):
        """Gets the delivery_dump_sup_office_base of this ModelsWarehouseReturnRates.  # noqa: E501

        <p><b>Stoimost vozvrata, dostavka na PVZ (bazovaa cena za 1 l), ₽</b></p> <p>Primenaetsa, kogda:<p> <ul> <li>prodavec hohet vyvezti tovary so sklada Wildberries;</li> <li>na sklade obnaruhili brakovannye tovary;</li> <li>pokupatel vozvrahaet tovar, no ego nelza vernut v prodahu.</li> </ul>  # noqa: E501

        :return: The delivery_dump_sup_office_base of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_sup_office_base

    @delivery_dump_sup_office_base.setter
    def delivery_dump_sup_office_base(self, delivery_dump_sup_office_base):
        """Sets the delivery_dump_sup_office_base of this ModelsWarehouseReturnRates.

        <p><b>Stoimost vozvrata, dostavka na PVZ (bazovaa cena za 1 l), ₽</b></p> <p>Primenaetsa, kogda:<p> <ul> <li>prodavec hohet vyvezti tovary so sklada Wildberries;</li> <li>na sklade obnaruhili brakovannye tovary;</li> <li>pokupatel vozvrahaet tovar, no ego nelza vernut v prodahu.</li> </ul>  # noqa: E501

        :param delivery_dump_sup_office_base: The delivery_dump_sup_office_base of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_sup_office_base = delivery_dump_sup_office_base

    @property
    def delivery_dump_sup_office_liter(self):
        """Gets the delivery_dump_sup_office_liter of this ModelsWarehouseReturnRates.  # noqa: E501

        <p><b>Stoimost vozvrata, dostavka na PVZ (dop. litr), ₽</b></p> <p>Stoimost za kahdyi dopolnitelnyi litr</p>  # noqa: E501

        :return: The delivery_dump_sup_office_liter of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_sup_office_liter

    @delivery_dump_sup_office_liter.setter
    def delivery_dump_sup_office_liter(self, delivery_dump_sup_office_liter):
        """Sets the delivery_dump_sup_office_liter of this ModelsWarehouseReturnRates.

        <p><b>Stoimost vozvrata, dostavka na PVZ (dop. litr), ₽</b></p> <p>Stoimost za kahdyi dopolnitelnyi litr</p>  # noqa: E501

        :param delivery_dump_sup_office_liter: The delivery_dump_sup_office_liter of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_sup_office_liter = delivery_dump_sup_office_liter

    @property
    def delivery_dump_sup_return_expr(self):
        """Gets the delivery_dump_sup_return_expr of this ModelsWarehouseReturnRates.  # noqa: E501

        <p><b>Stoimost vozvrata, obratnaa logistika nevostrebovannogo vozvrata, za edinicu tovara, ₽</b></p>   # noqa: E501

        :return: The delivery_dump_sup_return_expr of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._delivery_dump_sup_return_expr

    @delivery_dump_sup_return_expr.setter
    def delivery_dump_sup_return_expr(self, delivery_dump_sup_return_expr):
        """Sets the delivery_dump_sup_return_expr of this ModelsWarehouseReturnRates.

        <p><b>Stoimost vozvrata, obratnaa logistika nevostrebovannogo vozvrata, za edinicu tovara, ₽</b></p>   # noqa: E501

        :param delivery_dump_sup_return_expr: The delivery_dump_sup_return_expr of this ModelsWarehouseReturnRates.  # noqa: E501
        :type: str
        """

        self._delivery_dump_sup_return_expr = delivery_dump_sup_return_expr

    @property
    def warehouse_name(self):
        """Gets the warehouse_name of this ModelsWarehouseReturnRates.  # noqa: E501

        Nazvanie sklada  # noqa: E501

        :return: The warehouse_name of this ModelsWarehouseReturnRates.  # noqa: E501
        :rtype: str
        """
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, warehouse_name):
        """Sets the warehouse_name of this ModelsWarehouseReturnRates.

        Nazvanie sklada  # noqa: E501

        :param warehouse_name: The warehouse_name of this ModelsWarehouseReturnRates.  # noqa: E501
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
        if issubclass(ModelsWarehouseReturnRates, dict):
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
        if not isinstance(other, ModelsWarehouseReturnRates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other