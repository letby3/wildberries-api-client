# coding: utf-8

"""
    Opisanie API Marketplace

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Order(object):
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
        'id': 'int',
        'rid': 'str',
        'created_at': 'datetime',
        'warehouse_id': 'int',
        'supply_id': 'str',
        'offices': 'list[str]',
        'address': 'OrderAddress',
        'user': 'OrderUser',
        'skus': 'list[str]',
        'price': 'int',
        'converted_price': 'int',
        'currency_code': 'int',
        'converted_currency_code': 'int',
        'order_uid': 'str',
        'delivery_type': 'str',
        'nm_id': 'int',
        'chrt_id': 'int',
        'article': 'str',
        'cargo_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'rid': 'rid',
        'created_at': 'createdAt',
        'warehouse_id': 'warehouseId',
        'supply_id': 'supplyId',
        'offices': 'offices',
        'address': 'address',
        'user': 'user',
        'skus': 'skus',
        'price': 'price',
        'converted_price': 'convertedPrice',
        'currency_code': 'currencyCode',
        'converted_currency_code': 'convertedCurrencyCode',
        'order_uid': 'orderUid',
        'delivery_type': 'deliveryType',
        'nm_id': 'nmId',
        'chrt_id': 'chrtId',
        'article': 'article',
        'cargo_type': 'cargoType'
    }

    def __init__(self, id=None, rid=None, created_at=None, warehouse_id=None, supply_id=None, offices=None, address=None, user=None, skus=None, price=None, converted_price=None, currency_code=None, converted_currency_code=None, order_uid=None, delivery_type=None, nm_id=None, chrt_id=None, article=None, cargo_type=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._rid = None
        self._created_at = None
        self._warehouse_id = None
        self._supply_id = None
        self._offices = None
        self._address = None
        self._user = None
        self._skus = None
        self._price = None
        self._converted_price = None
        self._currency_code = None
        self._converted_currency_code = None
        self._order_uid = None
        self._delivery_type = None
        self._nm_id = None
        self._chrt_id = None
        self._article = None
        self._cargo_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if rid is not None:
            self.rid = rid
        if created_at is not None:
            self.created_at = created_at
        if warehouse_id is not None:
            self.warehouse_id = warehouse_id
        if supply_id is not None:
            self.supply_id = supply_id
        if offices is not None:
            self.offices = offices
        if address is not None:
            self.address = address
        if user is not None:
            self.user = user
        if skus is not None:
            self.skus = skus
        if price is not None:
            self.price = price
        if converted_price is not None:
            self.converted_price = converted_price
        if currency_code is not None:
            self.currency_code = currency_code
        if converted_currency_code is not None:
            self.converted_currency_code = converted_currency_code
        if order_uid is not None:
            self.order_uid = order_uid
        if delivery_type is not None:
            self.delivery_type = delivery_type
        if nm_id is not None:
            self.nm_id = nm_id
        if chrt_id is not None:
            self.chrt_id = chrt_id
        if article is not None:
            self.article = article
        if cargo_type is not None:
            self.cargo_type = cargo_type

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501

        Identifikator sborohnogo zadania v Marketpleise  # noqa: E501

        :return: The id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.

        Identifikator sborohnogo zadania v Marketpleise  # noqa: E501

        :param id: The id of this Order.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def rid(self):
        """Gets the rid of this Order.  # noqa: E501

        Identifikator sborohnogo zadania v sisteme Wildberries  # noqa: E501

        :return: The rid of this Order.  # noqa: E501
        :rtype: str
        """
        return self._rid

    @rid.setter
    def rid(self, rid):
        """Sets the rid of this Order.

        Identifikator sborohnogo zadania v sisteme Wildberries  # noqa: E501

        :param rid: The rid of this Order.  # noqa: E501
        :type: str
        """

        self._rid = rid

    @property
    def created_at(self):
        """Gets the created_at of this Order.  # noqa: E501

        Data sozdania sborohnogo zadania (RFC3339)  # noqa: E501

        :return: The created_at of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Order.

        Data sozdania sborohnogo zadania (RFC3339)  # noqa: E501

        :param created_at: The created_at of this Order.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this Order.  # noqa: E501

        Identifikator sklada prodavca, na kotoryi postupilo sborohnoe zadanie  # noqa: E501

        :return: The warehouse_id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this Order.

        Identifikator sklada prodavca, na kotoryi postupilo sborohnoe zadanie  # noqa: E501

        :param warehouse_id: The warehouse_id of this Order.  # noqa: E501
        :type: int
        """

        self._warehouse_id = warehouse_id

    @property
    def supply_id(self):
        """Gets the supply_id of this Order.  # noqa: E501

        Identifikator postavki. Vozvrahaetsa, esli zakaz zakreplen za postavkoi  # noqa: E501

        :return: The supply_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._supply_id

    @supply_id.setter
    def supply_id(self, supply_id):
        """Sets the supply_id of this Order.

        Identifikator postavki. Vozvrahaetsa, esli zakaz zakreplen za postavkoi  # noqa: E501

        :param supply_id: The supply_id of this Order.  # noqa: E501
        :type: str
        """

        self._supply_id = supply_id

    @property
    def offices(self):
        """Gets the offices of this Order.  # noqa: E501

        Spisok ofisov, kuda sleduet privezti tovar  # noqa: E501

        :return: The offices of this Order.  # noqa: E501
        :rtype: list[str]
        """
        return self._offices

    @offices.setter
    def offices(self, offices):
        """Sets the offices of this Order.

        Spisok ofisov, kuda sleduet privezti tovar  # noqa: E501

        :param offices: The offices of this Order.  # noqa: E501
        :type: list[str]
        """

        self._offices = offices

    @property
    def address(self):
        """Gets the address of this Order.  # noqa: E501


        :return: The address of this Order.  # noqa: E501
        :rtype: OrderAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Order.


        :param address: The address of this Order.  # noqa: E501
        :type: OrderAddress
        """

        self._address = address

    @property
    def user(self):
        """Gets the user of this Order.  # noqa: E501


        :return: The user of this Order.  # noqa: E501
        :rtype: OrderUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Order.


        :param user: The user of this Order.  # noqa: E501
        :type: OrderUser
        """

        self._user = user

    @property
    def skus(self):
        """Gets the skus of this Order.  # noqa: E501

        Massiv barkodov tovara  # noqa: E501

        :return: The skus of this Order.  # noqa: E501
        :rtype: list[str]
        """
        return self._skus

    @skus.setter
    def skus(self, skus):
        """Sets the skus of this Order.

        Massiv barkodov tovara  # noqa: E501

        :param skus: The skus of this Order.  # noqa: E501
        :type: list[str]
        """

        self._skus = skus

    @property
    def price(self):
        """Gets the price of this Order.  # noqa: E501

        cena v valute prodahi s uhetom vseh skidok, umnohennaa na 100. Kod valuty prodahi v pole currencyCode.  # noqa: E501

        :return: The price of this Order.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Order.

        cena v valute prodahi s uhetom vseh skidok, umnohennaa na 100. Kod valuty prodahi v pole currencyCode.  # noqa: E501

        :param price: The price of this Order.  # noqa: E501
        :type: int
        """

        self._price = price

    @property
    def converted_price(self):
        """Gets the converted_price of this Order.  # noqa: E501

        cena v valute prodahi s uhetom vseh skidok, skonvertirovannaa po kursu na moment prodahi v rossiiskie kopeiki. Predostavlaetsa v informacionnyh celah.  # noqa: E501

        :return: The converted_price of this Order.  # noqa: E501
        :rtype: int
        """
        return self._converted_price

    @converted_price.setter
    def converted_price(self, converted_price):
        """Sets the converted_price of this Order.

        cena v valute prodahi s uhetom vseh skidok, skonvertirovannaa po kursu na moment prodahi v rossiiskie kopeiki. Predostavlaetsa v informacionnyh celah.  # noqa: E501

        :param converted_price: The converted_price of this Order.  # noqa: E501
        :type: int
        """

        self._converted_price = converted_price

    @property
    def currency_code(self):
        """Gets the currency_code of this Order.  # noqa: E501

        Kod valuty prodahi (ISO 4217)  # noqa: E501

        :return: The currency_code of this Order.  # noqa: E501
        :rtype: int
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Order.

        Kod valuty prodahi (ISO 4217)  # noqa: E501

        :param currency_code: The currency_code of this Order.  # noqa: E501
        :type: int
        """

        self._currency_code = currency_code

    @property
    def converted_currency_code(self):
        """Gets the converted_currency_code of this Order.  # noqa: E501

        Kod valuty strany prodavca (ISO 4217)  # noqa: E501

        :return: The converted_currency_code of this Order.  # noqa: E501
        :rtype: int
        """
        return self._converted_currency_code

    @converted_currency_code.setter
    def converted_currency_code(self, converted_currency_code):
        """Sets the converted_currency_code of this Order.

        Kod valuty strany prodavca (ISO 4217)  # noqa: E501

        :param converted_currency_code: The converted_currency_code of this Order.  # noqa: E501
        :type: int
        """

        self._converted_currency_code = converted_currency_code

    @property
    def order_uid(self):
        """Gets the order_uid of this Order.  # noqa: E501

        Identifikator tranzakcii dla gruppirovki sborohnyh zadanii. Sborohnye zadania v odnoi korzine pokupatela budut imet odinakovyi orderUID  # noqa: E501

        :return: The order_uid of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_uid

    @order_uid.setter
    def order_uid(self, order_uid):
        """Sets the order_uid of this Order.

        Identifikator tranzakcii dla gruppirovki sborohnyh zadanii. Sborohnye zadania v odnoi korzine pokupatela budut imet odinakovyi orderUID  # noqa: E501

        :param order_uid: The order_uid of this Order.  # noqa: E501
        :type: str
        """

        self._order_uid = order_uid

    @property
    def delivery_type(self):
        """Gets the delivery_type of this Order.  # noqa: E501

        <dl> <dt>Tip dostavki:</dt> <dd>fbs - dostavka na sklad Wildberries</dd> <dd>dbs - dostavka silami prodavca</dd> <dd>wbgo - dostavka kurerom WB</dd> </dl>   # noqa: E501

        :return: The delivery_type of this Order.  # noqa: E501
        :rtype: str
        """
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, delivery_type):
        """Sets the delivery_type of this Order.

        <dl> <dt>Tip dostavki:</dt> <dd>fbs - dostavka na sklad Wildberries</dd> <dd>dbs - dostavka silami prodavca</dd> <dd>wbgo - dostavka kurerom WB</dd> </dl>   # noqa: E501

        :param delivery_type: The delivery_type of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["dbs", "fbs", "wbgo"]  # noqa: E501
        if delivery_type not in allowed_values:
            raise ValueError(
                "Invalid value for `delivery_type` ({0}), must be one of {1}"  # noqa: E501
                .format(delivery_type, allowed_values)
            )

        self._delivery_type = delivery_type

    @property
    def nm_id(self):
        """Gets the nm_id of this Order.  # noqa: E501

        Artikul WB  # noqa: E501

        :return: The nm_id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._nm_id

    @nm_id.setter
    def nm_id(self, nm_id):
        """Sets the nm_id of this Order.

        Artikul WB  # noqa: E501

        :param nm_id: The nm_id of this Order.  # noqa: E501
        :type: int
        """

        self._nm_id = nm_id

    @property
    def chrt_id(self):
        """Gets the chrt_id of this Order.  # noqa: E501

        Identifikator razmera tovara v sisteme Wildberries  # noqa: E501

        :return: The chrt_id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._chrt_id

    @chrt_id.setter
    def chrt_id(self, chrt_id):
        """Sets the chrt_id of this Order.

        Identifikator razmera tovara v sisteme Wildberries  # noqa: E501

        :param chrt_id: The chrt_id of this Order.  # noqa: E501
        :type: int
        """

        self._chrt_id = chrt_id

    @property
    def article(self):
        """Gets the article of this Order.  # noqa: E501

        Artikul prodavca  # noqa: E501

        :return: The article of this Order.  # noqa: E501
        :rtype: str
        """
        return self._article

    @article.setter
    def article(self, article):
        """Sets the article of this Order.

        Artikul prodavca  # noqa: E501

        :param article: The article of this Order.  # noqa: E501
        :type: str
        """

        self._article = article

    @property
    def cargo_type(self):
        """Gets the cargo_type of this Order.  # noqa: E501

        <dl> <dt>Tip tovara:</dt> <dd>1 - obyhnyi</dd> <dd>2 - SGT (Sverhgabaritnyi tovar)</dd> <dd>3 - KGT (Krupnogabaritnyi tovar). Ne ispolzuetsa na dannyi moment.</dd> </dl>   # noqa: E501

        :return: The cargo_type of this Order.  # noqa: E501
        :rtype: int
        """
        return self._cargo_type

    @cargo_type.setter
    def cargo_type(self, cargo_type):
        """Sets the cargo_type of this Order.

        <dl> <dt>Tip tovara:</dt> <dd>1 - obyhnyi</dd> <dd>2 - SGT (Sverhgabaritnyi tovar)</dd> <dd>3 - KGT (Krupnogabaritnyi tovar). Ne ispolzuetsa na dannyi moment.</dd> </dl>   # noqa: E501

        :param cargo_type: The cargo_type of this Order.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3]  # noqa: E501
        if cargo_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cargo_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cargo_type, allowed_values)
            )

        self._cargo_type = cargo_type

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
