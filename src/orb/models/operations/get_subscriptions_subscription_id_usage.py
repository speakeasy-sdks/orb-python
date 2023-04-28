"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from datetime import datetime
from enum import Enum
from typing import Optional

class GetSubscriptionsSubscriptionIDUsageGranularityEnum(str, Enum):
    r"""This determines the windowing of usage reporting."""
    DAY = 'day'


@dataclasses.dataclass
class GetSubscriptionsSubscriptionIDUsageRequest:
    
    subscription_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'subscription_id', 'style': 'simple', 'explode': False }})

    billable_metric_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'billable_metric_id', 'style': 'form', 'explode': True }})

    r"""When specified in conjunction with `group_by`, this parameter filters usage to a single billable metric. Note that both `group_by` and `billable_metric_id` must be specific together."""
    granularity: Optional[GetSubscriptionsSubscriptionIDUsageGranularityEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'granularity', 'style': 'form', 'explode': True }})

    r"""This determines the windowing of usage reporting."""
    group_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'group_by', 'style': 'form', 'explode': True }})

    r"""When specified in conjunction with `billable_metric_id`, this parameter groups by the key provided. Note that both `group_by` and `billable_metric_id` must be specific together."""
    timeframe_end: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeframe_end', 'style': 'form', 'explode': True }})

    r"""Usage returned is _exclusive_ of `timeframe_end`"""
    timeframe_start: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeframe_start', 'style': 'form', 'explode': True }})

    r"""Usage returned is _inclusive_ of `timeframe_start`"""
    

@dataclasses.dataclass
class GetSubscriptionsSubscriptionIDUsageResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    