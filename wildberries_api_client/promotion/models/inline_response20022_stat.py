# coding: utf-8

"""
    Opisanie API Prodvihenie

    Sinhronizacia dannyh iz bd proishodit raz v 3 minuty.  <br>Izmenenie statusa proishodit raz v 1 minutu. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu statusa. <br>Izmenenie stavki proishodit raz v 30 sekund. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu stavki.   # noqa: E501

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20022Stat(object):
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
        'advert_id': 'int',
        'keyword': 'str',
        'advert_name': 'str',
        'campaign_name': 'str',
        'begin': 'datetime',
        'end': 'datetime',
        'views': 'int',
        'clicks': 'int',
        'frq': 'int',
        'ctr': 'float',
        'cpc': 'float',
        'duration': 'int',
        'sum': 'float'
    }

    attribute_map = {
        'advert_id': 'advertId',
        'keyword': 'keyword',
        'advert_name': 'advertName',
        'campaign_name': 'campaignName',
        'begin': 'begin',
        'end': 'end',
        'views': 'views',
        'clicks': 'clicks',
        'frq': 'frq',
        'ctr': 'ctr',
        'cpc': 'cpc',
        'duration': 'duration',
        'sum': 'sum'
    }

    def __init__(self, advert_id=None, keyword=None, advert_name=None, campaign_name=None, begin=None, end=None, views=None, clicks=None, frq=None, ctr=None, cpc=None, duration=None, sum=None):  # noqa: E501
        """InlineResponse20022Stat - a model defined in Swagger"""  # noqa: E501
        self._advert_id = None
        self._keyword = None
        self._advert_name = None
        self._campaign_name = None
        self._begin = None
        self._end = None
        self._views = None
        self._clicks = None
        self._frq = None
        self._ctr = None
        self._cpc = None
        self._duration = None
        self._sum = None
        self.discriminator = None
        if advert_id is not None:
            self.advert_id = advert_id
        if keyword is not None:
            self.keyword = keyword
        if advert_name is not None:
            self.advert_name = advert_name
        if campaign_name is not None:
            self.campaign_name = campaign_name
        if begin is not None:
            self.begin = begin
        if end is not None:
            self.end = end
        if views is not None:
            self.views = views
        if clicks is not None:
            self.clicks = clicks
        if frq is not None:
            self.frq = frq
        if ctr is not None:
            self.ctr = ctr
        if cpc is not None:
            self.cpc = cpc
        if duration is not None:
            self.duration = duration
        if sum is not None:
            self.sum = sum

    @property
    def advert_id(self):
        """Gets the advert_id of this InlineResponse20022Stat.  # noqa: E501

        Identifikator kampanii v sisteme Wildberries  # noqa: E501

        :return: The advert_id of this InlineResponse20022Stat.  # noqa: E501
        :rtype: int
        """
        return self._advert_id

    @advert_id.setter
    def advert_id(self, advert_id):
        """Sets the advert_id of this InlineResponse20022Stat.

        Identifikator kampanii v sisteme Wildberries  # noqa: E501

        :param advert_id: The advert_id of this InlineResponse20022Stat.  # noqa: E501
        :type: int
        """

        self._advert_id = advert_id

    @property
    def keyword(self):
        """Gets the keyword of this InlineResponse20022Stat.  # noqa: E501

        Kluhevaa fraza  # noqa: E501

        :return: The keyword of this InlineResponse20022Stat.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this InlineResponse20022Stat.

        Kluhevaa fraza  # noqa: E501

        :param keyword: The keyword of this InlineResponse20022Stat.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def advert_name(self):
        """Gets the advert_name of this InlineResponse20022Stat.  # noqa: E501

        Pole permanentno otkluheno  # noqa: E501

        :return: The advert_name of this InlineResponse20022Stat.  # noqa: E501
        :rtype: str
        """
        return self._advert_name

    @advert_name.setter
    def advert_name(self, advert_name):
        """Sets the advert_name of this InlineResponse20022Stat.

        Pole permanentno otkluheno  # noqa: E501

        :param advert_name: The advert_name of this InlineResponse20022Stat.  # noqa: E501
        :type: str
        """

        self._advert_name = advert_name

    @property
    def campaign_name(self):
        """Gets the campaign_name of this InlineResponse20022Stat.  # noqa: E501

        Nazvanie kampanii  # noqa: E501

        :return: The campaign_name of this InlineResponse20022Stat.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this InlineResponse20022Stat.

        Nazvanie kampanii  # noqa: E501

        :param campaign_name: The campaign_name of this InlineResponse20022Stat.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def begin(self):
        """Gets the begin of this InlineResponse20022Stat.  # noqa: E501

        Data zapuska kampanii  # noqa: E501

        :return: The begin of this InlineResponse20022Stat.  # noqa: E501
        :rtype: datetime
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this InlineResponse20022Stat.

        Data zapuska kampanii  # noqa: E501

        :param begin: The begin of this InlineResponse20022Stat.  # noqa: E501
        :type: datetime
        """

        self._begin = begin

    @property
    def end(self):
        """Gets the end of this InlineResponse20022Stat.  # noqa: E501

        Data zaverhenia kampanii  # noqa: E501

        :return: The end of this InlineResponse20022Stat.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this InlineResponse20022Stat.

        Data zaverhenia kampanii  # noqa: E501

        :param end: The end of this InlineResponse20022Stat.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def views(self):
        """Gets the views of this InlineResponse20022Stat.  # noqa: E501

        Kolihestvo prosmotrov  # noqa: E501

        :return: The views of this InlineResponse20022Stat.  # noqa: E501
        :rtype: int
        """
        return self._views

    @views.setter
    def views(self, views):
        """Sets the views of this InlineResponse20022Stat.

        Kolihestvo prosmotrov  # noqa: E501

        :param views: The views of this InlineResponse20022Stat.  # noqa: E501
        :type: int
        """

        self._views = views

    @property
    def clicks(self):
        """Gets the clicks of this InlineResponse20022Stat.  # noqa: E501

        Kolihestvo klikov  # noqa: E501

        :return: The clicks of this InlineResponse20022Stat.  # noqa: E501
        :rtype: int
        """
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        """Sets the clicks of this InlineResponse20022Stat.

        Kolihestvo klikov  # noqa: E501

        :param clicks: The clicks of this InlineResponse20022Stat.  # noqa: E501
        :type: int
        """

        self._clicks = clicks

    @property
    def frq(self):
        """Gets the frq of this InlineResponse20022Stat.  # noqa: E501

        hastota (otnohenie kolihestva prosmotrov k kolihestvu unikalnyh polzovatelei)  # noqa: E501

        :return: The frq of this InlineResponse20022Stat.  # noqa: E501
        :rtype: int
        """
        return self._frq

    @frq.setter
    def frq(self, frq):
        """Sets the frq of this InlineResponse20022Stat.

        hastota (otnohenie kolihestva prosmotrov k kolihestvu unikalnyh polzovatelei)  # noqa: E501

        :param frq: The frq of this InlineResponse20022Stat.  # noqa: E501
        :type: int
        """

        self._frq = frq

    @property
    def ctr(self):
        """Gets the ctr of this InlineResponse20022Stat.  # noqa: E501

        Pokazatel klikabelnosti (otnohenie hisla klikov k kolihestvu pokazov. Vyrahaetsa v procentah).   # noqa: E501

        :return: The ctr of this InlineResponse20022Stat.  # noqa: E501
        :rtype: float
        """
        return self._ctr

    @ctr.setter
    def ctr(self, ctr):
        """Sets the ctr of this InlineResponse20022Stat.

        Pokazatel klikabelnosti (otnohenie hisla klikov k kolihestvu pokazov. Vyrahaetsa v procentah).   # noqa: E501

        :param ctr: The ctr of this InlineResponse20022Stat.  # noqa: E501
        :type: float
        """

        self._ctr = ctr

    @property
    def cpc(self):
        """Gets the cpc of this InlineResponse20022Stat.  # noqa: E501

        Stoimost klika, ₽  # noqa: E501

        :return: The cpc of this InlineResponse20022Stat.  # noqa: E501
        :rtype: float
        """
        return self._cpc

    @cpc.setter
    def cpc(self, cpc):
        """Sets the cpc of this InlineResponse20022Stat.

        Stoimost klika, ₽  # noqa: E501

        :param cpc: The cpc of this InlineResponse20022Stat.  # noqa: E501
        :type: float
        """

        self._cpc = cpc

    @property
    def duration(self):
        """Gets the duration of this InlineResponse20022Stat.  # noqa: E501

        Dlitelnost kampanii, v sekundah  # noqa: E501

        :return: The duration of this InlineResponse20022Stat.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse20022Stat.

        Dlitelnost kampanii, v sekundah  # noqa: E501

        :param duration: The duration of this InlineResponse20022Stat.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def sum(self):
        """Gets the sum of this InlineResponse20022Stat.  # noqa: E501

        Zatraty, ₽.  # noqa: E501

        :return: The sum of this InlineResponse20022Stat.  # noqa: E501
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this InlineResponse20022Stat.

        Zatraty, ₽.  # noqa: E501

        :param sum: The sum of this InlineResponse20022Stat.  # noqa: E501
        :type: float
        """

        self._sum = sum

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
        if issubclass(InlineResponse20022Stat, dict):
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
        if not isinstance(other, InlineResponse20022Stat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other