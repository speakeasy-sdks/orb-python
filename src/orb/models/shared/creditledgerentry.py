"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from orb import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditLedgerEntryCreditBlock:
    r"""Credit block that the entry affected"""
    
    expiry_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiry_date') }})
    r"""Complete timestamp with date and time for when this block expires"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    per_unit_cost_basis: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per_unit_cost_basis') }})
    r"""How much, in USD, a customer paid for a single credit in this block"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditLedgerEntryCustomer:
    
    external_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    
class CreditLedgerEntryEntryStatus(str, Enum):
    r"""Committed entries are older than the ingestion grace period, and cannot change. Pending entries are newer than the grace period and are subject to updates"""
    COMMITTED = 'committed'
    PENDING = 'pending'

class CreditLedgerEntryEntryType(str, Enum):
    INCREMENT = 'increment'
    DECREMENT = 'decrement'
    EXPIRATION_CHANGE = 'expiration_change'
    CREDIT_BLOCK_EXPIRY = 'credit_block_expiry'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditLedgerEntry:
    r"""A credit ledger entry is a single entry in the customer balance ledger. More details about working with real-time balances are [here](../guides/product-catalog/prepurchase).
    
    To support late and out-of-order event reporting, ledger entries are marked as either __committed_ or _pending_. Committed entries are finalized and will not change. Pending entries can be updated up until the event reporting grace period.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    credit_block: CreditLedgerEntryCreditBlock = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_block') }})
    r"""Credit block that the entry affected"""
    customer: CreditLedgerEntryCustomer = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer') }})
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Optional metadata that can be specified when adding ledger results via the API"""
    ending_balance: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ending_balance') }})
    entry_status: CreditLedgerEntryEntryStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entry_status') }})
    r"""Committed entries are older than the ingestion grace period, and cannot change. Pending entries are newer than the grace period and are subject to updates"""
    entry_type: CreditLedgerEntryEntryType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entry_type') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    ledger_sequence_number: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ledger_sequence_number') }})
    r"""The position in which this entry appears in the ledger, starting at 0"""
    metadata: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""User-specified metadata dictionary that's specified when adding a ledger entry. This contains key/value pairs if metadata is specified, but otherwise is an empty dictionary."""
    starting_balance: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('starting_balance') }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""Number of credits that were impacted. Required on creation for increment and decrement entries."""
    event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_id'), 'exclude': lambda f: f is None }})
    new_block_expiry_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_block_expiry_date'), 'exclude': lambda f: f is None }})
    r"""In the case of an expiration change ledger entry, this represents the expiration time of the new block."""
    price_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price_id'), 'exclude': lambda f: f is None }})
    