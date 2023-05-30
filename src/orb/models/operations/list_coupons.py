"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import coupon as shared_coupon
from ..shared import pagination_metadata as shared_pagination_metadata
from dataclasses_json import Undefined, dataclass_json
from orb import utils
from typing import Optional


@dataclasses.dataclass
class ListCouponsRequest:
    
    redemption_code: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'redemption_code', 'style': 'form', 'explode': True }})
    r"""Filter to coupons matching this redemption code."""
    show_archived: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'show_archived', 'style': 'form', 'explode': True }})
    r"""Show archived coupons as well (by default, this endpoint only returns active coupons)."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCoupons200ApplicationJSON:
    r"""OK"""
    
    data: Optional[list[shared_coupon.Coupon]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    pagination_metadata: Optional[shared_pagination_metadata.PaginationMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination_metadata'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListCouponsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_coupons_200_application_json_object: Optional[ListCoupons200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    