"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from orb import utils
from typing import Optional

class SubscriptionUsageDataModelType(str, Enum):
    USAGE = 'usage'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionUsageDataUsage:
    
    quantity: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    timeframe_end: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeframe_end'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    timeframe_start: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeframe_start'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionUsageData:
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: SubscriptionUsageDataModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    usage: list[SubscriptionUsageDataUsage] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionUsage:
    r"""OK"""
    
    data: Optional[list[SubscriptionUsageData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    