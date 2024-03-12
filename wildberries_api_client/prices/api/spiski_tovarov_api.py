# coding: utf-8

"""
    API cen i skidok

    S pomohu etih metodov mohno ustanavlivat ceny i skidki. Maksimum — 10 zaprosov za 6 sekund summarno dla vseh metodov.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wildberries_api_client.prices.api_client import ApiClient


class SpiskiTovarovApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v2_list_goods_filter_get(self, limit, **kwargs):  # noqa: E501
        """Poluhit tovary  # noqa: E501

        Vozvrahaet informaciu o tovare po ego artikulu. htoby poluhit informaciu obo vseh tovarah, ostavte artikul pustym  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_list_goods_filter_get(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Skolko elementov vyvesti na odnoi stranice (paginacia). Maksimum 1 000 elementov  (required)
        :param int offset: Skolko elementov propustit
        :param int filter_nm_id: Artikul Wildberries, po kotoromu iskat tovar 
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_list_goods_filter_get_with_http_info(limit, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_list_goods_filter_get_with_http_info(limit, **kwargs)  # noqa: E501
            return data

    def api_v2_list_goods_filter_get_with_http_info(self, limit, **kwargs):  # noqa: E501
        """Poluhit tovary  # noqa: E501

        Vozvrahaet informaciu o tovare po ego artikulu. htoby poluhit informaciu obo vseh tovarah, ostavte artikul pustym  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_list_goods_filter_get_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Skolko elementov vyvesti na odnoi stranice (paginacia). Maksimum 1 000 elementov  (required)
        :param int offset: Skolko elementov propustit
        :param int filter_nm_id: Artikul Wildberries, po kotoromu iskat tovar 
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'filter_nm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_list_goods_filter_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `api_v2_list_goods_filter_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'filter_nm_id' in params:
            query_params.append(('filterNmID', params['filter_nm_id']))  # noqa: E501

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
            '/api/v2/list/goods/filter', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_list_goods_size_nm_get(self, limit, nm_id, **kwargs):  # noqa: E501
        """Poluhit razmery tovara  # noqa: E501

        Vozvrahaet informaciu o vseh razmerah odnogo tovara. Rabotaet tolko dla tovarov iz kategorii, gde mohno ustanavlivat ceny otdelno dla raznyh razmerov. Dla takih tovarov v otvete metoda [Poluhit tovary po artikulam](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1size~1nm/get) `editableSizePrice: true`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_list_goods_size_nm_get(limit, nm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Skolko elementov vyvesti na odnoi stranice (paginacia). Maksimum 1 000 elementov  (required)
        :param int nm_id: Artikul Wildberries (required)
        :param int offset: Skolko elementov propustit
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_list_goods_size_nm_get_with_http_info(limit, nm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_list_goods_size_nm_get_with_http_info(limit, nm_id, **kwargs)  # noqa: E501
            return data

    def api_v2_list_goods_size_nm_get_with_http_info(self, limit, nm_id, **kwargs):  # noqa: E501
        """Poluhit razmery tovara  # noqa: E501

        Vozvrahaet informaciu o vseh razmerah odnogo tovara. Rabotaet tolko dla tovarov iz kategorii, gde mohno ustanavlivat ceny otdelno dla raznyh razmerov. Dla takih tovarov v otvete metoda [Poluhit tovary po artikulam](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1size~1nm/get) `editableSizePrice: true`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_list_goods_size_nm_get_with_http_info(limit, nm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Skolko elementov vyvesti na odnoi stranice (paginacia). Maksimum 1 000 elementov  (required)
        :param int nm_id: Artikul Wildberries (required)
        :param int offset: Skolko elementov propustit
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'nm_id', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_list_goods_size_nm_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `api_v2_list_goods_size_nm_get`")  # noqa: E501
        # verify the required parameter 'nm_id' is set
        if ('nm_id' not in params or
                params['nm_id'] is None):
            raise ValueError("Missing the required parameter `nm_id` when calling `api_v2_list_goods_size_nm_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'nm_id' in params:
            query_params.append(('nmID', params['nm_id']))  # noqa: E501

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
            '/api/v2/list/goods/size/nm', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
