# coding: utf-8

"""
    Opisanie API Kontenta

     <dl> <dt>Slovar sokrahenii:</dt> <dd>KT — kartohka tovara</dd> <dd>NM—- nomenklatura</dd> </dl> Ogranihenia po kolihestvu zaprosov: <dd>Dopuskaetsa maksimum 100 zaprosov v minutu na metody kontenta v celom.</dd> <br> Publihnoe API Kontenta sozdano dla sinhronizacii dannyh mehdu serverami Wildberries i serverami prodavcov. <br> Vy zagruhaete dannye na svoi nositeli, rabotaete s nimi na svoih mohnostah i sinhroniziruetes s nahimi serverami po mere neobhodimosti. <br> <code>Ne dopuskaetsa ispolzovanie API Kontenta v kahestve vnehnei bazy dannyh. Pri prevyhenii limitov na zaprosy dostup k API budet ogranihen.</code> <br> <br> <br>   # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wildberries_api_client.content.api_client import ApiClient


class TegiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def content_v2_tag_id_delete(self, id, **kwargs):  # noqa: E501
        """Udalenie tega  # noqa: E501

        Metod pozvolaet udalit teg.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tag_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: hislovoi identifikator tega (required)
        :return: InlineResponse20015
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_v2_tag_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.content_v2_tag_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def content_v2_tag_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Udalenie tega  # noqa: E501

        Metod pozvolaet udalit teg.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tag_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: hislovoi identifikator tega (required)
        :return: InlineResponse20015
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
                    " to method content_v2_tag_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `content_v2_tag_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/content/v2/tag/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20015',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_v2_tag_id_patch(self, body, id, **kwargs):  # noqa: E501
        """Izmenenie tega  # noqa: E501

        Metod pozvolaet izmenat informaciu o tege (ima i cvet).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tag_id_patch(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagIdBody body: (required)
        :param int id: hislovoi identifikator tega (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_v2_tag_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.content_v2_tag_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def content_v2_tag_id_patch_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Izmenenie tega  # noqa: E501

        Metod pozvolaet izmenat informaciu o tege (ima i cvet).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tag_id_patch_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagIdBody body: (required)
        :param int id: hislovoi identifikator tega (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_v2_tag_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `content_v2_tag_id_patch`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `content_v2_tag_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/content/v2/tag/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_v2_tag_nomenclature_link_post(self, body, **kwargs):  # noqa: E501
        """Upravlenie tegami v KT  # noqa: E501

        Metod pozvolaet dobavit tegi k KT i snat ih s KT.<br> Pri snatii tega s KT sam teg ne udalaetsa.<br> K kartohke mohno dobavit 15 tegov.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tag_nomenclature_link_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NomenclatureLinkBody body: (required)
        :return: ResponseContentError6
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_v2_tag_nomenclature_link_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.content_v2_tag_nomenclature_link_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def content_v2_tag_nomenclature_link_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Upravlenie tegami v KT  # noqa: E501

        Metod pozvolaet dobavit tegi k KT i snat ih s KT.<br> Pri snatii tega s KT sam teg ne udalaetsa.<br> K kartohke mohno dobavit 15 tegov.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tag_nomenclature_link_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NomenclatureLinkBody body: (required)
        :return: ResponseContentError6
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
                    " to method content_v2_tag_nomenclature_link_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `content_v2_tag_nomenclature_link_post`")  # noqa: E501

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
            '/content/v2/tag/nomenclature/link', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContentError6',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_v2_tag_post(self, body, **kwargs):  # noqa: E501
        """Sozdanie tega  # noqa: E501

        Metod pozvolaet sozdat teg.<br> Zavesti mohno 15 tegov.<br> Maksimalnaa dlina tega 15 simvolov.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tag_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V2TagBody body: (required)
        :return: ResponseContentError6
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_v2_tag_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.content_v2_tag_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def content_v2_tag_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Sozdanie tega  # noqa: E501

        Metod pozvolaet sozdat teg.<br> Zavesti mohno 15 tegov.<br> Maksimalnaa dlina tega 15 simvolov.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tag_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V2TagBody body: (required)
        :return: ResponseContentError6
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
                    " to method content_v2_tag_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `content_v2_tag_post`")  # noqa: E501

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
            '/content/v2/tag', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContentError6',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_v2_tags_get(self, **kwargs):  # noqa: E501
        """Spisok tegov  # noqa: E501

        Metod pozvolaet poluhit spisok suhestvuuhih tegov prodavca.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tags_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_v2_tags_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.content_v2_tags_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def content_v2_tags_get_with_http_info(self, **kwargs):  # noqa: E501
        """Spisok tegov  # noqa: E501

        Metod pozvolaet poluhit spisok suhestvuuhih tegov prodavca.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_tags_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20014
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
                    " to method content_v2_tags_get" % key
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
            '/content/v2/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)