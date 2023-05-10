"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import billingaddress as shared_billingaddress
from ..shared import shippingaddress as shared_shippingaddress
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from orb import utils
from typing import Optional

class CustomerPaymentProviderEnum(str, Enum):
    r"""The external payments or invoicing solution connected to this customer."""
    STRIPE = 'stripe'
    QUICKBOOKS = 'quickbooks'
    BILL_COM = 'bill.com'
    STRIPE_CHARGE = 'stripe_charge'
    STRIPE_INVOICE = 'stripe_invoice'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Customer:
    r"""A customer is a buyer of your products, and the other party to the billing relationship.
    
    In Orb, customers are assigned system generated identifiers automatically, but it's often desirable to have these match existing identifiers in your system. To avoid having to denormalize Orb ID information, you can pass in an `external_customer_id` with your own identifier. See [Customer ID Aliases](../docs/Customer-ID-Aliases.md) for further information about how these aliases work in Orb.
    
    In addition to having an identifier in your system, a customer may exist in a payment provider solution like Stripe. Use the `payment_provider_id` and the `payment_provider` enum field to express this mapping.
    
    A customer also has a timezone (from the standard [IANA timezone database](https://www.iana.org/time-zones)), which defaults to your account's timezone. See [Timezone localization](../docs/Timezone-localization.md) for information on what this timezone parameter influences within Orb.
    """
    
    balance: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance') }})
    r"""The customer's current balance in their currency."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""An ISO 4217 currency string used for the customer's invoices and balance."""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""A valid customer email, to be used for notifications. When Orb triggers payment through a payment gateway, this email will be used for any automatically issued receipts."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The full name of the customer"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    payment_provider: CustomerPaymentProviderEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_provider') }})
    r"""The external payments or invoicing solution connected to this customer."""
    payment_provider_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_provider_id') }})
    r"""The ID of this customer in an external payments solution, such as Stripe. This is used for creating charges or invoices in the external system via Orb."""
    timezone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone') }})
    r"""A timezone identifier from the IANA timezone database, such as \\"America/Los_Angeles\\". This defaults to your account's timezone if not set. This cannot be changed after customer creation."""
    billing_address: Optional[shared_billingaddress.BillingAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    r"""The customer's billing address; all fields in the address are optional. This address appears on customer invoices."""
    external_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id'), 'exclude': lambda f: f is None }})
    r"""An optional user-defined ID for this customer resource, used throughout the system as an alias for this Customer. Use this field to identify a customer by an existing identifier in your system."""
    shipping_address: Optional[shared_shippingaddress.ShippingAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_address'), 'exclude': lambda f: f is None }})
    r"""The customer's shipping address; all fields in the address are optional. Note that downstream tax calculations are based on the shipping address."""
    