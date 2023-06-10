"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import plan as shared_plan
from typing import Optional



@dataclasses.dataclass
class FetchPlanRequest:
    plan_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'plan_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class FetchPlanResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plan: Optional[shared_plan.Plan] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

