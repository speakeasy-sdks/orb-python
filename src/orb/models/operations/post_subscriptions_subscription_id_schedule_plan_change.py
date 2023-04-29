"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import subscription as shared_subscription
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from orb import utils
from typing import Any, Optional

class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyChangeOptionEnum(str, Enum):
    r"""Determines the timing of the plan change"""
    REQUESTED_DATE = 'requested_date'
    END_OF_SUBSCRIPTION_TERM = 'end_of_subscription_term'
    IMMEDIATE = 'immediate'

class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides7ModelTypeEnum(str, Enum):
    TIERED_BPS = 'tiered_bps'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides7TieredBpsConfigTiers:
    
    bps: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bps') }})
    maximum_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maximum_amount') }})
    minimum_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount') }})
    per_unit_maximum: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per_unit_maximum') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides7TieredBpsConfig:
    
    tiers: list[PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides7TieredBpsConfigTiers] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides7:
    r"""Tiered BPS price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides7ModelTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    tiered_bps_config: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides7TieredBpsConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiered_bps_config') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides6BulkBpsConfigTiers:
    
    bps: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bps') }})
    maximum_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maximum_amount') }})
    per_unit_maximum: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per_unit_maximum') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides6BulkBpsConfig:
    
    tiers: Optional[list[PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides6BulkBpsConfigTiers]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers'), 'exclude': lambda f: f is None }})
    
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides6ModelTypeEnum(str, Enum):
    BULK_BPS = 'bulk_bps'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides6:
    r"""Bulk BPS price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides6ModelTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    bulk_bps_config: Optional[PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides6BulkBpsConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulk_bps_config'), 'exclude': lambda f: f is None }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides5BpsConfig:
    
    bps: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bps') }})
    per_unit_maximum: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('per_unit_maximum') }})
    
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides5ModelTypeEnum(str, Enum):
    BPS = 'bps'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides5:
    r"""BPS price override"""
    
    bps_config: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides5BpsConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bps_config') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides5ModelTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides4ModelTypeEnum(str, Enum):
    PACKAGE = 'package'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides4PackageConfig:
    
    num_units: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_units') }})
    unit_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides4:
    r"""Package price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides4ModelTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    package_config: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides4PackageConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('package_config') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides3BulkConfigTiers:
    
    maximum_units: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maximum_units') }})
    unit_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides3BulkConfig:
    
    tiers: list[PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides3BulkConfigTiers] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers') }})
    
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides3ModelTypeEnum(str, Enum):
    BULK = 'bulk'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides3:
    r"""Bulk price override"""
    
    bulk_config: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides3BulkConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulk_config') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides3ModelTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides2ModelTypeEnum(str, Enum):
    UNIT = 'unit'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides2UnitConfig:
    
    unit_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides2:
    r"""Unit price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_type: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides2ModelTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    unit_config: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides2UnitConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_config') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides1ModelTypeEnum(str, Enum):
    TIERED = 'tiered'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides1TieredConfigTiers:
    
    first_unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_unit'), 'exclude': lambda f: f is None }})
    last_unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_unit'), 'exclude': lambda f: f is None }})
    unit_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_amount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides1TieredConfig:
    
    tiers: Optional[list[PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides1TieredConfigTiers]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiers'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides1:
    r"""Tiered price override"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""price_id"""
    model_type: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides1ModelTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_type') }})
    tiered_config: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyPriceOverrides1TieredConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiered_config') }})
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for this price."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBody:
    
    change_option: PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBodyChangeOptionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('change_option') }})
    r"""Determines the timing of the plan change"""
    align_billing_with_plan_change_date: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('align_billing_with_plan_change_date'), 'exclude': lambda f: f is None }})
    r"""Reset billing periods to be aligned with the plan change’s effective date."""
    change_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('change_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date that the plan change should take effect, localized to the customer's timezone. This parameter can only be passed if the `change_option` is `requested_date`."""
    external_plan_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_plan_id'), 'exclude': lambda f: f is None }})
    r"""The external_plan_id of the plan that the given subscription should be switched to. Note that either this property or `plan_id` must be specified."""
    minimum_amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum_amount'), 'exclude': lambda f: f is None }})
    r"""The subscription's override minimum amount for the plan."""
    plan_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plan_id'), 'exclude': lambda f: f is None }})
    r"""The plan that the given subscription should be switched to. Note that either this property or `external_plan_id` must be specified."""
    price_overrides: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price_overrides'), 'exclude': lambda f: f is None }})
    r"""Optionally provide a list of overrides for prices on the plan"""
    

@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeRequest:
    
    subscription_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'subscription_id', 'style': 'simple', 'explode': False }})
    request_body: Optional[PostSubscriptionsSubscriptionIDSchedulePlanChangeRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PostSubscriptionsSubscriptionIDSchedulePlanChangeResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    subscription: Optional[shared_subscription.Subscription] = dataclasses.field(default=None)
    r"""OK"""
    