"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from orb import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewBackfill:
    
    replace_existing_events: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replace_existing_events') }})
    r"""If true, replaces all existing events in the timeframe with the newly ingested events. If false, adds the newly ingested events to the existing events."""
    timeframe_end: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeframe_end'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The (exclusive) end of the usage timeframe affected by this backfill."""
    timeframe_start: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeframe_start'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The (inclusive) end of the usage timeframe affected by this backfill."""
    close_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('close_time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The time at which no more events will be accepted for this backfill. The backfill will automatically begin reflecting throughout Orb at the close time. If not specified, it will default to 1 day after the creation of the backfill."""
    customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_id'), 'exclude': lambda f: f is None }})
    r"""The ID of the customer to which this backfill is scoped."""
    external_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id'), 'exclude': lambda f: f is None }})
    r"""The external customer ID of the customer to which this backfill is scoped."""
    