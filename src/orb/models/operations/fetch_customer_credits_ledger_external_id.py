"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import credit_ledger_entry as shared_credit_ledger_entry
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from orb import utils
from typing import Optional

class FetchCustomerCreditsLedgerExternalIDEntryStatus(str, Enum):
    r"""Filters to a single status of ledger entry"""
    COMMITTED = 'committed'
    PENDING = 'pending'

class FetchCustomerCreditsLedgerExternalIDEntryType(str, Enum):
    r"""Filter to a single type of ledger entry"""
    INCREMENT = 'increment'
    DECREMENT = 'decrement'
    EXPIRATION_CHANGE = 'expiration_change'
    CREDIT_BLOCK_EXPIRY = 'credit_block_expiry'


@dataclasses.dataclass
class FetchCustomerCreditsLedgerExternalIDRequest:
    
    external_customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'external_customer_id', 'style': 'simple', 'explode': False }})
    entry_status: Optional[FetchCustomerCreditsLedgerExternalIDEntryStatus] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'entry_status', 'style': 'form', 'explode': True }})
    r"""Filters to a single status of ledger entry"""
    entry_type: Optional[FetchCustomerCreditsLedgerExternalIDEntryType] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'entry_type', 'style': 'form', 'explode': True }})
    r"""Filter to a single type of ledger entry"""
    minimum_amount: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'minimum_amount', 'style': 'form', 'explode': True }})
    r"""Filter to ledger entries that affect at least this amount"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FetchCustomerCreditsLedgerExternalID200ApplicationJSONPaginationMetadata:
    
    has_more: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_more') }})
    next_cursor: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_cursor') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FetchCustomerCreditsLedgerExternalID200ApplicationJSON:
    r"""OK"""
    
    data: list[shared_credit_ledger_entry.CreditLedgerEntry] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    pagination_metadata: FetchCustomerCreditsLedgerExternalID200ApplicationJSONPaginationMetadata = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination_metadata') }})
    

@dataclasses.dataclass
class FetchCustomerCreditsLedgerExternalIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fetch_customer_credits_ledger_external_id_200_application_json_object: Optional[FetchCustomerCreditsLedgerExternalID200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    