"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import discount as shared_discount
from dataclasses_json import Undefined, dataclass_json
from orb import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreditNoteLineItemSubLineItems:
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreditNoteLineItemTaxAmounts:
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    tax_rate_description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_rate_description') }})
    tax_rate_percentage: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_rate_percentage') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreditNoteLineItem:
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount of the line item, including any line item minimums and discounts"""
    discounts: shared_discount.Discount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discounts') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The Orb id of this resource"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the corresponding invoice line item"""
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    r"""An optional quantity credited."""
    sub_line_items: list[CreditNoteLineItemSubLineItems] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sub_line_items') }})
    r"""Any sub line items that may be credited."""
    subtotal: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtotal') }})
    r"""The amount of the line item, excluding any line item minimums and discounts"""
    tax_amounts: list[CreditNoteLineItemTaxAmounts] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_amounts') }})
    r"""Any tax amounts applied onto the line item."""
    

