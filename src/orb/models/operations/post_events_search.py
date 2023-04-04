"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import event as shared_event
from dataclasses_json import Undefined, dataclass_json
from orb import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostEventsSearchRequestBody:
    
    event_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_ids'), 'exclude': lambda f: f is None }})
    r"""This is an explicit array of IDs to filter by. Note that an event's ID is the idempotency_key that was originally used for ingestion. Values in this array will be treated case sensitively."""  
    invoice_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_id'), 'exclude': lambda f: f is None }})
    r"""This is an issued Orb invoice ID (see also List Invoices). Orb will fetch all events that were used to calculate the invoice. In the common case, this will be a list of events whose timestamp property falls within the billing period specified by the invoice."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostEventsSearch200ApplicationJSON:
    r"""An array of events matching the specified search_criteria. If no events match, this array will be empty."""
    
    data: Optional[list[shared_event.Event]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})  
    pagination_metadata: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination_metadata'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class PostEventsSearchResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    post_events_search_200_application_json_object: Optional[PostEventsSearch200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    