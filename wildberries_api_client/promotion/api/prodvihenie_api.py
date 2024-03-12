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


class ProdvihenieApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def adv_v0_delete_get(self, id, **kwargs):  # noqa: E501
        """Udalenie kampanii  # noqa: E501

        Metod pozvolaet udalat kampanii v statuse <b>4 - gotova k zapusku</b>. <span class=\"newM\">new</span><br> <br> Dopuskaetsa 5 zaprosov v sekundu.<br>  Posle udalenia kampania nekotoroe vrema budet nahoditsa v <b>-1</b> statuse.<br> Polnoe udalenie kampanii zanimaet ot 3 do 10 minut.            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v0_delete_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID kampanii (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v0_delete_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v0_delete_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def adv_v0_delete_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Udalenie kampanii  # noqa: E501

        Metod pozvolaet udalat kampanii v statuse <b>4 - gotova k zapusku</b>. <span class=\"newM\">new</span><br> <br> Dopuskaetsa 5 zaprosov v sekundu.<br>  Posle udalenia kampania nekotoroe vrema budet nahoditsa v <b>-1</b> statuse.<br> Polnoe udalenie kampanii zanimaet ot 3 do 10 minut.            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v0_delete_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID kampanii (required)
        :return: None
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
                    " to method adv_v0_delete_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `adv_v0_delete_get`")  # noqa: E501

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
            '/adv/v0/delete', 'GET',
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

    def adv_v1_promotion_adverts_post(self, body, **kwargs):  # noqa: E501
        """Informacia o kampaniah  # noqa: E501

        Metod pozvolaet poluhat informaciu o kampaniah po query parametram, libo po spisku id kampanii. <span class=\"newM\">new</span> <br> Dopuskaetsa 5 zaprosov v sekundu.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_promotion_adverts_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] body: (required)
        :param int status: <dl> <dt>Status kampanii:</dt> <dd><code>-1</code> - kampania v processe udalenia <span class=\"new\">new</span></dd> <dd><code>4</code> - gotova k zapusku </dd> <dd><code>7</code> - kampania zaverhena</dd> <dd><code>8</code> - otkazalsa</dd> <dd><code>9</code> - idut pokazy</dd> <dd><code>11</code> - kampania na pauze</dd> </dl> Kampania v processe udalenia. Status oznahaet, hto kampania byla udalena, i herez 3-10 minut ona isheznet iz otveta metoda. 
        :param int type: <dl> <dt>Tip kampanii:</dt> <dd><code>4</code> - kampania v kataloge</dd> <dd><code>5</code> - kampania v kartohke tovara</dd> <dd><code>6</code> - kampania v poiske</dd> <dd><code>7</code> - kampania v rekomendaciah na glavnoi stranice</dd> <dd><code>8</code> - avtomatiheskaa kampania </dd> <dd><code>9</code> - poisk + katalog </dd> </dl> 
        :param str order: <dl> <dt>Poradok:</dt> <dd><code>create</code> (po vremeni sozdania kampanii)</dd> <dd><code>change</code> (po vremeni poslednego izmenenia kampanii)</dd> <dd><code>id</code> (po identifikatoru kampanii)</dd> </dl> <br>Naprimer: <code>/adv/v1/promotion/adverts?type=6&order=change&direction=asc</code> 
        :param str direction: <dl> <dt>Napravlenie:</dt> <dd><code>desc</code> (ot bolhego k menhemu)</dd> <dd><code>asc</code> (ot menhego k bolhemu)</dd> </dl> <br>Naprimer: <code>/adv/v1/promotion/adverts?type=6&order=change&<b>direction=asc</b></code> 
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_promotion_adverts_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_promotion_adverts_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def adv_v1_promotion_adverts_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Informacia o kampaniah  # noqa: E501

        Metod pozvolaet poluhat informaciu o kampaniah po query parametram, libo po spisku id kampanii. <span class=\"newM\">new</span> <br> Dopuskaetsa 5 zaprosov v sekundu.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_promotion_adverts_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] body: (required)
        :param int status: <dl> <dt>Status kampanii:</dt> <dd><code>-1</code> - kampania v processe udalenia <span class=\"new\">new</span></dd> <dd><code>4</code> - gotova k zapusku </dd> <dd><code>7</code> - kampania zaverhena</dd> <dd><code>8</code> - otkazalsa</dd> <dd><code>9</code> - idut pokazy</dd> <dd><code>11</code> - kampania na pauze</dd> </dl> Kampania v processe udalenia. Status oznahaet, hto kampania byla udalena, i herez 3-10 minut ona isheznet iz otveta metoda. 
        :param int type: <dl> <dt>Tip kampanii:</dt> <dd><code>4</code> - kampania v kataloge</dd> <dd><code>5</code> - kampania v kartohke tovara</dd> <dd><code>6</code> - kampania v poiske</dd> <dd><code>7</code> - kampania v rekomendaciah na glavnoi stranice</dd> <dd><code>8</code> - avtomatiheskaa kampania </dd> <dd><code>9</code> - poisk + katalog </dd> </dl> 
        :param str order: <dl> <dt>Poradok:</dt> <dd><code>create</code> (po vremeni sozdania kampanii)</dd> <dd><code>change</code> (po vremeni poslednego izmenenia kampanii)</dd> <dd><code>id</code> (po identifikatoru kampanii)</dd> </dl> <br>Naprimer: <code>/adv/v1/promotion/adverts?type=6&order=change&direction=asc</code> 
        :param str direction: <dl> <dt>Napravlenie:</dt> <dd><code>desc</code> (ot bolhego k menhemu)</dd> <dd><code>asc</code> (ot menhego k bolhemu)</dd> </dl> <br>Naprimer: <code>/adv/v1/promotion/adverts?type=6&order=change&<b>direction=asc</b></code> 
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'status', 'type', 'order', 'direction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_promotion_adverts_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `adv_v1_promotion_adverts_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'direction' in params:
            query_params.append(('direction', params['direction']))  # noqa: E501

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
            '/adv/v1/promotion/adverts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_promotion_count_get(self, **kwargs):  # noqa: E501
        """Spiski kampanii  # noqa: E501

        Metod pozvolaet poluhat spiski kampanii, sgruppirovannyh po tipu i statusu, s informaciei o date poslednego izmenenia kampanii. <span class=\"newM\">new</span> <br> Dopuskaetsa 5 zaprosov v sekundu.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_promotion_count_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_promotion_count_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_promotion_count_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def adv_v1_promotion_count_get_with_http_info(self, **kwargs):  # noqa: E501
        """Spiski kampanii  # noqa: E501

        Metod pozvolaet poluhat spiski kampanii, sgruppirovannyh po tipu i statusu, s informaciei o date poslednego izmenenia kampanii. <span class=\"newM\">new</span> <br> Dopuskaetsa 5 zaprosov v sekundu.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_promotion_count_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adv_v1_promotion_count_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/adv/v1/promotion/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_save_ad_post(self, body, **kwargs):  # noqa: E501
        """Sozdat avtomatiheskuu kampaniu  # noqa: E501

        Sozdaut avtomatiheskuu kampaniu.<br> Maksimum 1 zapros v 20 sekund.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_save_ad_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SaveadBody body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_save_ad_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_save_ad_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def adv_v1_save_ad_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Sozdat avtomatiheskuu kampaniu  # noqa: E501

        Sozdaut avtomatiheskuu kampaniu.<br> Maksimum 1 zapros v 20 sekund.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_save_ad_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SaveadBody body: (required)
        :return: str
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
                    " to method adv_v1_save_ad_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `adv_v1_save_ad_post`")  # noqa: E501

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
            '/adv/v1/save-ad', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adv_v1_search_save_ad_post(self, body, **kwargs):  # noqa: E501
        """Sozdat kampaniu v poiske  # noqa: E501

        Sozdaet kampaniu v poiske. <span class=\"newM\">new</span><br> Maksimum 1 zapros v minutu. <br> <br> Poradok raboty: <ol>   <li>Poluhit spisok predmetov metodom <b>\"Spisok predmetov dla kampanii v poiske\"</b>.</li>   <li>Po <code>id</code> nuhnogo predmeta iz pervogo punkta poluhit tovary, kotorye est v nalihii metodom <b>\"Spisok tovarov dla kampanii v poiske\"</b>.</li>   <li>Dobavit neobhodimye tovary v telo zaprosa dannogo metoda.</li> </ol>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_search_save_ad_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchSaveadBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v1_search_save_ad_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.adv_v1_search_save_ad_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def adv_v1_search_save_ad_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Sozdat kampaniu v poiske  # noqa: E501

        Sozdaet kampaniu v poiske. <span class=\"newM\">new</span><br> Maksimum 1 zapros v minutu. <br> <br> Poradok raboty: <ol>   <li>Poluhit spisok predmetov metodom <b>\"Spisok predmetov dla kampanii v poiske\"</b>.</li>   <li>Po <code>id</code> nuhnogo predmeta iz pervogo punkta poluhit tovary, kotorye est v nalihii metodom <b>\"Spisok tovarov dla kampanii v poiske\"</b>.</li>   <li>Dobavit neobhodimye tovary v telo zaprosa dannogo metoda.</li> </ol>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v1_search_save_ad_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchSaveadBody body: (required)
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
                    " to method adv_v1_search_save_ad_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `adv_v1_search_save_ad_post`")  # noqa: E501

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
            '/adv/v1/search/save-ad', 'POST',
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

    def adv_v2_seacat_save_ad_post(self, **kwargs):  # noqa: E501
        """Sozdat kampaniu Poisk + Katalog  # noqa: E501

        Sozdaet kampaniu Poisk + Katalog. <span class=\"newM\">new</span><br> Maksimum 5 zaprosov v minutu   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v2_seacat_save_ad_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SeacatSaveadBody body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adv_v2_seacat_save_ad_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.adv_v2_seacat_save_ad_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def adv_v2_seacat_save_ad_post_with_http_info(self, **kwargs):  # noqa: E501
        """Sozdat kampaniu Poisk + Katalog  # noqa: E501

        Sozdaet kampaniu Poisk + Katalog. <span class=\"newM\">new</span><br> Maksimum 5 zaprosov v minutu   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adv_v2_seacat_save_ad_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SeacatSaveadBody body:
        :return: int
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
                    " to method adv_v2_seacat_save_ad_post" % key
                )
            params[key] = val
        del params['kwargs']

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
            '/adv/v2/seacat/save-ad', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)