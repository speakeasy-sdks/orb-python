# Orb

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/orb-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PostCustomersRequestBody(
    billing_address=operations.PostCustomersRequestBodyBillingAddress(
        city="Laruecester",
        country="US",
        line1="quibusdam",
        line2="unde",
        postal_code="58466-3428",
        state="ipsa",
    ),
    currency="delectus",
    email="Geraldine_Kreiger52@gmail.com",
    external_customer_id="iusto",
    name="excepturi",
    payment_provider="bill.com",
    payment_provider_id="recusandae",
    shipping_address=operations.PostCustomersRequestBodyShippingAddress(
        city="Belleville",
        country="US",
        line1="quis",
        line2="veritatis",
        postal_code="03897-1889",
        state="molestiae",
    ),
    timezone="Etc/UTC",
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
