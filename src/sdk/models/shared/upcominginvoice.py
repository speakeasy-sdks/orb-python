"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpcomingInvoiceCustomer:
    r"""The customer receiving this invoice."""
    
    external_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id') }})  
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpcomingInvoiceLineItemsGrouping:
    r"""For configured prices that are split by a grouping key, this will be populated with the key and a value. The `amount` and `subtotal` will be the values for this particular grouping."""
    
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})  
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpcomingInvoiceLineItemsSubLineItemsMatrixConfig:
    r"""Only available if `type` is `matrix`. Contains the values of the matrix that this `sub_line_item` represents."""
    
    dimension_values: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimension_values') }})
    r"""The ordered dimension values for this line item."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpcomingInvoiceLineItemsSubLineItemsTierConfig:
    r"""Only available if `type` is `tier`. Contains the range of units in this tier and the unit amount."""
    
    first_unit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_unit') }})  
    last_unit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_unit') }})  
    unit_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount') }})  
    
class UpcomingInvoiceLineItemsSubLineItemsTypeEnum(str, Enum):
    r"""An identifier for a sub line item that is specific to a pricing model."""
    MATRIX = 'matrix'
    TIER = 'tier'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpcomingInvoiceLineItemsSubLineItems:
    
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The total amount for this sub line item."""  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})  
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})  
    type: UpcomingInvoiceLineItemsSubLineItemsTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""An identifier for a sub line item that is specific to a pricing model."""  
    matrix_config: Optional[UpcomingInvoiceLineItemsSubLineItemsMatrixConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('matrix_config'), 'exclude': lambda f: f is None }})
    r"""Only available if `type` is `matrix`. Contains the values of the matrix that this `sub_line_item` represents."""  
    tier_config: Optional[UpcomingInvoiceLineItemsSubLineItemsTierConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tier_config'), 'exclude': lambda f: f is None }})
    r"""Only available if `type` is `tier`. Contains the range of units in this tier and the unit amount."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpcomingInvoiceLineItems:
    
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The final amount after any discounts or minimums."""  
    end_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The end date of the range of time applied for this line item's price."""  
    grouping: UpcomingInvoiceLineItemsGrouping = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grouping') }})
    r"""For configured prices that are split by a grouping key, this will be populated with the key and a value. The `amount` and `subtotal` will be the values for this particular grouping."""  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the price associated with this line item."""  
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})  
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The start date of the range of time applied for this line item's price."""  
    sub_line_items: list[UpcomingInvoiceLineItemsSubLineItems] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sub_line_items') }})
    r"""For complex pricing structures, the line item can be broken down further in `sub_line_items`."""  
    subtotal: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtotal') }})
    r"""The line amount before any line item-specific discounts or minimums."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpcomingInvoiceSubscription:
    r"""The associated subscription for this invoice."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpcomingInvoice:
    r"""Upcoming invoices contain a line-by-line breakdown of an upcoming amount due for a subscription, including incurred usage in the billing period as well as any recurring fees.
    
    Although each line item will be invoiced on the `target_date`, each invoice line item may have distinct date ranges (e.g. for usage billed in arrears, the range may specify the current month whereas an in-advance recurring fees will be for the following month).
    
    Since an invoice resource has not been created for this upcoming invoice, this endpoint intentionally does not return an `id` field.
    """
    
    amount_due: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_due') }})
    r"""The final amount to be charged to the customer after all minimums and discounts have been applied. Only populated for non-pre-paid plans."""  
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""An ISO 4217 currency string or `credits`"""  
    customer: UpcomingInvoiceCustomer = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer') }})
    r"""The customer receiving this invoice."""  
    line_items: list[UpcomingInvoiceLineItems] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line_items') }})
    r"""The breakdown of prices in this invoice."""  
    subscription: UpcomingInvoiceSubscription = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription') }})
    r"""The associated subscription for this invoice."""  
    subtotal: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtotal') }})
    r"""The total before any discounts and minimums are applied."""  
    target_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    r"""The expected issue date of the invoice."""  
    