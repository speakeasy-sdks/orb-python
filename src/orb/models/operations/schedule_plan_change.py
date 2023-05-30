"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ..shared import subscription as shared_subscription
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from orb import utils
from typing import Any, Optional

class SchedulePlanChangeRequestBodyChangeOption(str, Enum):
    r"""Determines the timing of the plan change"""
    REQUESTED_DATE = 'requested_date'
    END_OF_SUBSCRIPTION_TERM = 'end_of_subscription_term'
    IMMEDIATE = 'immediate'

class SchedulePlanChangeRequestBodyPriceOverrides7ModelType(str, Enum):
    TIERED_BPS = 'tiered_bps'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides7TieredBpsConfigTiers:
    
    bps: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bps') }})
    maximum_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maximum_amount') }})
    minimum_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount') }})
    per_unit_maximum: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per_unit_maximum') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides7TieredBpsConfig:
    
    tiers: list[SchedulePlanChangeRequestBodyPriceOverrides7TieredBpsConfigTiers] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides7:
    r"""Tiered BPS price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: SchedulePlanChangeRequestBodyPriceOverrides7ModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    tiered_bps_config: SchedulePlanChangeRequestBodyPriceOverrides7TieredBpsConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiered_bps_config') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides6BulkBpsConfigTiers:
    
    bps: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bps') }})
    maximum_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maximum_amount') }})
    per_unit_maximum: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per_unit_maximum') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides6BulkBpsConfig:
    
    tiers: Optional[list[SchedulePlanChangeRequestBodyPriceOverrides6BulkBpsConfigTiers]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers'), 'exclude': lambda f: f is None }})
    
class SchedulePlanChangeRequestBodyPriceOverrides6ModelType(str, Enum):
    BULK_BPS = 'bulk_bps'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides6:
    r"""Bulk BPS price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: SchedulePlanChangeRequestBodyPriceOverrides6ModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    bulk_bps_config: Optional[SchedulePlanChangeRequestBodyPriceOverrides6BulkBpsConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulk_bps_config'), 'exclude': lambda f: f is None }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides5BpsConfig:
    
    bps: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bps') }})
    per_unit_maximum: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per_unit_maximum') }})
    
class SchedulePlanChangeRequestBodyPriceOverrides5ModelType(str, Enum):
    BPS = 'bps'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides5:
    r"""BPS price override"""
    
    bps_config: SchedulePlanChangeRequestBodyPriceOverrides5BpsConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bps_config') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: SchedulePlanChangeRequestBodyPriceOverrides5ModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    
class SchedulePlanChangeRequestBodyPriceOverrides4ModelType(str, Enum):
    PACKAGE = 'package'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides4PackageConfig:
    
    num_units: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_units') }})
    unit_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides4:
    r"""Package price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: SchedulePlanChangeRequestBodyPriceOverrides4ModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    package_config: SchedulePlanChangeRequestBodyPriceOverrides4PackageConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('package_config') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides3BulkConfigTiers:
    
    maximum_units: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maximum_units') }})
    unit_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides3BulkConfig:
    
    tiers: list[SchedulePlanChangeRequestBodyPriceOverrides3BulkConfigTiers] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers') }})
    
class SchedulePlanChangeRequestBodyPriceOverrides3ModelType(str, Enum):
    BULK = 'bulk'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides3:
    r"""Bulk price override"""
    
    bulk_config: SchedulePlanChangeRequestBodyPriceOverrides3BulkConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulk_config') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: SchedulePlanChangeRequestBodyPriceOverrides3ModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    
class SchedulePlanChangeRequestBodyPriceOverrides2ModelType(str, Enum):
    UNIT = 'unit'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides2UnitConfig:
    
    unit_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides2:
    r"""Unit price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: SchedulePlanChangeRequestBodyPriceOverrides2ModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    unit_config: SchedulePlanChangeRequestBodyPriceOverrides2UnitConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_config') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    
class SchedulePlanChangeRequestBodyPriceOverrides1ModelType(str, Enum):
    TIERED = 'tiered'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides1TieredConfigTiers:
    
    first_unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_unit'), 'exclude': lambda f: f is None }})
    last_unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_unit'), 'exclude': lambda f: f is None }})
    unit_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides1TieredConfig:
    
    tiers: Optional[list[SchedulePlanChangeRequestBodyPriceOverrides1TieredConfigTiers]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBodyPriceOverrides1:
    r"""Tiered price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""price_id"""
    model_type: SchedulePlanChangeRequestBodyPriceOverrides1ModelType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    tiered_config: SchedulePlanChangeRequestBodyPriceOverrides1TieredConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiered_config') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchedulePlanChangeRequestBody:
    
    change_option: SchedulePlanChangeRequestBodyChangeOption = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('change_option') }})
    r"""Determines the timing of the plan change"""
    align_billing_with_plan_change_date: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('align_billing_with_plan_change_date'), 'exclude': lambda f: f is None }})
    r"""Reset billing periods to be aligned with the plan change’s effective date."""
    change_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('change_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date that the plan change should take effect. This parameter can only be passed if the `change_option` is `requested_date`."""
    coupon_redemption_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('coupon_redemption_code'), 'exclude': lambda f: f is None }})
    r"""Redemption code to be used for this subscription. If the coupon cannot be found by its redemption code, or cannot be redeemed, an error response will be returned and the plan change will not be scheduled."""
    external_plan_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_plan_id'), 'exclude': lambda f: f is None }})
    r"""The external_plan_id of the plan that the given subscription should be switched to. Note that either this property or `plan_id` must be specified."""
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for the plan."""
    plan_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plan_id'), 'exclude': lambda f: f is None }})
    r"""The plan that the given subscription should be switched to. Note that either this property or `external_plan_id` must be specified."""
    price_overrides: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price_overrides'), 'exclude': lambda f: f is None }})
    r"""Optionally provide a list of overrides for prices on the plan"""
    

@dataclasses.dataclass
class SchedulePlanChangeRequest:
    
    subscription_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'subscription_id', 'style': 'simple', 'explode': False }})
    request_body: Optional[SchedulePlanChangeRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SchedulePlanChangeResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    subscription: Optional[shared_subscription.Subscription] = dataclasses.field(default=None)
    r"""OK"""
    