"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import customers as shared_customers
from typing import Optional


@dataclasses.dataclass
class ListCustomersResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    customers: Optional[shared_customers.Customers] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    