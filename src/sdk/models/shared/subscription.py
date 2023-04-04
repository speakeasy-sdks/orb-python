"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import customer as shared_customer
from ..shared import plan as shared_plan
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional

class SubscriptionStatusEnum(str, Enum):
    ACTIVE = 'active'
    ENDED = 'ended'
    UPCOMING = 'upcoming'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Subscription:
    r"""A subscription represents the purchase of a plan by a customer.
    
    By default, subscriptions begin on the day that they're created and renew automatically for each billing cycle at the cadence that's configured in the plan definition.
    
    Subscriptions also default to **beginning of month alignment**, which means the first invoice issued for the subscription will have pro-rated charges between the `start_date` and the first of the following month. Subsequent billing periods will always start and end on a month boundary (e.g. subsequent month starts for monthly billing).
    
    Depending on the plan configuration, any _flat_ recurring fees will be billed either at the beginning (in-advance) or end (in-arrears) of each billing cycle. Plans default to **in-advance billing**. Usage-based fees are billed in arrears as usage is accumulated. In the normal course of events, you can expect an invoice to contain usage-based charges for the previous period, and a recurring fee for the following period.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    customer: shared_customer.Customer = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer') }})
    r"""A customer is a buyer of your products, and the other party to the billing relationship.
    
    In Orb, customers are assigned system generated identifiers automatically, but it's often desirable to have these match existing identifiers in your system. To avoid having to denormalize Orb ID information, you can pass in an `external_customer_id` with your own identifier. See [Customer ID Aliases](../docs/Customer-ID-Aliases.md) for further information about how these aliases work in Orb.
    
    In addition to having an identifier in your system, a customer may exist in a payment provider solution like Stripe. Use the `payment_provider_id` and the `payment_provider` enum field to express this mapping.
    
    A customer also has a timezone (from the standard [IANA timezone database](https://www.iana.org/time-zones)), which defaults to your account's timezone. See [Timezone localization](../docs/Timezone-localization.md) for information on what this timezone parameter influences within Orb.
    """  
    end_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date Orb stops billing for this subscription."""  
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    plan: shared_plan.Plan = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plan') }})  
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date Orb starts billing for this subscription."""  
    status: SubscriptionStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})  
    active_plan_phase_order: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active_plan_phase_order'), 'exclude': lambda f: f is None }})
    r"""The current plan phase that is active, only if the subscription's plan has phases."""  
    current_billing_period_end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_billing_period_end_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The end of the current billing period. This is an exclusive timestamp, such that the instant returned is not part of the billing period. Set to null for subscriptions that are not currently active."""  
    current_billing_period_start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_billing_period_start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The start of the current billing period. This is an inclusive timestamp; the instant returned is exactly the beginning of the billing period. Set to null if the subscription is not currently active."""  
    