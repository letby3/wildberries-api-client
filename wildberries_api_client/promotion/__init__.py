# coding: utf-8

# flake8: noqa

"""
    Opisanie API Prodvihenie

    Sinhronizacia dannyh iz bd proishodit raz v 3 minuty.  <br>Izmenenie statusa proishodit raz v 1 minutu. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu statusa. <br>Izmenenie stavki proishodit raz v 30 sekund. Vnutri etogo intervala budet sohraneno poslednee deistvie po izmeneniu stavki.   # noqa: E501

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from wildberries_api_client.promotion.api.aktivnost_kampanii_api import AktivnostKampaniiApi
from wildberries_api_client.promotion.api.aktivnost_mediakampanii_api import AktivnostMediakampaniiApi
from wildberries_api_client.promotion.api.finansy_api import FinansyApi
from wildberries_api_client.promotion.api.media_api import MediaApi
from wildberries_api_client.promotion.api.prodvihenie_api import ProdvihenieApi
from wildberries_api_client.promotion.api.slovari_api import SlovariApi
from wildberries_api_client.promotion.api.statistika_api import StatistikaApi
from wildberries_api_client.promotion.api.statistika_mediakampanii_api import StatistikaMediakampaniiApi
from wildberries_api_client.promotion.api.stavki_api import StavkiApi
from wildberries_api_client.promotion.api.stavki_mediakampanii_api import StavkiMediakampaniiApi
from wildberries_api_client.promotion.api.upravlenie_obhimi_parametrami_kampanii_api import UpravlenieObhimiParametramiKampaniiApi
from wildberries_api_client.promotion.api.upravlenie_parametrami_avtomatiheskih_kampanii_api import UpravlenieParametramiAvtomatiheskihKampaniiApi
from wildberries_api_client.promotion.api.upravlenie_parametrami_kampanii_v_poiske_api import UpravlenieParametramiKampaniiVPoiskeApi
# import ApiClient
from wildberries_api_client.promotion.api_client import ApiClient
from wildberries_api_client.promotion.configuration import Configuration
# import models into sdk package
from wildberries_api_client.promotion.models.advert_pause_body import AdvertPauseBody
from wildberries_api_client.promotion.models.advert_start_body import AdvertStartBody
from wildberries_api_client.promotion.models.advert_stop_body import AdvertStopBody
from wildberries_api_client.promotion.models.advv0allcpm_cpm import Advv0allcpmCpm
from wildberries_api_client.promotion.models.advv0intervals_intervals import Advv0intervalsIntervals
from wildberries_api_client.promotion.models.advv0nmactive_active import Advv0nmactiveActive
from wildberries_api_client.promotion.models.advv1searchsavead_groups import Advv1searchsaveadGroups
from wildberries_api_client.promotion.models.advv1searchsupplierproducts_kind import Advv1searchsupplierproductsKind
from wildberries_api_client.promotion.models.advv1searchsupplierproducts_subject import Advv1searchsupplierproductsSubject
from wildberries_api_client.promotion.models.auto_active_body import AutoActiveBody
from wildberries_api_client.promotion.models.auto_setexcluded_body import AutoSetexcludedBody
from wildberries_api_client.promotion.models.auto_updatenm_body import AutoUpdatenmBody
from wildberries_api_client.promotion.models.booster_stats import BoosterStats
from wildberries_api_client.promotion.models.booster_stats_inner import BoosterStatsInner
from wildberries_api_client.promotion.models.budget_deposit_body import BudgetDepositBody
from wildberries_api_client.promotion.models.cpm_change_body import CpmChangeBody
from wildberries_api_client.promotion.models.daily_stats1 import DailyStats1
from wildberries_api_client.promotion.models.daily_stats1_inner import DailyStats1Inner
from wildberries_api_client.promotion.models.daily_stats2 import DailyStats2
from wildberries_api_client.promotion.models.daily_stats2_inner import DailyStats2Inner
from wildberries_api_client.promotion.models.days import Days
from wildberries_api_client.promotion.models.days_inner import DaysInner
from wildberries_api_client.promotion.models.inline_response200 import InlineResponse200
from wildberries_api_client.promotion.models.inline_response2001 import InlineResponse2001
from wildberries_api_client.promotion.models.inline_response20010 import InlineResponse20010
from wildberries_api_client.promotion.models.inline_response20011 import InlineResponse20011
from wildberries_api_client.promotion.models.inline_response20012 import InlineResponse20012
from wildberries_api_client.promotion.models.inline_response20013 import InlineResponse20013
from wildberries_api_client.promotion.models.inline_response20014 import InlineResponse20014
from wildberries_api_client.promotion.models.inline_response20015 import InlineResponse20015
from wildberries_api_client.promotion.models.inline_response20016 import InlineResponse20016
from wildberries_api_client.promotion.models.inline_response20017 import InlineResponse20017
from wildberries_api_client.promotion.models.inline_response20018 import InlineResponse20018
from wildberries_api_client.promotion.models.inline_response20019 import InlineResponse20019
from wildberries_api_client.promotion.models.inline_response2002 import InlineResponse2002
from wildberries_api_client.promotion.models.inline_response20020 import InlineResponse20020
from wildberries_api_client.promotion.models.inline_response20020_clusters import InlineResponse20020Clusters
from wildberries_api_client.promotion.models.inline_response20021 import InlineResponse20021
from wildberries_api_client.promotion.models.inline_response20021_stat import InlineResponse20021Stat
from wildberries_api_client.promotion.models.inline_response20022 import InlineResponse20022
from wildberries_api_client.promotion.models.inline_response20022_stat import InlineResponse20022Stat
from wildberries_api_client.promotion.models.inline_response20022_words import InlineResponse20022Words
from wildberries_api_client.promotion.models.inline_response20022_words_keywords import InlineResponse20022WordsKeywords
from wildberries_api_client.promotion.models.inline_response20023 import InlineResponse20023
from wildberries_api_client.promotion.models.inline_response20023_words import InlineResponse20023Words
from wildberries_api_client.promotion.models.inline_response20024 import InlineResponse20024
from wildberries_api_client.promotion.models.inline_response20024_apps import InlineResponse20024Apps
from wildberries_api_client.promotion.models.inline_response20024_booster_stats import InlineResponse20024BoosterStats
from wildberries_api_client.promotion.models.inline_response20024_days import InlineResponse20024Days
from wildberries_api_client.promotion.models.inline_response20024_nm import InlineResponse20024Nm
from wildberries_api_client.promotion.models.inline_response20025 import InlineResponse20025
from wildberries_api_client.promotion.models.inline_response20025_catalog import InlineResponse20025Catalog
from wildberries_api_client.promotion.models.inline_response20025_dates import InlineResponse20025Dates
from wildberries_api_client.promotion.models.inline_response20025_search import InlineResponse20025Search
from wildberries_api_client.promotion.models.inline_response20026 import InlineResponse20026
from wildberries_api_client.promotion.models.inline_response20027 import InlineResponse20027
from wildberries_api_client.promotion.models.inline_response2002_adverts import InlineResponse2002Adverts
from wildberries_api_client.promotion.models.inline_response2003 import InlineResponse2003
from wildberries_api_client.promotion.models.inline_response2004 import InlineResponse2004
from wildberries_api_client.promotion.models.inline_response2004_extended import InlineResponse2004Extended
from wildberries_api_client.promotion.models.inline_response2004_items import InlineResponse2004Items
from wildberries_api_client.promotion.models.inline_response2004_show_hours import InlineResponse2004ShowHours
from wildberries_api_client.promotion.models.inline_response2005 import InlineResponse2005
from wildberries_api_client.promotion.models.inline_response2006 import InlineResponse2006
from wildberries_api_client.promotion.models.inline_response2007 import InlineResponse2007
from wildberries_api_client.promotion.models.inline_response2008 import InlineResponse2008
from wildberries_api_client.promotion.models.inline_response2009 import InlineResponse2009
from wildberries_api_client.promotion.models.inline_response200_advert import InlineResponse200Advert
from wildberries_api_client.promotion.models.inline_response200_advert_list import InlineResponse200AdvertList
from wildberries_api_client.promotion.models.inline_response400 import InlineResponse400
from wildberries_api_client.promotion.models.one_ofinline_response2001 import OneOfinlineResponse2001
from wildberries_api_client.promotion.models.one_ofinline_response20018 import OneOfinlineResponse20018
from wildberries_api_client.promotion.models.one_ofinline_response2009 import OneOfinlineResponse2009
from wildberries_api_client.promotion.models.one_ofv1_fullstats_body import OneOfv1FullstatsBody
from wildberries_api_client.promotion.models.one_ofv1_stats_body import OneOfv1StatsBody
from wildberries_api_client.promotion.models.one_ofv2_fullstats_body import OneOfv2FullstatsBody
from wildberries_api_client.promotion.models.request_with_campaign_id import RequestWithCampaignID
from wildberries_api_client.promotion.models.request_with_campaign_id_inner import RequestWithCampaignIDInner
from wildberries_api_client.promotion.models.request_with_date import RequestWithDate
from wildberries_api_client.promotion.models.request_with_date_inner import RequestWithDateInner
from wildberries_api_client.promotion.models.request_with_interval import RequestWithInterval
from wildberries_api_client.promotion.models.request_with_interval_inner import RequestWithIntervalInner
from wildberries_api_client.promotion.models.response429 import Response429
from wildberries_api_client.promotion.models.response_adv_error1 import ResponseAdvError1
from wildberries_api_client.promotion.models.response_advert401 import ResponseAdvert401
from wildberries_api_client.promotion.models.response_info_advert import ResponseInfoAdvert
from wildberries_api_client.promotion.models.response_info_advert_intervals import ResponseInfoAdvertIntervals
from wildberries_api_client.promotion.models.response_info_advert_nms import ResponseInfoAdvertNms
from wildberries_api_client.promotion.models.response_info_advert_params import ResponseInfoAdvertParams
from wildberries_api_client.promotion.models.response_info_advert_type8 import ResponseInfoAdvertType8
from wildberries_api_client.promotion.models.response_info_advert_type8_auto_params import ResponseInfoAdvertType8AutoParams
from wildberries_api_client.promotion.models.response_info_advert_type8_auto_params_active import ResponseInfoAdvertType8AutoParamsActive
from wildberries_api_client.promotion.models.response_info_advert_type8_auto_params_menus import ResponseInfoAdvertType8AutoParamsMenus
from wildberries_api_client.promotion.models.response_info_advert_type8_auto_params_sets import ResponseInfoAdvertType8AutoParamsSets
from wildberries_api_client.promotion.models.response_info_advert_type8_auto_params_subject import ResponseInfoAdvertType8AutoParamsSubject
from wildberries_api_client.promotion.models.response_info_advert_type9 import ResponseInfoAdvertType9
from wildberries_api_client.promotion.models.response_info_advert_type9_menus import ResponseInfoAdvertType9Menus
from wildberries_api_client.promotion.models.response_info_advert_type9_subject import ResponseInfoAdvertType9Subject
from wildberries_api_client.promotion.models.response_info_advert_type9_united_params import ResponseInfoAdvertType9UnitedParams
from wildberries_api_client.promotion.models.response_with_date import ResponseWithDate
from wildberries_api_client.promotion.models.response_with_date_inner import ResponseWithDateInner
from wildberries_api_client.promotion.models.response_with_interval import ResponseWithInterval
from wildberries_api_client.promotion.models.response_with_interval_inner import ResponseWithIntervalInner
from wildberries_api_client.promotion.models.response_with_return import ResponseWithReturn
from wildberries_api_client.promotion.models.seacat_savead_body import SeacatSaveadBody
from wildberries_api_client.promotion.models.search_savead_body import SearchSaveadBody
from wildberries_api_client.promotion.models.search_setexcluded_body import SearchSetexcludedBody
from wildberries_api_client.promotion.models.search_setphrase_body import SearchSetphraseBody
from wildberries_api_client.promotion.models.search_setplus_body import SearchSetplusBody
from wildberries_api_client.promotion.models.search_setstrong_body import SearchSetstrongBody
from wildberries_api_client.promotion.models.stat import Stat
from wildberries_api_client.promotion.models.stat_date import StatDate
from wildberries_api_client.promotion.models.stat_interval import StatInterval
from wildberries_api_client.promotion.models.stat_interval_interval import StatIntervalInterval
from wildberries_api_client.promotion.models.stats1 import Stats1
from wildberries_api_client.promotion.models.stats1_inner import Stats1Inner
from wildberries_api_client.promotion.models.stats2 import Stats2
from wildberries_api_client.promotion.models.stats2_inner import Stats2Inner
from wildberries_api_client.promotion.models.stats_blok1 import StatsBlok1
from wildberries_api_client.promotion.models.stats_blok2 import StatsBlok2
from wildberries_api_client.promotion.models.v0_allcpm_body import V0AllcpmBody
from wildberries_api_client.promotion.models.v0_cpm_body import V0CpmBody
from wildberries_api_client.promotion.models.v0_intervals_body import V0IntervalsBody
from wildberries_api_client.promotion.models.v0_nmactive_body import V0NmactiveBody
from wildberries_api_client.promotion.models.v0_rename_body import V0RenameBody
from wildberries_api_client.promotion.models.v1_fullstats_body import V1FullstatsBody
from wildberries_api_client.promotion.models.v1_savead_body import V1SaveadBody
from wildberries_api_client.promotion.models.v1_stats_body import V1StatsBody
from wildberries_api_client.promotion.models.v2_fullstats_body import V2FullstatsBody
