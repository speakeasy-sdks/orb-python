"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from orb import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AmendUsageExternalCustomerIDRequestBodyEvents:
    
    event_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_name') }})
    r"""A name to meaningfully identify the action or event type."""
    properties: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties') }})
    r"""A dictionary of custom properties. Values in this dictionary must be numeric, boolean, or strings. Nested dictionaries are disallowed."""
    timestamp: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp') }})
    r"""An ISO 8601 format date with no timezone offset (i.e. UTC). This should represent the time that usage was recorded, and is particularly important to attribute usage to a given billing period."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AmendUsageExternalCustomerIDRequestBody:
    
    events: list[AmendUsageExternalCustomerIDRequestBodyEvents] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    

@dataclasses.dataclass
class AmendUsageExternalCustomerIDRequest:
    
    external_customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'external_customer_id', 'style': 'simple', 'explode': False }})
    timeframe_end: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'timeframe_end', 'style': 'form', 'explode': True }})
    r"""This bound is exclusive (i.e. events before this timestamp will be updated)"""
    timeframe_start: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'timeframe_start', 'style': 'form', 'explode': True }})
    r"""This bound is inclusive (i.e. events with this timestamp onward, inclusive will be updated)"""
    request_body: Optional[AmendUsageExternalCustomerIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AmendUsageExternalCustomerID400ApplicationJSONValidationErrors:
    
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('idempotency_key'), 'exclude': lambda f: f is None }})
    validation_errors: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_errors'), 'exclude': lambda f: f is None }})
    r"""An array of strings corresponding to each validation failure"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AmendUsageExternalCustomerID400ApplicationJSON:
    r"""Bad Request"""
    
    status: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""HTTP Code"""
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    r"""Error message"""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    validation_errors: list[AmendUsageExternalCustomerID400ApplicationJSONValidationErrors] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_errors') }})
    r"""Contains all failing validation events."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AmendUsageExternalCustomerID200ApplicationJSON:
    r"""OK"""
    
    duplicate: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duplicate'), 'exclude': lambda f: f is None }})
    r"""An array of strings, corresponding to idempotency_key's marked as duplicates (previously ingested)"""
    ingested: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ingested'), 'exclude': lambda f: f is None }})
    r"""An array of strings, corresponding to idempotency_key's which were successfully ingested."""
    

@dataclasses.dataclass
class AmendUsageExternalCustomerIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    amend_usage_external_customer_id_200_application_json_object: Optional[AmendUsageExternalCustomerID200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    amend_usage_external_customer_id_400_application_json_object: Optional[AmendUsageExternalCustomerID400ApplicationJSON] = dataclasses.field(default=None)
    r"""Bad Request"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    