"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from orb import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPing200ApplicationJSON:
    r"""OK"""
    
    response: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('response') }})

    

@dataclasses.dataclass
class GetPingResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    get_ping_200_application_json_object: Optional[GetPing200ApplicationJSON] = dataclasses.field(default=None)

    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    