"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from orb import utils
from typing import Optional

class CreateDiscountDiscountType(str, Enum):
    PERCENTAGE = 'percentage'
    USAGE = 'usage'
    AMOUNT = 'amount'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateDiscount:
    r"""The subscription's override discount for this price."""
    
    amount_discount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_discount'), 'exclude': lambda f: f is None }})
    r"""Only allowed if discount_type is amount"""
    discount_type: Optional[CreateDiscountDiscountType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discount_type'), 'exclude': lambda f: f is None }})
    percentage_discount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('percentage_discount'), 'exclude': lambda f: f is None }})
    r"""Only allowed if discount_type is percentage"""
    usage_discount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage_discount'), 'exclude': lambda f: f is None }})
    r"""Only allowed if discount_type is usage"""
    