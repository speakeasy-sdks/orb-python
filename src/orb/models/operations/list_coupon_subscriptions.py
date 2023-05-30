"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import pagination_metadata as shared_pagination_metadata
from ..shared import subscription as shared_subscription
from dataclasses_json import Undefined, dataclass_json
from orb import utils
from typing import Optional


@dataclasses.dataclass
class ListCouponSubscriptionsRequest:
    
    coupon_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'coupon_id', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCouponSubscriptions200ApplicationJSON:
    r"""OK"""
    
    data: Optional[list[shared_subscription.Subscription]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    pagination_metadata: Optional[shared_pagination_metadata.PaginationMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination_metadata'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListCouponSubscriptionsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_coupon_subscriptions_200_application_json_object: Optional[ListCouponSubscriptions200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    