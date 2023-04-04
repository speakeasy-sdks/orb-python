<div align="center">
    <img src="https://user-images.githubusercontent.com/6267663/229776275-b670d564-fc2e-4843-b061-adf230737e3f.svg">
    <h1>Python SDK</h1>
   <p>The modern pricing platform to bill for seats, consumption, and everything in between.</p>
   <a href="https://docs.withorb.com/docs/orb-docs/overview"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=5444e4&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/orb-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/orb-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/orb-python/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/orb-python?sort=semver&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install orb-billing
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import orb
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.Customer(
    balance="33.00",
    billing_address=shared.BillingAddress(
        city="Laruecester",
        country="US",
        line1="quibusdam",
        line2="unde",
        postal_code="58466-3428",
        state="ipsa",
    ),
    created_at="2022-03-08T10:35:32.561Z",
    currency="suscipit",
    email="Paxton.Schulist@yahoo.com",
    external_customer_id="excepturi",
    id="nisi",
    name="recusandae",
    payment_provider="null",
    payment_provider_id="ab",
    shipping_address=shared.ShippingAddress(
        city="North Lydia",
        country="US",
        line1="perferendis",
        line2="ipsam",
        postal_code="97188-9478",
        state="esse",
    ),
    timezone="America/Los_Angeles",
)
    
res = s.customer.create(req)

if res.customer is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### availability

* `ping` - Check availability

### credits

* `create` - Add credit ledger entry
* `get_credits` - Retrieve credit balance
* `get_credits_ledger` - View credits ledger

### customer

* `create` - Create customer
* `get` - Retrieve a customer
* `get_balance` - Get customer balance transactions
* `get_by_external_id` - Retrieve a customer by external ID
* `get_costs` - View customer costs
* `get_costs_by_external_id` - View customer costs by external customer ID
* `list` - List customers
* `update` - Update customer
* `update_by_external_id` - Update a customer by external ID
* `update_usage` - Amend customer usage
* `update_usage_by_external_id` - Amend customer usage by external ID

### event

* `deprecate` - Deprecate single event
* `ingest` - Ingest events
* `search` - Search events
* `update` - Amend single event

### invoice

* `get` - Retrieve an Invoice
* `get_upcoming` - Retrieve upcoming invoice
* `list` - List invoices

### plan

* `get` - Retrieve a plan
* `get_by_external_id` - Retrieve a plan by external plan ID
* `list` - List plans

### subscription

* `cancel` - Cancel subscription
* `change_schedule` - Schedule plan change
* `create` - Create subscription
* `get` - Retrieve a subscription
* `get_cost` - View subscription costs
* `get_schedule` - View subscription schedule
* `get_usage` - View subscription usage
* `list` - List subscriptions
* `unschedule` - Unschedule pending plan changes
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
