"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import usageitem as shared_usageitem
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from orb import utils

class ModelType(str, Enum):
    USAGE = 'usage'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Usage:
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: ModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    usage: list[shared_usageitem.UsageItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage') }})
    