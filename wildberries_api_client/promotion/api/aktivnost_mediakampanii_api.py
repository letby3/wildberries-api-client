# coding: utf-8

"""
    Opisanie API Prodvihenie

    Sinhronizacia dannyh iz bd proishodit raz v 3 minuty.  <br>Izmenenie statusa proishodit raz v 1 minutu. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu statusa. <br>Izmenenie stavki proishodit raz v 30 sekund. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu stavki.   # noqa: E501

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wildberries_api_client.promotion.api_client import ApiClient


class AktivnostMediakampaniiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def adv_v1_advert_pause_post(self, body, **kwargs):  # noqa: E501
        """Priostanovka mediakampanii  # noqa: E501

        Metod pozvolaet priostanavlivat mediakampanii. <span class=\"newM\">new</span><br>  Perevodit priostanavlivaemuu mediakampaniu v status `9`.<br> Dopuskaetsa maksimum 10 zaprosov v minutu. <br>  `Vahno:` priostanovit mediakampaniu mohno ne bolhe 10 raz v sutki. Sutki otshityvautsa s polunohi po Moskovskomu vremeni. <br>         <dl> <dt>Statusy, v kotoryh dla mediakampanii dostupna priostanovka:</dt>   <dd><code>4</code> — odobreno</dd>   <dd><code>5</code> — zaplanirovano</dd>   <dd><code>6</code> — na pokazah</dd>   <dd><code>10</code> — pauza po dnevnomu limitu</dd>   <dd><code>11</code> — pauza po rashodu budheta</dd> </dl>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_advert_pause_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdvertPauseBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_advert_pause_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_advert_pause_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def adv_v1_advert_pause_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Priostanovka mediakampanii  # noqa: E501

        Metod pozvolaet priostanavlivat mediakampanii. <span class=\"newM\">new</span><br>  Perevodit priostanavlivaemuu mediakampaniu v status `9`.<br> Dopuskaetsa maksimum 10 zaprosov v minutu. <br>  `Vahno:` priostanovit mediakampaniu mohno ne bolhe 10 raz v sutki. Sutki otshityvautsa s polunohi po Moskovskomu vremeni. <br>         <dl> <dt>Statusy, v kotoryh dla mediakampanii dostupna priostanovka:</dt>   <dd><code>4</code> — odobreno</dd>   <dd><code>5</code> — zaplanirovano</dd>   <dd><code>6</code> — na pokazah</dd>   <dd><code>10</code> — pauza po dnevnomu limitu</dd>   <dd><code>11</code> — pauza po rashodu budheta</dd> </dl>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_advert_pause_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdvertPauseBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_advert_pause_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `adv_v1_advert_pause_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v1/advert/pause', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_advert_start_post(self, body, **kwargs):  # noqa: E501
        """Zapusk mediakampanii  # noqa: E501

        Metod pozvolaet zapuskat priostanovlennye mediakampanii. <span class=\"newM\">new</span> <br> Posle zapuska kampania v tehenie 2-5 minut budet nahoditsa v statuse `4`, posle hego status budet izmenen na aktualnyi, v zavisimosti ot konfiguracii mediakampanii. <br>  Dopuskaetsa maksimum 10 zaprosov v minutu. <dl> <dt>Statusy, v kotoryh dla mediakampanii dostupen zapusk:</dt>   <dd><code>9</code> - priostanovlena prodavcom</dd>   <dd><code>11</code> - pauza po rashodu budheta</dd> </dl>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_advert_start_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdvertStartBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_advert_start_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_advert_start_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def adv_v1_advert_start_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Zapusk mediakampanii  # noqa: E501

        Metod pozvolaet zapuskat priostanovlennye mediakampanii. <span class=\"newM\">new</span> <br> Posle zapuska kampania v tehenie 2-5 minut budet nahoditsa v statuse `4`, posle hego status budet izmenen na aktualnyi, v zavisimosti ot konfiguracii mediakampanii. <br>  Dopuskaetsa maksimum 10 zaprosov v minutu. <dl> <dt>Statusy, v kotoryh dla mediakampanii dostupen zapusk:</dt>   <dd><code>9</code> - priostanovlena prodavcom</dd>   <dd><code>11</code> - pauza po rashodu budheta</dd> </dl>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_advert_start_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdvertStartBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_advert_start_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `adv_v1_advert_start_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v1/advert/start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_advert_stop_post(self, body, **kwargs):  # noqa: E501
        """Zaverhenie mediakampanii  # noqa: E501

        Metod zaverhaet mediakampaniu - perevodit ee v status `7`. <span class=\"newM\">new</span> <br>  Dopuskaetsa maksimum 10 zaprosov v minutu. <dl> <dt>Statusy, v kotoryh dla mediakampanii dostupno zaverhenie:</dt>   <dd><code>1</code> - hernovik</dd>   <dd><code>3</code> - otkloneno (s vozmohnostu vernut na moderaciu)</dd>   <dd><code>4</code> - odobreno</dd>   <dd><code>5</code> - zaplanirovano</dd>   <dd><code>6</code> - na pokazah</dd>   <dd><code>8</code> - otkazalsa</dd>   <dd><code>9</code> - priostanovlena prodavcom</dd>   <dd><code>10</code> - pauza po dnevnomu limitu</dd>   <dd><code>11</code> - pauza po rashodu budheta</dd> </dl>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_advert_stop_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdvertStopBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_advert_stop_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_advert_stop_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def adv_v1_advert_stop_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Zaverhenie mediakampanii  # noqa: E501

        Metod zaverhaet mediakampaniu - perevodit ee v status `7`. <span class=\"newM\">new</span> <br>  Dopuskaetsa maksimum 10 zaprosov v minutu. <dl> <dt>Statusy, v kotoryh dla mediakampanii dostupno zaverhenie:</dt>   <dd><code>1</code> - hernovik</dd>   <dd><code>3</code> - otkloneno (s vozmohnostu vernut na moderaciu)</dd>   <dd><code>4</code> - odobreno</dd>   <dd><code>5</code> - zaplanirovano</dd>   <dd><code>6</code> - na pokazah</dd>   <dd><code>8</code> - otkazalsa</dd>   <dd><code>9</code> - priostanovlena prodavcom</dd>   <dd><code>10</code> - pauza po dnevnomu limitu</dd>   <dd><code>11</code> - pauza po rashodu budheta</dd> </dl>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_advert_stop_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdvertStopBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_advert_stop_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `adv_v1_advert_stop_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v1/advert/stop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
