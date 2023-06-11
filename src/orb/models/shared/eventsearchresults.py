"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import event as shared_event
from ..shared import pagination_metadata as shared_pagination_metadata
from dataclasses_json import Undefined, dataclass_json
from orb import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class EventSearchResults:
    r"""An array of events matching the specified search_criteria. If no events match, this array will be empty."""
    data: Optional[list[shared_event.Event]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    pagination_metadata: Optional[shared_pagination_metadata.PaginationMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination_metadata'), 'exclude': lambda f: f is None }})
    

