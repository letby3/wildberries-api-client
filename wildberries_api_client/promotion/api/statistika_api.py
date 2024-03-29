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


class StatistikaApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def adv_v1_auto_stat_get(self, id, **kwargs):  # noqa: E501
        """Statistika avtomatiheskoi kampanii  # noqa: E501

        Metod pozvolaet poluhat kratkuu statistiku po avtomatiheskoi kampanii. <br> Dopuskaetsa 1 zapros v 6 sekund.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_auto_stat_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_auto_stat_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_auto_stat_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def adv_v1_auto_stat_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Statistika avtomatiheskoi kampanii  # noqa: E501

        Metod pozvolaet poluhat kratkuu statistiku po avtomatiheskoi kampanii. <br> Dopuskaetsa 1 zapros v 6 sekund.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_auto_stat_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_auto_stat_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `adv_v1_auto_stat_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v1/auto/stat', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20019',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_auto_stat_words_get(self, id, **kwargs):  # noqa: E501
        """Statistika avtomatiheskoi kampanii po kluhevym frazam  # noqa: E501

        Metod pozvolaet poluhat statistiku avtomatiheskoi kampanii po kluhevym frazam. <br> Dopuskaetsa 1 zapros v sekundu.<br>  Informacia obnovlaetsa primerno kahdye polhasa. <br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_auto_stat_words_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_auto_stat_words_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_auto_stat_words_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def adv_v1_auto_stat_words_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Statistika avtomatiheskoi kampanii po kluhevym frazam  # noqa: E501

        Metod pozvolaet poluhat statistiku avtomatiheskoi kampanii po kluhevym frazam. <br> Dopuskaetsa 1 zapros v sekundu.<br>  Informacia obnovlaetsa primerno kahdye polhasa. <br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_auto_stat_words_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_auto_stat_words_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `adv_v1_auto_stat_words_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v1/auto/stat-words', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20023',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_fullstat_get(self, id, **kwargs):  # noqa: E501
        """Polnaa statistika kampanii  # noqa: E501

        Metod pozvolaet poluhat rashirennuu statistku kampanii, razdelennuu po dnam, nomenklaturam i platformam (sait, android, IOS). <br> Dopuskaetsa 1 zapros v 6 sekund.<br>  Informacia obnovlaetsa ne rehe odnogo raza v dva hasa.<br> <br> <b>Metod budet otkluhen 25 dekabra</b>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_fullstat_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :param str begin: Nahalo zaprahivaemogo perioda
        :param str end: Konec zaprahivaemogo perioda
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_fullstat_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_fullstat_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def adv_v1_fullstat_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Polnaa statistika kampanii  # noqa: E501

        Metod pozvolaet poluhat rashirennuu statistku kampanii, razdelennuu po dnam, nomenklaturam i platformam (sait, android, IOS). <br> Dopuskaetsa 1 zapros v 6 sekund.<br>  Informacia obnovlaetsa ne rehe odnogo raza v dva hasa.<br> <br> <b>Metod budet otkluhen 25 dekabra</b>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_fullstat_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :param str begin: Nahalo zaprahivaemogo perioda
        :param str end: Konec zaprahivaemogo perioda
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'begin', 'end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_fullstat_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `adv_v1_fullstat_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'begin' in params:
            query_params.append(('begin', params['begin']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v1/fullstat', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20024',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_fullstats_post(self, body, **kwargs):  # noqa: E501
        """Statistika kampanii  # noqa: E501

        Metod rabotaet analogihno metodu \"Polnaa statistika kampanii\". <br> Dopuskaetsa 1 zapros v minutu.  <br> `Vahno`! V zaprose neobhodimo peredavat libo parametr `dates` libo parametr `interval`, no ne oba. <br> Pri zaprose bez parametrov `dates` i `interval` vernutsa dannye za vse vrema pokazov kampanii. <br> <br> <b>Metod budet otkluhen 25 dekabra</b>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_fullstats_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1FullstatsBody body: (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_fullstats_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_fullstats_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def adv_v1_fullstats_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Statistika kampanii  # noqa: E501

        Metod rabotaet analogihno metodu \"Polnaa statistika kampanii\". <br> Dopuskaetsa 1 zapros v minutu.  <br> `Vahno`! V zaprose neobhodimo peredavat libo parametr `dates` libo parametr `interval`, no ne oba. <br> Pri zaprose bez parametrov `dates` i `interval` vernutsa dannye za vse vrema pokazov kampanii. <br> <br> <b>Metod budet otkluhen 25 dekabra</b>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_fullstats_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1FullstatsBody body: (required)
        :return: InlineResponse20018
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
                    " to method adv_v1_fullstats_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `adv_v1_fullstats_post`")  # noqa: E501

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
            '/adv/v1/fullstats', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_seacat_stat_get(self, id, **kwargs):  # noqa: E501
        """Statistika kampanii Poisk + Katalog  # noqa: E501

        Metod pozvolaet poluhat statistiku po kampaniam Poisk + Katalog. <br> Dopuskaetsa 2 zaprosa v sekundu.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_seacat_stat_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20025
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_seacat_stat_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_seacat_stat_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def adv_v1_seacat_stat_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Statistika kampanii Poisk + Katalog  # noqa: E501

        Metod pozvolaet poluhat statistiku po kampaniam Poisk + Katalog. <br> Dopuskaetsa 2 zaprosa v sekundu.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_seacat_stat_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20025
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_seacat_stat_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `adv_v1_seacat_stat_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v1/seacat/stat', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20025',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_stat_words_get(self, id, **kwargs):  # noqa: E501
        """Statistika poiskovoi kampanii po kluhevym frazam  # noqa: E501

        Metod pozvolaet poluhat statistiku poiskovoi kampanii po kluhevym frazam.<br> Dopuskaetsa maksimum 4 zaprosa v sekundu.<br>  Informacia obnovlaetsa primerno kahdye polhasa. <br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_stat_words_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_stat_words_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_stat_words_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def adv_v1_stat_words_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Statistika poiskovoi kampanii po kluhevym frazam  # noqa: E501

        Metod pozvolaet poluhat statistiku poiskovoi kampanii po kluhevym frazam.<br> Dopuskaetsa maksimum 4 zaprosa v sekundu.<br>  Informacia obnovlaetsa primerno kahdye polhasa. <br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_stat_words_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_stat_words_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `adv_v1_stat_words_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v1/stat/words', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20022',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v2_auto_daily_words_get(self, id, **kwargs):  # noqa: E501
        """Detalnaa statistika avtomatiheskoi kampanii po kluhevym frazam  # noqa: E501

        <p>Vozvrahaet statistiku po kluhevym frazam za kahdyi den, kogda kampania byla aktivna.</p> <p>Informacia obnovlaetsa raz v 15 minut.</p> <p>Maksimum — 4 zaprosa sekundu.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v2_auto_daily_words_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v2_auto_daily_words_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v2_auto_daily_words_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def adv_v2_auto_daily_words_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Detalnaa statistika avtomatiheskoi kampanii po kluhevym frazam  # noqa: E501

        <p>Vozvrahaet statistiku po kluhevym frazam za kahdyi den, kogda kampania byla aktivna.</p> <p>Informacia obnovlaetsa raz v 15 minut.</p> <p>Maksimum — 4 zaprosa sekundu.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v2_auto_daily_words_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v2_auto_daily_words_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `adv_v2_auto_daily_words_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v2/auto/daily-words', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20021',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v2_auto_stat_words_get(self, id, **kwargs):  # noqa: E501
        """Statistika avtomatiheskoi kampanii po klasteram fraz  # noqa: E501

        <p>Vozvrahaet klastery kluhevyh fraz (nabory pohohih), po kotorym pokazyvalis tovary v kampanii, i kolihestvo pokazov po nim. V otvet metoda popadaut tolko te frazy, po kotorym tovary pokazyvalis hota by odin raz.</p> <p>Informacia obnovlaetsa raz v 15 minut.</p> <p>Maksimum — 4 zaprosa sekundu.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v2_auto_stat_words_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v2_auto_stat_words_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v2_auto_stat_words_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def adv_v2_auto_stat_words_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Statistika avtomatiheskoi kampanii po klasteram fraz  # noqa: E501

        <p>Vozvrahaet klastery kluhevyh fraz (nabory pohohih), po kotorym pokazyvalis tovary v kampanii, i kolihestvo pokazov po nim. V otvet metoda popadaut tolko te frazy, po kotorym tovary pokazyvalis hota by odin raz.</p> <p>Informacia obnovlaetsa raz v 15 minut.</p> <p>Maksimum — 4 zaprosa sekundu.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v2_auto_stat_words_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifikator kampanii (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v2_auto_stat_words_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `adv_v2_auto_stat_words_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/adv/v2/auto/stat-words', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v2_fullstats_post(self, body, **kwargs):  # noqa: E501
        """Statistika kampanii  # noqa: E501

        Vozvrahaet statistiku kampanii. <span class=\"newM\">new</span> <br> Maksimum 1 zapros v minutu. <br> Dannye vernutsa dla kampanii v statuse 7, 9 i 11. <br> <b>Vahno</b>. V zaprose mohno peredavat libo parametr `dates` libo parametr `interval`, no ne oba.<br> Mohno otpravit zapros tolko s ID kampanii. Pri etom vernutsa dannye za poslednie sutki, no ne za ves period suhestvovania kampanii.   <br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v2_fullstats_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V2FullstatsBody body: (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v2_fullstats_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v2_fullstats_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def adv_v2_fullstats_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Statistika kampanii  # noqa: E501

        Vozvrahaet statistiku kampanii. <span class=\"newM\">new</span> <br> Maksimum 1 zapros v minutu. <br> Dannye vernutsa dla kampanii v statuse 7, 9 i 11. <br> <b>Vahno</b>. V zaprose mohno peredavat libo parametr `dates` libo parametr `interval`, no ne oba.<br> Mohno otpravit zapros tolko s ID kampanii. Pri etom vernutsa dannye za poslednie sutki, no ne za ves period suhestvovania kampanii.   <br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v2_fullstats_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V2FullstatsBody body: (required)
        :return: InlineResponse20018
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
                    " to method adv_v2_fullstats_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `adv_v2_fullstats_post`")  # noqa: E501

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
            '/adv/v2/fullstats', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
