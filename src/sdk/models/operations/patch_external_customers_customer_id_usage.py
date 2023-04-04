"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchExternalCustomersCustomerIDUsageRequestBodyEvents:
    
    event_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_name') }})
    r"""A name to meaningfully identify the action or event type."""  
    properties: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties') }})
    r"""A dictionary of custom properties. Values in this dictionary must be numeric, boolean, or strings. Nested dictionaries are disallowed."""  
    timestamp: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp') }})
    r"""An ISO 8601 format date with no timezone offset (i.e. UTC). This should represent the time that usage was recorded, and is particularly important to attribute usage to a given billing period."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchExternalCustomersCustomerIDUsageRequestBody:
    
    events: list[PatchExternalCustomersCustomerIDUsageRequestBodyEvents] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})  
    

@dataclasses.dataclass
class PatchExternalCustomersCustomerIDUsageRequest:
    
    external_customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'external_customer_id', 'style': 'simple', 'explode': False }})  
    timeframe_end: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'timeframe_end', 'style': 'form', 'explode': True }})
    r"""This bound is exclusive (i.e. events before this timestamp will be updated)"""  
    timeframe_start: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'timeframe_start', 'style': 'form', 'explode': True }})
    r"""This bound is inclusive (i.e. events with this timestamp onward, inclusive will be updated)"""  
    request_body: Optional[PatchExternalCustomersCustomerIDUsageRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchExternalCustomersCustomerIDUsage400ApplicationJSONValidationErrors:
    
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('idempotency_key'), 'exclude': lambda f: f is None }})  
    validation_errors: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_errors'), 'exclude': lambda f: f is None }})
    r"""An array of strings corresponding to each validation failure"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchExternalCustomersCustomerIDUsage400ApplicationJSON:
    r"""Bad Request"""
    
    status: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""HTTP Code"""  
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    r"""Error message"""  
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    validation_errors: list[PatchExternalCustomersCustomerIDUsage400ApplicationJSONValidationErrors] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_errors') }})
    r"""Contains all failing validation events."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchExternalCustomersCustomerIDUsage200ApplicationJSON:
    r"""OK"""
    
    duplicate: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duplicate'), 'exclude': lambda f: f is None }})
    r"""An array of strings, corresponding to idempotency_key's marked as duplicates (previously ingested)"""  
    ingested: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ingested'), 'exclude': lambda f: f is None }})
    r"""An array of strings, corresponding to idempotency_key's which were successfully ingested."""  
    

@dataclasses.dataclass
class PatchExternalCustomersCustomerIDUsageResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    patch_external_customers_customer_id_usage_200_application_json_object: Optional[PatchExternalCustomersCustomerIDUsage200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""  
    patch_external_customers_customer_id_usage_400_application_json_object: Optional[PatchExternalCustomersCustomerIDUsage400ApplicationJSON] = dataclasses.field(default=None)
    r"""Bad Request"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    