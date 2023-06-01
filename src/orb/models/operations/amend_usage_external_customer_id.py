"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import amendedusage as shared_amendedusage
from ..shared import event as shared_event
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from orb import utils
from typing import Optional


@dataclasses.dataclass
class AmendUsageExternalCustomerIDRequest:
    
    external_customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'external_customer_id', 'style': 'simple', 'explode': False }})
    request_body: Optional[list[shared_event.Event]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    timeframe_end: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeframe_end', 'style': 'form', 'explode': True }})
    r"""Costs returned are exclusive of `timeframe_end`."""
    timeframe_start: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeframe_start', 'style': 'form', 'explode': True }})
    r"""Costs returned are inclusive of `timeframe_start`."""
    

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
    

@dataclasses.dataclass
class AmendUsageExternalCustomerIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    amend_usage_external_customer_id_400_application_json_object: Optional[AmendUsageExternalCustomerID400ApplicationJSON] = dataclasses.field(default=None)
    r"""Bad Request"""
    amended_usage: Optional[shared_amendedusage.AmendedUsage] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    