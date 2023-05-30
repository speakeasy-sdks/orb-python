"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import customer_balance_transaction as shared_customer_balance_transaction
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from orb import utils
from typing import Optional

class PostCustomersCustomerIDBalanceTransactionsRequestBodyType(str, Enum):
    INCREMENT = 'increment'
    DECREMENT = 'decrement'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostCustomersCustomerIDBalanceTransactionsRequestBody:
    
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    type: PostCustomersCustomerIDBalanceTransactionsRequestBodyType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""An optional description that can be specified around this entry."""
    

@dataclasses.dataclass
class PostCustomersCustomerIDBalanceTransactionsRequest:
    
    customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customer_id', 'style': 'simple', 'explode': False }})
    request_body: Optional[PostCustomersCustomerIDBalanceTransactionsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PostCustomersCustomerIDBalanceTransactionsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    customer_balance_transaction: Optional[shared_customer_balance_transaction.CustomerBalanceTransaction] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    