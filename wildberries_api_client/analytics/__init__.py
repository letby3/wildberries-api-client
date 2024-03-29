# coding: utf-8

# flake8: noqa

"""
    Opisanie API Analitika

    **Servis predostavlaet publihnyi API dla poluhenia analitiheskih dannyh.**          Analitiheskie dannye v istohnike hranatsa za poslednii god, pri vybore daty nahala perioda ranee hem god nazad, budet   vozvrahatsa ohibka, takim obrazom maksimalnoe kol-vo dnei v agregaciah — 365.  Takhe v dannyh, gde predostavlaetsa informacia po predyduhemu periodu:   1. V `previousPeriod` dannye za takoi he period, hto i v `selectedPeriod`.   2. Esli data nahala `previousPeriod` ranee, hem god nazad ot tekuhei daty, ona budet privedena k vidu:      `previousPeriod.start = tekuhaa data - 365 dnei.`  #### Taimzony  Format IANA, aktualnyi spisok mohno posmotret [zdes](https://nodatime.org/TimeZones). <br> <br> <br>   # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from wildberries_api_client.analytics.api.othety_pouderhaniam_api import OthetyPouderhaniamApi
from wildberries_api_client.analytics.api.platnoe_hranenie_api import PlatnoeHranenieApi
from wildberries_api_client.analytics.api.tovary_sobazatelnoi_markirovkoi_api import TovarySobazatelnoiMarkirovkoiApi
from wildberries_api_client.analytics.api.voronka_prodah_api import VoronkaProdahApi
# import ApiClient
from wildberries_api_client.analytics.api_client import ApiClient
from wildberries_api_client.analytics.configuration import Configuration
# import models into sdk package
from wildberries_api_client.analytics.models.create_task_request import CreateTaskRequest
from wildberries_api_client.analytics.models.create_task_request_paid_storage import CreateTaskRequestPaidStorage
from wildberries_api_client.analytics.models.create_task_request_paid_storage_params import CreateTaskRequestPaidStorageParams
from wildberries_api_client.analytics.models.create_task_response import CreateTaskResponse
from wildberries_api_client.analytics.models.create_task_response_data import CreateTaskResponseData
from wildberries_api_client.analytics.models.error_response import ErrorResponse
from wildberries_api_client.analytics.models.excise_report_request import ExciseReportRequest
from wildberries_api_client.analytics.models.excise_report_response import ExciseReportResponse
from wildberries_api_client.analytics.models.get_tasks_request import GetTasksRequest
from wildberries_api_client.analytics.models.get_tasks_response import GetTasksResponse
from wildberries_api_client.analytics.models.get_tasks_response_bytes_error import GetTasksResponseBytesError
from wildberries_api_client.analytics.models.get_tasks_response_bytes_error_data import GetTasksResponseBytesErrorData
from wildberries_api_client.analytics.models.get_tasks_response_bytes_error_data_tasks import GetTasksResponseBytesErrorDataTasks
from wildberries_api_client.analytics.models.get_tasks_response_data import GetTasksResponseData
from wildberries_api_client.analytics.models.inline_response200 import InlineResponse200
from wildberries_api_client.analytics.models.inline_response200_details import InlineResponse200Details
from wildberries_api_client.analytics.models.models_excise_report_response import ModelsExciseReportResponse
from wildberries_api_client.analytics.models.models_excise_report_response_data import ModelsExciseReportResponseData
from wildberries_api_client.analytics.models.models_excise_report_response_data_inner import ModelsExciseReportResponseDataInner
from wildberries_api_client.analytics.models.nm_report_detail_history_request import NmReportDetailHistoryRequest
from wildberries_api_client.analytics.models.nm_report_detail_history_request_period import NmReportDetailHistoryRequestPeriod
from wildberries_api_client.analytics.models.nm_report_detail_history_response import NmReportDetailHistoryResponse
from wildberries_api_client.analytics.models.nm_report_detail_history_response_data import NmReportDetailHistoryResponseData
from wildberries_api_client.analytics.models.nm_report_detail_history_response_history import NmReportDetailHistoryResponseHistory
from wildberries_api_client.analytics.models.nm_report_detail_request import NmReportDetailRequest
from wildberries_api_client.analytics.models.nm_report_detail_request_order_by import NmReportDetailRequestOrderBy
from wildberries_api_client.analytics.models.nm_report_detail_request_period import NmReportDetailRequestPeriod
from wildberries_api_client.analytics.models.nm_report_detail_response import NmReportDetailResponse
from wildberries_api_client.analytics.models.nm_report_detail_response_data import NmReportDetailResponseData
from wildberries_api_client.analytics.models.nm_report_detail_response_data_cards import NmReportDetailResponseDataCards
from wildberries_api_client.analytics.models.nm_report_detail_response_data_object import NmReportDetailResponseDataObject
from wildberries_api_client.analytics.models.nm_report_detail_response_data_statistics import NmReportDetailResponseDataStatistics
from wildberries_api_client.analytics.models.nm_report_detail_response_data_statistics_period_comparison import NmReportDetailResponseDataStatisticsPeriodComparison
from wildberries_api_client.analytics.models.nm_report_detail_response_data_statistics_period_comparison_conversions import NmReportDetailResponseDataStatisticsPeriodComparisonConversions
from wildberries_api_client.analytics.models.nm_report_detail_response_data_statistics_previous_period import NmReportDetailResponseDataStatisticsPreviousPeriod
from wildberries_api_client.analytics.models.nm_report_detail_response_data_statistics_previous_period_conversions import NmReportDetailResponseDataStatisticsPreviousPeriodConversions
from wildberries_api_client.analytics.models.nm_report_detail_response_data_statistics_selected_period import NmReportDetailResponseDataStatisticsSelectedPeriod
from wildberries_api_client.analytics.models.nm_report_detail_response_data_statistics_selected_period_conversions import NmReportDetailResponseDataStatisticsSelectedPeriodConversions
from wildberries_api_client.analytics.models.nm_report_detail_response_data_stocks import NmReportDetailResponseDataStocks
from wildberries_api_client.analytics.models.nm_report_detail_response_data_tags import NmReportDetailResponseDataTags
from wildberries_api_client.analytics.models.nm_report_grouped_history_request import NmReportGroupedHistoryRequest
from wildberries_api_client.analytics.models.nm_report_grouped_history_request_period import NmReportGroupedHistoryRequestPeriod
from wildberries_api_client.analytics.models.nm_report_grouped_history_response import NmReportGroupedHistoryResponse
from wildberries_api_client.analytics.models.nm_report_grouped_history_response_data import NmReportGroupedHistoryResponseData
from wildberries_api_client.analytics.models.nm_report_grouped_history_response_history import NmReportGroupedHistoryResponseHistory
from wildberries_api_client.analytics.models.nm_report_grouped_history_response_object import NmReportGroupedHistoryResponseObject
from wildberries_api_client.analytics.models.nm_report_grouped_history_response_tag import NmReportGroupedHistoryResponseTag
from wildberries_api_client.analytics.models.nm_report_grouped_request import NmReportGroupedRequest
from wildberries_api_client.analytics.models.nm_report_grouped_request_order_by import NmReportGroupedRequestOrderBy
from wildberries_api_client.analytics.models.nm_report_grouped_request_period import NmReportGroupedRequestPeriod
from wildberries_api_client.analytics.models.nm_report_grouped_response import NmReportGroupedResponse
from wildberries_api_client.analytics.models.nm_report_grouped_response_data import NmReportGroupedResponseData
from wildberries_api_client.analytics.models.nm_report_grouped_response_data_groups import NmReportGroupedResponseDataGroups
from wildberries_api_client.analytics.models.nm_report_grouped_response_data_object import NmReportGroupedResponseDataObject
from wildberries_api_client.analytics.models.nm_report_grouped_response_data_statistics import NmReportGroupedResponseDataStatistics
from wildberries_api_client.analytics.models.nm_report_grouped_response_data_statistics_period_comparison import NmReportGroupedResponseDataStatisticsPeriodComparison
from wildberries_api_client.analytics.models.nm_report_grouped_response_data_statistics_period_comparison_conversions import NmReportGroupedResponseDataStatisticsPeriodComparisonConversions
from wildberries_api_client.analytics.models.nm_report_grouped_response_data_statistics_previous_period import NmReportGroupedResponseDataStatisticsPreviousPeriod
from wildberries_api_client.analytics.models.nm_report_grouped_response_data_statistics_previous_period_conversions import NmReportGroupedResponseDataStatisticsPreviousPeriodConversions
from wildberries_api_client.analytics.models.nm_report_grouped_response_data_statistics_selected_period import NmReportGroupedResponseDataStatisticsSelectedPeriod
from wildberries_api_client.analytics.models.one_of_create_task_request import OneOfCreateTaskRequest
from wildberries_api_client.analytics.models.response_body_content_error400 import ResponseBodyContentError400
from wildberries_api_client.analytics.models.response_body_content_error400_additional_errors import ResponseBodyContentError400AdditionalErrors
from wildberries_api_client.analytics.models.response_body_content_error403 import ResponseBodyContentError403
from wildberries_api_client.analytics.models.response_error import ResponseError
from wildberries_api_client.analytics.models.response_error_additional_errors import ResponseErrorAdditionalErrors
from wildberries_api_client.analytics.models.response_paid_storage import ResponsePaidStorage
from wildberries_api_client.analytics.models.response_paid_storage_inner import ResponsePaidStorageInner
