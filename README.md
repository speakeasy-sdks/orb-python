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
import dateutil.parser
from orb.models import shared

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.Customer(
    balance='33.00',
    billing_address=shared.BillingAddress(
        city='Laruecester',
        country='US',
        line1='quibusdam',
        line2='unde',
        postal_code='58466-3428',
        state='ipsa',
    ),
    created_at=dateutil.parser.isoparse('2022-03-08T10:35:32.561Z'),
    currency='suscipit',
    email='Paxton.Schulist@yahoo.com',
    external_customer_id='excepturi',
    id='6ed151a0-5dfc-42dd-b7cc-78ca1ba928fc',
    name='Jack Johns',
    payment_provider=shared.CustomerPaymentProviderEnum.QUICKBOOKS,
    payment_provider_id='impedit',
    shipping_address=shared.ShippingAddress(
        city='Klockoberg',
        country='US',
        line1='excepturi',
        line2='aspernatur',
        postal_code='36162',
        state='natus',
    ),
    timezone='America/Los_Angeles',
)

res = s.customer.create(req)

if res.customer is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [availability](docs/availability/README.md)

* [ping](docs/availability/README.md#ping) - Check availability

### [credits](docs/credits/README.md)

* [get](docs/credits/README.md#get) - Add credit ledger entry
* [get_credits](docs/credits/README.md#get_credits) - Retrieve credit balance
* [get_credits_ledger](docs/credits/README.md#get_credits_ledger) - View credits ledger

### [customer](docs/customer/README.md)

* [create](docs/customer/README.md#create) - Create customer
* [get](docs/customer/README.md#get) - Retrieve a customer
* [get_balance](docs/customer/README.md#get_balance) - Get customer balance transactions
* [get_by_external_id](docs/customer/README.md#get_by_external_id) - Retrieve a customer by external ID
* [get_costs](docs/customer/README.md#get_costs) - View customer costs
* [get_costs_by_external_id](docs/customer/README.md#get_costs_by_external_id) - View customer costs by external customer ID
* [list](docs/customer/README.md#list) - List customers
* [update](docs/customer/README.md#update) - Update customer
* [update_by_external_id](docs/customer/README.md#update_by_external_id) - Update a customer by external ID
* [update_usage](docs/customer/README.md#update_usage) - Amend customer usage
* [update_usage_by_external_id](docs/customer/README.md#update_usage_by_external_id) - Amend customer usage by external ID

### [event](docs/event/README.md)

* [deprecate](docs/event/README.md#deprecate) - Deprecate single event
* [ingest](docs/event/README.md#ingest) - Ingest events
* [search](docs/event/README.md#search) - Search events
* [update](docs/event/README.md#update) - Amend single event

### [invoice](docs/invoice/README.md)

* [get](docs/invoice/README.md#get) - Retrieve an Invoice
* [get_upcoming](docs/invoice/README.md#get_upcoming) - Retrieve upcoming invoice
* [list](docs/invoice/README.md#list) - List invoices

### [plan](docs/plan/README.md)

* [get](docs/plan/README.md#get) - Retrieve a plan
* [get_by_external_id](docs/plan/README.md#get_by_external_id) - Retrieve a plan by external plan ID
* [list](docs/plan/README.md#list) - List plans

### [subscription](docs/subscription/README.md)

* [cancel](docs/subscription/README.md#cancel) - Cancel subscription
* [change_schedule](docs/subscription/README.md#change_schedule) - Schedule plan change
* [create](docs/subscription/README.md#create) - Create subscription
* [get](docs/subscription/README.md#get) - Retrieve a subscription
* [get_cost](docs/subscription/README.md#get_cost) - View subscription costs
* [get_schedule](docs/subscription/README.md#get_schedule) - View subscription schedule
* [get_usage](docs/subscription/README.md#get_usage) - View subscription usage
* [list](docs/subscription/README.md#list) - List subscriptions
* [unschedule](docs/subscription/README.md#unschedule) - Unschedule pending plan changes
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
