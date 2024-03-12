# coding: utf-8

"""
    Opisanie API Voprosov i Otzyvov

    `Vahno!` Dopuskaetsa 1 zapros v sekundu na metody voprosov i otzyvov v celom. Pri prevyhenii limita do 3 zaprosov v sekundu posleduet blokirovka na 60 sekund.   # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20019Data(object):
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
        'user_name': 'str',
        'matching_size': 'str',
        'text': 'str',
        'product_valuation': 'int',
        'created_date': 'datetime',
        'state': 'str',
        'answer': 'InlineResponse20019DataAnswer',
        'product_details': 'InlineResponse20019DataProductDetails',
        'photo_links': 'list[InlineResponse20019DataPhotoLinks]',
        'video': 'InlineResponse20019DataVideo',
        'was_viewed': 'bool',
        'is_able_supplier_feedback_valuation': 'bool',
        'supplier_feedback_valuation': 'int',
        'is_able_supplier_product_valuation': 'bool',
        'supplier_product_valuation': 'int',
        'is_able_return_product_orders': 'bool',
        'return_product_orders_date': 'str',
        'bables': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'user_name': 'userName',
        'matching_size': 'matchingSize',
        'text': 'text',
        'product_valuation': 'productValuation',
        'created_date': 'createdDate',
        'state': 'state',
        'answer': 'answer',
        'product_details': 'productDetails',
        'photo_links': 'photoLinks',
        'video': 'video',
        'was_viewed': 'wasViewed',
        'is_able_supplier_feedback_valuation': 'isAbleSupplierFeedbackValuation',
        'supplier_feedback_valuation': 'supplierFeedbackValuation',
        'is_able_supplier_product_valuation': 'isAbleSupplierProductValuation',
        'supplier_product_valuation': 'supplierProductValuation',
        'is_able_return_product_orders': 'isAbleReturnProductOrders',
        'return_product_orders_date': 'returnProductOrdersDate',
        'bables': 'bables'
    }

    def __init__(self, id=None, user_name=None, matching_size=None, text=None, product_valuation=None, created_date=None, state=None, answer=None, product_details=None, photo_links=None, video=None, was_viewed=None, is_able_supplier_feedback_valuation=None, supplier_feedback_valuation=None, is_able_supplier_product_valuation=None, supplier_product_valuation=None, is_able_return_product_orders=None, return_product_orders_date=None, bables=None):  # noqa: E501
        """InlineResponse20019Data - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_name = None
        self._matching_size = None
        self._text = None
        self._product_valuation = None
        self._created_date = None
        self._state = None
        self._answer = None
        self._product_details = None
        self._photo_links = None
        self._video = None
        self._was_viewed = None
        self._is_able_supplier_feedback_valuation = None
        self._supplier_feedback_valuation = None
        self._is_able_supplier_product_valuation = None
        self._supplier_product_valuation = None
        self._is_able_return_product_orders = None
        self._return_product_orders_date = None
        self._bables = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if user_name is not None:
            self.user_name = user_name
        if matching_size is not None:
            self.matching_size = matching_size
        if text is not None:
            self.text = text
        if product_valuation is not None:
            self.product_valuation = product_valuation
        if created_date is not None:
            self.created_date = created_date
        if state is not None:
            self.state = state
        if answer is not None:
            self.answer = answer
        if product_details is not None:
            self.product_details = product_details
        if photo_links is not None:
            self.photo_links = photo_links
        if video is not None:
            self.video = video
        if was_viewed is not None:
            self.was_viewed = was_viewed
        if is_able_supplier_feedback_valuation is not None:
            self.is_able_supplier_feedback_valuation = is_able_supplier_feedback_valuation
        if supplier_feedback_valuation is not None:
            self.supplier_feedback_valuation = supplier_feedback_valuation
        if is_able_supplier_product_valuation is not None:
            self.is_able_supplier_product_valuation = is_able_supplier_product_valuation
        if supplier_product_valuation is not None:
            self.supplier_product_valuation = supplier_product_valuation
        if is_able_return_product_orders is not None:
            self.is_able_return_product_orders = is_able_return_product_orders
        if return_product_orders_date is not None:
            self.return_product_orders_date = return_product_orders_date
        if bables is not None:
            self.bables = bables

    @property
    def id(self):
        """Gets the id of this InlineResponse20019Data.  # noqa: E501

        Identifikator otzyva  # noqa: E501

        :return: The id of this InlineResponse20019Data.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20019Data.

        Identifikator otzyva  # noqa: E501

        :param id: The id of this InlineResponse20019Data.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user_name(self):
        """Gets the user_name of this InlineResponse20019Data.  # noqa: E501

        Ima avtora otzyva  # noqa: E501

        :return: The user_name of this InlineResponse20019Data.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this InlineResponse20019Data.

        Ima avtora otzyva  # noqa: E501

        :param user_name: The user_name of this InlineResponse20019Data.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def matching_size(self):
        """Gets the matching_size of this InlineResponse20019Data.  # noqa: E501

        <dl> <dt>   Sootvetstvie zaavlennogo razmera realnomu.   <br>Vozmohnye znahenia: </dt> <dd>\"\" - dla bezrazmernyh tovarov,</dd> <dd>\"ok\" - sootvetstvuet razmeru,</dd> <dd>\"smaller\" - malomerit,</dd> <dd>\"bigger\" - bolhemerit</dd>               </dl>    # noqa: E501

        :return: The matching_size of this InlineResponse20019Data.  # noqa: E501
        :rtype: str
        """
        return self._matching_size

    @matching_size.setter
    def matching_size(self, matching_size):
        """Sets the matching_size of this InlineResponse20019Data.

        <dl> <dt>   Sootvetstvie zaavlennogo razmera realnomu.   <br>Vozmohnye znahenia: </dt> <dd>\"\" - dla bezrazmernyh tovarov,</dd> <dd>\"ok\" - sootvetstvuet razmeru,</dd> <dd>\"smaller\" - malomerit,</dd> <dd>\"bigger\" - bolhemerit</dd>               </dl>    # noqa: E501

        :param matching_size: The matching_size of this InlineResponse20019Data.  # noqa: E501
        :type: str
        """

        self._matching_size = matching_size

    @property
    def text(self):
        """Gets the text of this InlineResponse20019Data.  # noqa: E501

        Tekst otzyva  # noqa: E501

        :return: The text of this InlineResponse20019Data.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this InlineResponse20019Data.

        Tekst otzyva  # noqa: E501

        :param text: The text of this InlineResponse20019Data.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def product_valuation(self):
        """Gets the product_valuation of this InlineResponse20019Data.  # noqa: E501

        Ocenka tovara  # noqa: E501

        :return: The product_valuation of this InlineResponse20019Data.  # noqa: E501
        :rtype: int
        """
        return self._product_valuation

    @product_valuation.setter
    def product_valuation(self, product_valuation):
        """Sets the product_valuation of this InlineResponse20019Data.

        Ocenka tovara  # noqa: E501

        :param product_valuation: The product_valuation of this InlineResponse20019Data.  # noqa: E501
        :type: int
        """

        self._product_valuation = product_valuation

    @property
    def created_date(self):
        """Gets the created_date of this InlineResponse20019Data.  # noqa: E501

        Data i vrema sozdania otzyva  # noqa: E501

        :return: The created_date of this InlineResponse20019Data.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this InlineResponse20019Data.

        Data i vrema sozdania otzyva  # noqa: E501

        :param created_date: The created_date of this InlineResponse20019Data.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def state(self):
        """Gets the state of this InlineResponse20019Data.  # noqa: E501

        <dt>Status otzyva:</dt>  <dd>`none` - ne obrabotan (novyi)</dd> <dd>`wbRu` - obrabotan</dd>    # noqa: E501

        :return: The state of this InlineResponse20019Data.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineResponse20019Data.

        <dt>Status otzyva:</dt>  <dd>`none` - ne obrabotan (novyi)</dd> <dd>`wbRu` - obrabotan</dd>    # noqa: E501

        :param state: The state of this InlineResponse20019Data.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def answer(self):
        """Gets the answer of this InlineResponse20019Data.  # noqa: E501


        :return: The answer of this InlineResponse20019Data.  # noqa: E501
        :rtype: InlineResponse20019DataAnswer
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this InlineResponse20019Data.


        :param answer: The answer of this InlineResponse20019Data.  # noqa: E501
        :type: InlineResponse20019DataAnswer
        """

        self._answer = answer

    @property
    def product_details(self):
        """Gets the product_details of this InlineResponse20019Data.  # noqa: E501


        :return: The product_details of this InlineResponse20019Data.  # noqa: E501
        :rtype: InlineResponse20019DataProductDetails
        """
        return self._product_details

    @product_details.setter
    def product_details(self, product_details):
        """Sets the product_details of this InlineResponse20019Data.


        :param product_details: The product_details of this InlineResponse20019Data.  # noqa: E501
        :type: InlineResponse20019DataProductDetails
        """

        self._product_details = product_details

    @property
    def photo_links(self):
        """Gets the photo_links of this InlineResponse20019Data.  # noqa: E501

        Massiv struktur fotografii  # noqa: E501

        :return: The photo_links of this InlineResponse20019Data.  # noqa: E501
        :rtype: list[InlineResponse20019DataPhotoLinks]
        """
        return self._photo_links

    @photo_links.setter
    def photo_links(self, photo_links):
        """Sets the photo_links of this InlineResponse20019Data.

        Massiv struktur fotografii  # noqa: E501

        :param photo_links: The photo_links of this InlineResponse20019Data.  # noqa: E501
        :type: list[InlineResponse20019DataPhotoLinks]
        """

        self._photo_links = photo_links

    @property
    def video(self):
        """Gets the video of this InlineResponse20019Data.  # noqa: E501


        :return: The video of this InlineResponse20019Data.  # noqa: E501
        :rtype: InlineResponse20019DataVideo
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this InlineResponse20019Data.


        :param video: The video of this InlineResponse20019Data.  # noqa: E501
        :type: InlineResponse20019DataVideo
        """

        self._video = video

    @property
    def was_viewed(self):
        """Gets the was_viewed of this InlineResponse20019Data.  # noqa: E501

        Prosmotren li otzyv  # noqa: E501

        :return: The was_viewed of this InlineResponse20019Data.  # noqa: E501
        :rtype: bool
        """
        return self._was_viewed

    @was_viewed.setter
    def was_viewed(self, was_viewed):
        """Sets the was_viewed of this InlineResponse20019Data.

        Prosmotren li otzyv  # noqa: E501

        :param was_viewed: The was_viewed of this InlineResponse20019Data.  # noqa: E501
        :type: bool
        """

        self._was_viewed = was_viewed

    @property
    def is_able_supplier_feedback_valuation(self):
        """Gets the is_able_supplier_feedback_valuation of this InlineResponse20019Data.  # noqa: E501

        Dostupna li prodavcu ocenka otzyva (`true` - dostupna, `false` - ne dostupna)  # noqa: E501

        :return: The is_able_supplier_feedback_valuation of this InlineResponse20019Data.  # noqa: E501
        :rtype: bool
        """
        return self._is_able_supplier_feedback_valuation

    @is_able_supplier_feedback_valuation.setter
    def is_able_supplier_feedback_valuation(self, is_able_supplier_feedback_valuation):
        """Sets the is_able_supplier_feedback_valuation of this InlineResponse20019Data.

        Dostupna li prodavcu ocenka otzyva (`true` - dostupna, `false` - ne dostupna)  # noqa: E501

        :param is_able_supplier_feedback_valuation: The is_able_supplier_feedback_valuation of this InlineResponse20019Data.  # noqa: E501
        :type: bool
        """

        self._is_able_supplier_feedback_valuation = is_able_supplier_feedback_valuation

    @property
    def supplier_feedback_valuation(self):
        """Gets the supplier_feedback_valuation of this InlineResponse20019Data.  # noqa: E501

        Ocenka otzyva, ostavlennaa prodavcom  # noqa: E501

        :return: The supplier_feedback_valuation of this InlineResponse20019Data.  # noqa: E501
        :rtype: int
        """
        return self._supplier_feedback_valuation

    @supplier_feedback_valuation.setter
    def supplier_feedback_valuation(self, supplier_feedback_valuation):
        """Sets the supplier_feedback_valuation of this InlineResponse20019Data.

        Ocenka otzyva, ostavlennaa prodavcom  # noqa: E501

        :param supplier_feedback_valuation: The supplier_feedback_valuation of this InlineResponse20019Data.  # noqa: E501
        :type: int
        """

        self._supplier_feedback_valuation = supplier_feedback_valuation

    @property
    def is_able_supplier_product_valuation(self):
        """Gets the is_able_supplier_product_valuation of this InlineResponse20019Data.  # noqa: E501

        Dostupna li prodavcu ocenka tovara (`true` - dostupna, `false` - ne dostupna)  # noqa: E501

        :return: The is_able_supplier_product_valuation of this InlineResponse20019Data.  # noqa: E501
        :rtype: bool
        """
        return self._is_able_supplier_product_valuation

    @is_able_supplier_product_valuation.setter
    def is_able_supplier_product_valuation(self, is_able_supplier_product_valuation):
        """Sets the is_able_supplier_product_valuation of this InlineResponse20019Data.

        Dostupna li prodavcu ocenka tovara (`true` - dostupna, `false` - ne dostupna)  # noqa: E501

        :param is_able_supplier_product_valuation: The is_able_supplier_product_valuation of this InlineResponse20019Data.  # noqa: E501
        :type: bool
        """

        self._is_able_supplier_product_valuation = is_able_supplier_product_valuation

    @property
    def supplier_product_valuation(self):
        """Gets the supplier_product_valuation of this InlineResponse20019Data.  # noqa: E501

        Ocenka tovara, ostavlennaa prodavcom  # noqa: E501

        :return: The supplier_product_valuation of this InlineResponse20019Data.  # noqa: E501
        :rtype: int
        """
        return self._supplier_product_valuation

    @supplier_product_valuation.setter
    def supplier_product_valuation(self, supplier_product_valuation):
        """Sets the supplier_product_valuation of this InlineResponse20019Data.

        Ocenka tovara, ostavlennaa prodavcom  # noqa: E501

        :param supplier_product_valuation: The supplier_product_valuation of this InlineResponse20019Data.  # noqa: E501
        :type: int
        """

        self._supplier_product_valuation = supplier_product_valuation

    @property
    def is_able_return_product_orders(self):
        """Gets the is_able_return_product_orders of this InlineResponse20019Data.  # noqa: E501

        Dostupna li tovaru opcia vozrata (`fase` - net, `true` - da)  # noqa: E501

        :return: The is_able_return_product_orders of this InlineResponse20019Data.  # noqa: E501
        :rtype: bool
        """
        return self._is_able_return_product_orders

    @is_able_return_product_orders.setter
    def is_able_return_product_orders(self, is_able_return_product_orders):
        """Sets the is_able_return_product_orders of this InlineResponse20019Data.

        Dostupna li tovaru opcia vozrata (`fase` - net, `true` - da)  # noqa: E501

        :param is_able_return_product_orders: The is_able_return_product_orders of this InlineResponse20019Data.  # noqa: E501
        :type: bool
        """

        self._is_able_return_product_orders = is_able_return_product_orders

    @property
    def return_product_orders_date(self):
        """Gets the return_product_orders_date of this InlineResponse20019Data.  # noqa: E501

        Data i vrema, kogda na zapros vozvrata byl poluhen otvet so status-kodom 200.  # noqa: E501

        :return: The return_product_orders_date of this InlineResponse20019Data.  # noqa: E501
        :rtype: str
        """
        return self._return_product_orders_date

    @return_product_orders_date.setter
    def return_product_orders_date(self, return_product_orders_date):
        """Sets the return_product_orders_date of this InlineResponse20019Data.

        Data i vrema, kogda na zapros vozvrata byl poluhen otvet so status-kodom 200.  # noqa: E501

        :param return_product_orders_date: The return_product_orders_date of this InlineResponse20019Data.  # noqa: E501
        :type: str
        """

        self._return_product_orders_date = return_product_orders_date

    @property
    def bables(self):
        """Gets the bables of this InlineResponse20019Data.  # noqa: E501

        Cpisok tegov pokupatela  # noqa: E501

        :return: The bables of this InlineResponse20019Data.  # noqa: E501
        :rtype: list[str]
        """
        return self._bables

    @bables.setter
    def bables(self, bables):
        """Sets the bables of this InlineResponse20019Data.

        Cpisok tegov pokupatela  # noqa: E501

        :param bables: The bables of this InlineResponse20019Data.  # noqa: E501
        :type: list[str]
        """

        self._bables = bables

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
        if issubclass(InlineResponse20019Data, dict):
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
        if not isinstance(other, InlineResponse20019Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
