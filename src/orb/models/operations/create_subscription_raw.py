"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import subscription as shared_subscription
from typing import Optional


@dataclasses.dataclass
class CreateSubscriptionRawResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    subscription: Optional[shared_subscription.Subscription] = dataclasses.field(default=None)
    r"""OK"""
    