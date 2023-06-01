"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from orb import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkPriceOverrideBulkConfigTiers:
    
    maximum_units: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maximum_units') }})
    unit_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkPriceOverrideBulkConfig:
    
    tiers: list[BulkPriceOverrideBulkConfigTiers] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers') }})
    
class BulkPriceOverrideModelType(str, Enum):
    BULK = 'bulk'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkPriceOverride:
    r"""Bulk price override"""
    
    bulk_config: BulkPriceOverrideBulkConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulk_config') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: BulkPriceOverrideModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    