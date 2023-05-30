"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from orb import utils
from typing import Optional

class DiscountDiscountType(str, Enum):
    PERCENTAGE = 'percentage'
    TRIAL = 'trial'
    USAGE = 'usage'
    AMOUNT = 'amount'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Discount:
    
    discount_type: DiscountDiscountType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discount_type') }})
    amount_discount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_discount'), 'exclude': lambda f: f is None }})
    r"""Only available if discount_type is `amount`."""
    applies_to_price_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('applies_to_price_ids'), 'exclude': lambda f: f is None }})
    r"""List of price_ids that this discount applies to. For plan/plan phase discounts, this can be a subset of prices."""
    percentage_discount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('percentage_discount'), 'exclude': lambda f: f is None }})
    r"""Only available if discount_type is `percentage`.This is a number between 0 and 1."""
    trial_amount_discount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trial_amount_discount'), 'exclude': lambda f: f is None }})
    r"""Only available if discount_type is `trial`"""
    usage_discount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage_discount'), 'exclude': lambda f: f is None }})
    r"""Only available if discount_type is `usage`. Number of usage units that this discount is for"""
    