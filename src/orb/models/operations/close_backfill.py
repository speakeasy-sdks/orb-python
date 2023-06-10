"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import backfill as shared_backfill
from typing import Optional



@dataclasses.dataclass
class CloseBackfillRequest:
    backfill_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'backfill_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class CloseBackfillResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    backfill: Optional[shared_backfill.Backfill] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

