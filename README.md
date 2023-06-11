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
from orb.models import shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CouponInput(
    discount=shared.Discount(
        amount_discount='corrupti',
        applies_to_price_ids=[
            'distinctio',
            'quibusdam',
            'unde',
        ],
        discount_type=shared.DiscountType.PERCENTAGE,
        percentage_discount=0.15,
        trial_amount_discount='nulla',
        usage_discount=5448.83,
    ),
    duration_in_months=847252,
    id='69a674e0-f467-4cc8-b96e-d151a05dfc2d',
    max_redemptions=870088,
    redemption_code='maiores',
    times_redeemed=473608,
)

res = s.coupon.create(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [availability](docs/sdks/availability/README.md)

* [ping](docs/sdks/availability/README.md#ping) - Check availability

### [coupon](docs/sdks/coupon/README.md)

* [archive](docs/sdks/coupon/README.md#archive) - Archive a coupon
* [create](docs/sdks/coupon/README.md#create) - Create a coupon
* [fetch](docs/sdks/coupon/README.md#fetch) - Retrieve a coupon
* [list](docs/sdks/coupon/README.md#list) - List coupons
* [list_subscriptions](docs/sdks/coupon/README.md#list_subscriptions) - List subscriptions for a coupon

### [credit](docs/sdks/credit/README.md)

* [add_by_external_id](docs/sdks/credit/README.md#add_by_external_id) - Add credit ledger entry by external customer ID
* [create](docs/sdks/credit/README.md#create) - Add credit ledger entry
* [fetch](docs/sdks/credit/README.md#fetch) - Retrieve credit balance
* [fetch_by_external_id](docs/sdks/credit/README.md#fetch_by_external_id) - Retrieve credit balance by external customer ID
* [fetch_ledger](docs/sdks/credit/README.md#fetch_ledger) - View credits ledger
* [fetch_ledger_by_external_id](docs/sdks/credit/README.md#fetch_ledger_by_external_id) - View credits ledger by external customer ID

### [credit_note](docs/sdks/creditnote/README.md)

* [list](docs/sdks/creditnote/README.md#list) - List credit notes

### [customer](docs/sdks/customer/README.md)

* [amend](docs/sdks/customer/README.md#amend) - Amend customer usage
* [amend_by_external_id](docs/sdks/customer/README.md#amend_by_external_id) - Amend customer usage by external ID
* [create](docs/sdks/customer/README.md#create) - Create customer
* [create_transaction](docs/sdks/customer/README.md#create_transaction) - Create a customer balance transaction
* [delete](docs/sdks/customer/README.md#delete) - Delete a customer
* [fetch](docs/sdks/customer/README.md#fetch) - Retrieve a customer
* [fetch_by_external_id](docs/sdks/customer/README.md#fetch_by_external_id) - Retrieve a customer by external ID
* [fetch_costs](docs/sdks/customer/README.md#fetch_costs) - View customer costs
* [fetch_costs_by_external_id](docs/sdks/customer/README.md#fetch_costs_by_external_id) - View customer costs by external customer ID
* [fetch_transactions](docs/sdks/customer/README.md#fetch_transactions) - Get customer balance transactions
* [list](docs/sdks/customer/README.md#list) - List customers
* [update_by_external_id](docs/sdks/customer/README.md#update_by_external_id) - Update a customer by external ID
* [update_customer](docs/sdks/customer/README.md#update_customer) - Update customer

### [event](docs/sdks/event/README.md)

* [amend](docs/sdks/event/README.md#amend) - Amend single event
* [close_backfill](docs/sdks/event/README.md#close_backfill) - Close a backfill
* [create](docs/sdks/event/README.md#create) - Create a backfill
* [deprecate_event](docs/sdks/event/README.md#deprecate_event) - Deprecate single event
* [ingest](docs/sdks/event/README.md#ingest) - Ingest events
* [list_backfills](docs/sdks/event/README.md#list_backfills) - List backfills
* [revert_backfill](docs/sdks/event/README.md#revert_backfill) - Revert a backfill
* [search](docs/sdks/event/README.md#search) - Search events

### [invoice](docs/sdks/invoice/README.md)

* [create](docs/sdks/invoice/README.md#create) - Create invoice line item
* [fetch](docs/sdks/invoice/README.md#fetch) - Retrieve an Invoice
* [fetch_upcoming](docs/sdks/invoice/README.md#fetch_upcoming) - Retrieve upcoming invoice
* [list](docs/sdks/invoice/README.md#list) - List invoices
* [void](docs/sdks/invoice/README.md#void) - Void an invoice

### [plan](docs/sdks/plan/README.md)

* [fetch](docs/sdks/plan/README.md#fetch) - Retrieve a plan
* [get_by_external_id](docs/sdks/plan/README.md#get_by_external_id) - Retrieve a plan by external plan ID
* [list](docs/sdks/plan/README.md#list) - List plans

### [subscription](docs/sdks/subscription/README.md)

* [cancel](docs/sdks/subscription/README.md#cancel) - Cancel subscription
* [create](docs/sdks/subscription/README.md#create) - Create subscription
* [fetch](docs/sdks/subscription/README.md#fetch) - Retrieve a subscription
* [fetch_costs](docs/sdks/subscription/README.md#fetch_costs) - View subscription costs
* [fetch_schedule](docs/sdks/subscription/README.md#fetch_schedule) - View subscription schedule
* [fetch_usage](docs/sdks/subscription/README.md#fetch_usage) - View subscription usage
* [list](docs/sdks/subscription/README.md#list) - List subscriptions
* [schedule_plan_change](docs/sdks/subscription/README.md#schedule_plan_change) - Schedule plan change
* [unschedule_cancellation](docs/sdks/subscription/README.md#unschedule_cancellation) - Unschedule pending cancellation
* [unschedule_plan_change](docs/sdks/subscription/README.md#unschedule_plan_change) - Unschedule pending plan changes
* [update_fixed_fee_quantity](docs/sdks/subscription/README.md#update_fixed_fee_quantity) - Update fixed fee quantity
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
