"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import credits as shared_credits
from typing import Optional


@dataclasses.dataclass
class FetchCustomerCreditsRequest:
    
    customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customer_id', 'style': 'simple', 'explode': False }})
    r"""The Orb Customer ID"""
    

@dataclasses.dataclass
class FetchCustomerCreditsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    credits: Optional[shared_credits.Credits] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    