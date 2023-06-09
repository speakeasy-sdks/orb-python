"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import subscriptions as shared_subscriptions
from typing import Optional


@dataclasses.dataclass
class ListCouponSubscriptionsRequest:
    
    coupon_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'coupon_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListCouponSubscriptionsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    subscriptions: Optional[shared_subscriptions.Subscriptions] = dataclasses.field(default=None)
    r"""OK"""
    