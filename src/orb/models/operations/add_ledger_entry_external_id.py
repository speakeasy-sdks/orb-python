"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import credit_ledger_entry as shared_credit_ledger_entry
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from orb import utils
from typing import Any, Optional

class AddLedgerEntryExternalIDRequestBodyEntryType(str, Enum):
    INCREMENT = 'increment'
    DECREMENT = 'decrement'
    EXPIRATION_CHANGE = 'expiration_change'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddLedgerEntryExternalIDRequestBodyInvoiceSettings:
    r"""Passing `invoice_settings` automatically generates an invoice for the newly added credits. If `invoice_settings` is passed, you must specify `per_unit_cost_basis`, as the calculation of the invoice total is done on that basis."""
    
    auto_collection: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auto_collection') }})
    r"""Whether the credits purchase invoice should auto collect with the customer's saved payment method."""
    net_terms: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('net_terms') }})
    r"""The net terms determines the difference between the invoice date and the issue date for the invoice. If you intend the invoice to be due on issue, set this to 0."""
    memo: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memo'), 'exclude': lambda f: f is None }})
    r"""An optional memo to display on the invoice."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddLedgerEntryExternalIDRequestBody:
    
    entry_type: AddLedgerEntryExternalIDRequestBodyEntryType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entry_type') }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""The number of credits to effect. Note that this is required for increment or decrement operations."""
    block_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_id'), 'exclude': lambda f: f is None }})
    r"""The ID of the block affected by an `expiration_change`"""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Optional metadata that can be specified when adding ledger results via the API. For example, this can be used to note an increment refers to trial credits, or for noting corrections as a result of an incident, etc."""
    expiry_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiry_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""A future date (specified in YYYY-MM-DD format) that denotes when this credit balance should expire."""
    invoice_settings: Optional[AddLedgerEntryExternalIDRequestBodyInvoiceSettings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_settings'), 'exclude': lambda f: f is None }})
    r"""Passing `invoice_settings` automatically generates an invoice for the newly added credits. If `invoice_settings` is passed, you must specify `per_unit_cost_basis`, as the calculation of the invoice total is done on that basis."""
    metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""User-specified key/value pairs for the ledger entry resource."""
    per_unit_cost_basis: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per_unit_cost_basis'), 'exclude': lambda f: f is None }})
    r"""Can only be specified when `entry_type=increment`. How much, in USD, a customer paid for a single credit in this block"""
    target_expiry_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_expiry_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""A future date (specified in YYYY-MM-DD) used for `expiration_change`"""
    

@dataclasses.dataclass
class AddLedgerEntryExternalIDRequest:
    
    external_customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'external_customer_id', 'style': 'simple', 'explode': False }})
    request_body: Optional[AddLedgerEntryExternalIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class AddLedgerEntryExternalIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    credit_ledger_entry: Optional[shared_credit_ledger_entry.CreditLedgerEntry] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    