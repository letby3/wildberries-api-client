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


class MediafailyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def content_v2_media_file_post(self, uploadfile, x_vendor_code, x_photo_number, **kwargs):  # noqa: E501
        """Dobavlenie media kontenta v KT  # noqa: E501

        Metod pozvolaet zagruzit i dobavit odin mediafail za zapros, k NM v KT. <br>Trebovania k mediafailam: <br>`Foto`: minimalnoe razrehenie – 700x900. <br>Maksimalno dopustimoe kolihestvo foto v KT 30. <br>Dopustimye formaty izobrahenii - jpg i png. <br>Minimalnyi uroven kahestva izobrahenia - 65%.   <br>`Video`: maksimalnyi razmer 50 mb. Formaty MOV, MP4. <br>Maksimalno dopustimoe kolihestvo video v KT 1.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_media_file_post(uploadfile, x_vendor_code, x_photo_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uploadfile: (required)
        :param str x_vendor_code: Artikul prodavca (required)
        :param int x_photo_number: Nomer mediafaila na zagruzku. <b>Nahinat s 1</b>.<br>Pri zagruzke video vsegda ukazyvat znahenie 1. <br>htoby dobavit foto k uhe zagruhennym v NM, nomer mediafaila dolhen byt bolhe kol-va zagruhennyh v NM mediafailov.  (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_v2_media_file_post_with_http_info(uploadfile, x_vendor_code, x_photo_number, **kwargs)  # noqa: E501
        else:
            (data) = self.content_v2_media_file_post_with_http_info(uploadfile, x_vendor_code, x_photo_number, **kwargs)  # noqa: E501
            return data

    def content_v2_media_file_post_with_http_info(self, uploadfile, x_vendor_code, x_photo_number, **kwargs):  # noqa: E501
        """Dobavlenie media kontenta v KT  # noqa: E501

        Metod pozvolaet zagruzit i dobavit odin mediafail za zapros, k NM v KT. <br>Trebovania k mediafailam: <br>`Foto`: minimalnoe razrehenie – 700x900. <br>Maksimalno dopustimoe kolihestvo foto v KT 30. <br>Dopustimye formaty izobrahenii - jpg i png. <br>Minimalnyi uroven kahestva izobrahenia - 65%.   <br>`Video`: maksimalnyi razmer 50 mb. Formaty MOV, MP4. <br>Maksimalno dopustimoe kolihestvo video v KT 1.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_media_file_post_with_http_info(uploadfile, x_vendor_code, x_photo_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uploadfile: (required)
        :param str x_vendor_code: Artikul prodavca (required)
        :param int x_photo_number: Nomer mediafaila na zagruzku. <b>Nahinat s 1</b>.<br>Pri zagruzke video vsegda ukazyvat znahenie 1. <br>htoby dobavit foto k uhe zagruhennym v NM, nomer mediafaila dolhen byt bolhe kol-va zagruhennyh v NM mediafailov.  (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uploadfile', 'x_vendor_code', 'x_photo_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_v2_media_file_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uploadfile' is set
        if ('uploadfile' not in params or
                params['uploadfile'] is None):
            raise ValueError("Missing the required parameter `uploadfile` when calling `content_v2_media_file_post`")  # noqa: E501
        # verify the required parameter 'x_vendor_code' is set
        if ('x_vendor_code' not in params or
                params['x_vendor_code'] is None):
            raise ValueError("Missing the required parameter `x_vendor_code` when calling `content_v2_media_file_post`")  # noqa: E501
        # verify the required parameter 'x_photo_number' is set
        if ('x_photo_number' not in params or
                params['x_photo_number'] is None):
            raise ValueError("Missing the required parameter `x_photo_number` when calling `content_v2_media_file_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_vendor_code' in params:
            header_params['X-Vendor-Code'] = params['x_vendor_code']  # noqa: E501
        if 'x_photo_number' in params:
            header_params['X-Photo-Number'] = params['x_photo_number']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'uploadfile' in params:
            local_var_files['uploadfile'] = params['uploadfile']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/content/v2/media/file', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_v2_media_save_post(self, body, **kwargs):  # noqa: E501
        """Izmenenie media kontenta KT  # noqa: E501

        Metod pozvolaet izmenit poradok izobrahenii ili udalit mediafaily s NM v KT, a takhe zagruzit izobrahenia v NM so storonnih resursov po URL. <br>Tekuhie izobrahenia zamenautsa na peredannye v massive data. <br> <br>Trebovania k mediafailam: <br>`Foto`: minimalnoe razrehenie – 700x900. <br>Maksimalno dopustimoe kolihestvo foto v KT 30.  <br>Dopustimye formaty izobrahenii - jpg i png. <br>Minimalnyi uroven kahestva izobrahenia - 65%.  <br> <br>Esli hota by odno izobrahenie v zaprose ne sootvetstvuet trebovaniam k mediafailam, to dahe pri kode otveta 200 ni odno izobrahenie ne zagruzitsa v KT.<br>  <br>`VAhNO!` Vse, hto peredaetsa v massive `data` polnostu zamenaet soboi soderhimoe massiva `mediaFiles` v KT. <br>Esli Vy dobavlaete foto k uhe imeuhimsa v KT, to vmeste s novymi peredaite v zaprose vse ssylki na foto i video, kotorye uhe soderhatsa v KT. V protivnom sluhae v kartohke okahutsa tolko peredavaemye foto.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_media_save_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MediaSaveBody1 body: (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_v2_media_save_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.content_v2_media_save_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def content_v2_media_save_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Izmenenie media kontenta KT  # noqa: E501

        Metod pozvolaet izmenit poradok izobrahenii ili udalit mediafaily s NM v KT, a takhe zagruzit izobrahenia v NM so storonnih resursov po URL. <br>Tekuhie izobrahenia zamenautsa na peredannye v massive data. <br> <br>Trebovania k mediafailam: <br>`Foto`: minimalnoe razrehenie – 700x900. <br>Maksimalno dopustimoe kolihestvo foto v KT 30.  <br>Dopustimye formaty izobrahenii - jpg i png. <br>Minimalnyi uroven kahestva izobrahenia - 65%.  <br> <br>Esli hota by odno izobrahenie v zaprose ne sootvetstvuet trebovaniam k mediafailam, to dahe pri kode otveta 200 ni odno izobrahenie ne zagruzitsa v KT.<br>  <br>`VAhNO!` Vse, hto peredaetsa v massive `data` polnostu zamenaet soboi soderhimoe massiva `mediaFiles` v KT. <br>Esli Vy dobavlaete foto k uhe imeuhimsa v KT, to vmeste s novymi peredaite v zaprose vse ssylki na foto i video, kotorye uhe soderhatsa v KT. V protivnom sluhae v kartohke okahutsa tolko peredavaemye foto.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v2_media_save_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MediaSaveBody1 body: (required)
        :return: InlineResponse20013
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
                    " to method content_v2_media_save_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `content_v2_media_save_post`")  # noqa: E501

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
            '/content/v2/media/save', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_v3_media_file_post(self, uploadfile, x_nm_id, x_photo_number, **kwargs):  # noqa: E501
        """Dobavit mediafaily  # noqa: E501

        Dobavlaet odin mediafail dla tovara (nomenklatury).  Trebovania k izobraheniam:    * maksimum izobrahenii dla odnogo tovara (nomenklatury) — 30;   * minimalnoe razrehenie – 700 × 900 pikselei;   * minimalnoe kahestvo — 65%;   * formaty — JPG, PNG, BMP, GIF, WebP.  Trebovania k video:    * maksimum 1 video dla odnogo tovara (nomenklatury);   * maksimalnyi razmer — 50 Mb;   * formaty — MOV, MP4.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v3_media_file_post(uploadfile, x_nm_id, x_photo_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uploadfile: (required)
        :param str x_nm_id: Artikul Wildberries (required)
        :param int x_photo_number: Nomer mediafaila na zagruzku, nahinaetsa s `1`. Pri zagruzke video vsegda ukazyvaite `1`.  htoby dobavit izobrahenie k uhe zagruhennym, nomer mediafaila dolhen byt bolhe kolihestva uhe zagruhennyh mediafailov.  (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_v3_media_file_post_with_http_info(uploadfile, x_nm_id, x_photo_number, **kwargs)  # noqa: E501
        else:
            (data) = self.content_v3_media_file_post_with_http_info(uploadfile, x_nm_id, x_photo_number, **kwargs)  # noqa: E501
            return data

    def content_v3_media_file_post_with_http_info(self, uploadfile, x_nm_id, x_photo_number, **kwargs):  # noqa: E501
        """Dobavit mediafaily  # noqa: E501

        Dobavlaet odin mediafail dla tovara (nomenklatury).  Trebovania k izobraheniam:    * maksimum izobrahenii dla odnogo tovara (nomenklatury) — 30;   * minimalnoe razrehenie – 700 × 900 pikselei;   * minimalnoe kahestvo — 65%;   * formaty — JPG, PNG, BMP, GIF, WebP.  Trebovania k video:    * maksimum 1 video dla odnogo tovara (nomenklatury);   * maksimalnyi razmer — 50 Mb;   * formaty — MOV, MP4.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v3_media_file_post_with_http_info(uploadfile, x_nm_id, x_photo_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uploadfile: (required)
        :param str x_nm_id: Artikul Wildberries (required)
        :param int x_photo_number: Nomer mediafaila na zagruzku, nahinaetsa s `1`. Pri zagruzke video vsegda ukazyvaite `1`.  htoby dobavit izobrahenie k uhe zagruhennym, nomer mediafaila dolhen byt bolhe kolihestva uhe zagruhennyh mediafailov.  (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uploadfile', 'x_nm_id', 'x_photo_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_v3_media_file_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uploadfile' is set
        if ('uploadfile' not in params or
                params['uploadfile'] is None):
            raise ValueError("Missing the required parameter `uploadfile` when calling `content_v3_media_file_post`")  # noqa: E501
        # verify the required parameter 'x_nm_id' is set
        if ('x_nm_id' not in params or
                params['x_nm_id'] is None):
            raise ValueError("Missing the required parameter `x_nm_id` when calling `content_v3_media_file_post`")  # noqa: E501
        # verify the required parameter 'x_photo_number' is set
        if ('x_photo_number' not in params or
                params['x_photo_number'] is None):
            raise ValueError("Missing the required parameter `x_photo_number` when calling `content_v3_media_file_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_nm_id' in params:
            header_params['X-Nm-Id'] = params['x_nm_id']  # noqa: E501
        if 'x_photo_number' in params:
            header_params['X-Photo-Number'] = params['x_photo_number']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'uploadfile' in params:
            local_var_files['uploadfile'] = params['uploadfile']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HeaderApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/content/v3/media/file', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_v3_media_save_post(self, body, **kwargs):  # noqa: E501
        """Izmenit mediafaily  # noqa: E501

        Izmenaet nabor mediafailov dla tovara (nomenklatury).  **Vnimanie**. Novye mediafaily (`data`) polnostu zamenaut starye (`mediaFiles`). htoby dobavit novye mediafaily, ukahite ssylki ne tolko na nih, no i na starye faily.    Trebovania k izobraheniam:     * maksimum izobrahenii dla odnogo tovara (nomenklatury) — 30;   * minimalnoe razrehenie – 700 × 900 pikselei;   * minimalnoe kahestvo — 65%;   * formaty — JPG, PNG, BMP, GIF, WebP.   Trebovania k video:     * maksimum 1 video dla odnogo tovara (nomenklatury).   * maksimalnyi razmer — 50 Mb;   * formaty — MOV, MP4.   Esli hota by odno izobrahenie v zaprose ne sootvetstvuet trebovaniam, to dahe pri uspehnom otvete (200) ni odno izobrahenie ne zagruzitsa   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v3_media_save_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MediaSaveBody body: (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_v3_media_save_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.content_v3_media_save_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def content_v3_media_save_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Izmenit mediafaily  # noqa: E501

        Izmenaet nabor mediafailov dla tovara (nomenklatury).  **Vnimanie**. Novye mediafaily (`data`) polnostu zamenaut starye (`mediaFiles`). htoby dobavit novye mediafaily, ukahite ssylki ne tolko na nih, no i na starye faily.    Trebovania k izobraheniam:     * maksimum izobrahenii dla odnogo tovara (nomenklatury) — 30;   * minimalnoe razrehenie – 700 × 900 pikselei;   * minimalnoe kahestvo — 65%;   * formaty — JPG, PNG, BMP, GIF, WebP.   Trebovania k video:     * maksimum 1 video dla odnogo tovara (nomenklatury).   * maksimalnyi razmer — 50 Mb;   * formaty — MOV, MP4.   Esli hota by odno izobrahenie v zaprose ne sootvetstvuet trebovaniam, to dahe pri uspehnom otvete (200) ni odno izobrahenie ne zagruzitsa   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_v3_media_save_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MediaSaveBody body: (required)
        :return: InlineResponse20013
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
                    " to method content_v3_media_save_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `content_v3_media_save_post`")  # noqa: E501

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
            '/content/v3/media/save', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)