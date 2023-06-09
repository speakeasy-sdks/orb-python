"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import subscription as shared_subscription
from ..shared import subscriptioncancellation as shared_subscriptioncancellation
from typing import Optional


@dataclasses.dataclass
class CancelSubscriptionRequest:
    
    subscription_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'subscription_id', 'style': 'simple', 'explode': False }})
    subscription_cancellation: Optional[shared_subscriptioncancellation.SubscriptionCancellation] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CancelSubscriptionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    subscription: Optional[shared_subscription.Subscription] = dataclasses.field(default=None)
    r"""OK"""
    