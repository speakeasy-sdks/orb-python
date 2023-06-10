"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import pagination_metadata as shared_pagination_metadata
from ..shared import subscriptioncost as shared_subscriptioncost
from dataclasses_json import Undefined, dataclass_json
from orb import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SubscriptionCosts:
    r"""OK"""
    data: list[shared_subscriptioncost.SubscriptionCost] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    pagination_metadata: shared_pagination_metadata.PaginationMetadata = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination_metadata') }})
    

