"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from orb import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkBPSPriceOverrideBulkBPSConfigTiers:
    
    bps: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bps') }})
    maximum_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maximum_amount') }})
    per_unit_maximum: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per_unit_maximum') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkBPSPriceOverrideBulkBPSConfig:
    
    tiers: Optional[list[BulkBPSPriceOverrideBulkBPSConfigTiers]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers'), 'exclude': lambda f: f is None }})
    
class BulkBpsModelType(str, Enum):
    BULK_BPS = 'bulk_bps'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkBPSPriceOverride:
    r"""Bulk BPS price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: BulkBpsModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    bulk_bps_config: Optional[BulkBPSPriceOverrideBulkBPSConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulk_bps_config'), 'exclude': lambda f: f is None }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    