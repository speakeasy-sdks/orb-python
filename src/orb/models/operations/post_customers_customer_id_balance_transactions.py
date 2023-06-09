"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import newtransaction as shared_newtransaction
from ..shared import transaction as shared_transaction
from typing import Optional


@dataclasses.dataclass
class PostCustomersCustomerIDBalanceTransactionsRequest:
    
    customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customer_id', 'style': 'simple', 'explode': False }})
    new_transaction: Optional[shared_newtransaction.NewTransaction] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PostCustomersCustomerIDBalanceTransactionsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    transaction: Optional[shared_transaction.Transaction] = dataclasses.field(default=None)
    r"""OK"""
    