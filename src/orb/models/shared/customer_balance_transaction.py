"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from orb import utils

class CustomerBalanceTransactionActionEnum(str, Enum):
    r"""Describes the reason that this transaction took place."""
    APPLIED_TO_INVOICE = 'applied_to_invoice'
    PRORATED_REFUND = 'prorated_refund'
    MANUAL_ADJUSTMENT = 'manual_adjustment'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomerBalanceTransactionInvoice:
    r"""The Invoice associated with this transaction"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The Invoice id"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomerBalanceTransaction:
    r"""A single change to the customer balance. All amounts are in the customer's currency."""
    
    action: CustomerBalanceTransactionActionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    r"""Describes the reason that this transaction took place."""
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The value of the amount changed in the transaction."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The creation time of this transaction."""
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""An optional description provided for manual customer balance adjustments."""
    ending_balance: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ending_balance') }})
    r"""The new value of the customer's balance prior to the transaction, in the customer's currency."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""A unique id for this transaction."""
    invoice: CustomerBalanceTransactionInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice') }})
    r"""The Invoice associated with this transaction"""
    starting_balance: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('starting_balance') }})
    r"""The original value of the customer's balance prior to the transaction, in the customer's currency."""
    