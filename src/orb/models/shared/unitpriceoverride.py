"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from orb import utils
from typing import Optional

class UnitModelType(str, Enum):
    UNIT = 'unit'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UnitPriceOverrideUnitConfig:
    unit_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UnitPriceOverride:
    r"""Unit price override"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: UnitModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    unit_config: UnitPriceOverrideUnitConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_config') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    

