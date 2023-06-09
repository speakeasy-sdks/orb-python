"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import backfill as shared_backfill
from ..shared import pagination_metadata as shared_pagination_metadata
from dataclasses_json import Undefined, dataclass_json
from orb import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Backfills:
    r"""OK"""
    
    data: Optional[list[shared_backfill.Backfill]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    pagination_metadata: Optional[shared_pagination_metadata.PaginationMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination_metadata'), 'exclude': lambda f: f is None }})
    