"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import coupon as shared_coupon
from typing import Optional


@dataclasses.dataclass
class FetchCouponRequest:
    
    coupon_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'coupon_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FetchCouponResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    coupon: Optional[shared_coupon.Coupon] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    