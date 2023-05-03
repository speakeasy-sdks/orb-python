# customer

## Overview

Actions related to customer management.

### Available Operations

* [create](#create) - Create customer
* [get](#get) - Retrieve a customer
* [get_balance](#get_balance) - Get customer balance transactions
* [get_by_external_id](#get_by_external_id) - Retrieve a customer by external ID
* [get_costs](#get_costs) - View customer costs
* [get_costs_by_external_id](#get_costs_by_external_id) - View customer costs by external customer ID
* [list](#list) - List customers
* [update](#update) - Update customer
* [update_by_external_id](#update_by_external_id) - Update a customer by external ID
* [update_usage](#update_usage) - Amend customer usage
* [update_usage_by_external_id](#update_usage_by_external_id) - Amend customer usage by external ID

## create

This operation is used to create an Orb customer, who is party to the core billing relationship. See [Customer](../reference/Orb-API.json/components/schemas/Customer) for an overview of the customer resource.

This endpoint is critical in the following Orb functionality:
* Automated charges can be configured by setting `payment_provider` and `payment_provider_id` to automatically issue invoices
* [Customer ID Aliases](../docs/Customer-ID-Aliases.md) can be configured by setting `external_customer_id`
* [Timezone localization](../docs/Timezone-localization.md) can be configured on a per-customer basis by setting the `timezone` parameter

### Example Usage

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
        city='Fort Manuelachester',
        country='US',
        line1='laborum',
        line2='dolores',
        postal_code='31736',
        state='nemo',
    ),
    created_at=dateutil.parser.isoparse('2022-06-06T21:04:34.044Z'),
    currency='accusantium',
    email='Lorenza.Yundt65@yahoo.com',
    external_customer_id='dolorem',
    id='a2fa9467-7392-451a-a52c-3f5ad019da1f',
    name='Caleb Koss',
    payment_provider=shared.CustomerPaymentProviderEnum.STRIPE,
    payment_provider_id='omnis',
    shipping_address=shared.ShippingAddress(
        city='Myrtistown',
        country='US',
        line1='doloremque',
        line2='reprehenderit',
        postal_code='91324',
        state='dicta',
    ),
    timezone='America/Los_Angeles',
)

res = s.customer.create(req)

if res.customer is not None:
    # handle response
```

## get

This endpoint is used to fetch customer details given an identifier.

See the [Customer resource](Orb-API.json/components/schemas/Customer) for a full discussion of the Customer model.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetCustomersCustomerIDRequest(
    customer_id='harum',
)

res = s.customer.get(req)

if res.customer is not None:
    # handle response
```

## get_balance

# The customer balance

The customer balance is an amount in the customer's currency, which Orb automatically applies to subsequent invoices. This balance can be adjusted manually via Orb's webapp on the customer details page. You can use this balance to provide a fixed mid-period credit to the customer. Commonly, this is done due to system downtime/SLA violation, or an adhoc adjustment discussed with the customer.

If the balance is a positive value at the time of invoicing, it represents that the customer has credit that should be used to offset the amount due on the next issued invoice. In this case, Orb will automatically reduce the next invoice by the balance amount, and roll over any remaining balance if the invoice is fully discounted.

If the balance is a negative value at the time of invoicing, Orb will increase the invoice's amount due with a positive adjustment, and reset the balance to 0.

This endpoint retrieves all customer balance transactions in reverse chronological order for a single customer, providing a complete audit trail of all adjustments and invoice applications.

## Eligibility

The customer balance can only be applied to invoices or adjusted manually if invoices are not synced to a separate invoicing provider. If a payment gateway such as Stripe is used, the balance will be applied to the invoice before forwarding payment to the gateway.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetCustomersCustomerIDBalanceTransactionsRequest(
    customer_id='enim',
)

res = s.customer.get_balance(req)

if res.get_customers_customer_id_balance_transactions_200_application_json_object is not None:
    # handle response
```

## get_by_external_id

This endpoint is used to fetch customer details given an `external_customer_id` (see [Customer ID Aliases](../docs/Customer-ID-Aliases.md)).

Note that the resource and semantics of this endpoint exactly mirror [Get Customer](Orb-API.json/paths/~1customers/get).

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetCustomersExternalCustomerIDExternalCustomerIDRequest(
    external_customer_id='accusamus',
)

res = s.customer.get_by_external_id(req)

if res.customer is not None:
    # handle response
```

## get_costs

This endpoint is used to fetch a day-by-day snapshot of a customer's costs in Orb, calculated by applying pricing information to the underlying usage (see the [subscription usage endpoint](../reference/Orb-API.json/paths/~1subscriptions~1{subscription_id}~1usage/get) to fetch usage per metric, in usage units rather than a currency). 

This endpoint can be leveraged for internal tooling and to provide a more transparent billing experience for your end users:

1. Understand the cost breakdown per line item historically and in real-time for the current billing period. 
2. Provide customer visibility into how different services are contributing to the overall invoice with a per-day timeseries (as compared to the [upcoming invoice](../reference/Orb-API.json/paths/~1invoices~1upcoming/get) resource, which represents a snapshot for the current period).
3. Assess how minimums and discounts affect your customers by teasing apart costs directly as a result of usage, as opposed to minimums and discounts at the plan and price level.
4. Gain insight into key customer health metrics, such as the percent utilization of the minimum committed spend.

## Fetching subscriptions
By default, this endpoint fetches the currently active subscription for the customer, and returns cost information for the subscription's current billing period, broken down by each participating price. If there are no currently active subscriptions, this will instead default to the most recently active subscription or return an empty series if none are found. For example, if your plan charges for compute hours, job runs, and data syncs, then this endpoint would provide a daily breakdown of your customer's cost for each of those axes.

If timeframe bounds are specified, Orb fetches all subscriptions that were active in that timeframe. If two subscriptions overlap on a single day, costs from each price will be summed, and prices for both subscriptions will be included in the breakdown.


## Prepaid plans
For plans that include prices which deduct credits rather than accrue in-arrears charges in a billable currency, this endpoint will return the total deduction amount, in credits, for the specified timeframe. 


## Cumulative subtotals and totals

Since the subtotal and total must factor in any billing-period level discounts and minimums, it's most meaningful to consider costs relative to the start of the subscription's billing period. As a result, by default this endpoint returns cumulative totals since the beginning of the billing period. In particular, the `timeframe_start` of a returned timeframe window is *always* the beginning of the billing period and `timeframe_end` is incremented one day at a time to build the result.

A customer that uses a few API calls a day but has a minimum commitment might exhibit the following pattern for their subtotal and total in the first few days of the month. Here, we assume that each API call is $2.50, the customer's plan has a monthly minimum of $50 for this price, and that the subscription's billing period bounds are aligned to the first of the month:

| timeframe_start | timeframe_end | Cumulative usage | Subtotal | Total (incl. commitment)  |
| -----------| ----------- | ----------- | ----------- |----------- |
| 2023-02-01 | 2023-02-02 | 9 | $22.50 | $50.00 |
| 2023-02-01 | 2023-02-03 | 19 | $47.50 | $50.00 |
| 2023-02-01 | 2023-02-04 | 20 | $50.00 | $50.00 |
| 2023-02-01 | 2023-02-05 | 28 | $70.00 | $70.00 |
| 2023-02-01 | 2023-02-06 | 36 | $90.00 | $90.00 |


### Periodic values
When the query parameter `view_mode=periodic` is specified, Orb will return an incremental day-by-day view of costs. In this case, there will always be a one-day difference between `timeframe_start` and `timeframe_end` for the timeframes returned. This is a transform on top of the cumulative costs, calculated by taking the difference of each timeframe with the last. Note that in the above example, the `Total` value would be 0 for the second two data points, since the minimum commitment has not yet been hit and each day is not contributing anything to the total cost.

## Timeframe bounds
If no timeframe bounds are specified, the response will default to the current billing period for the customer's subscription. For subscriptions that have ended, this will be the billing period when they were last active. If the subscription starts or ends within the timeframe, the response will only include windows where the subscription is active.
 
As noted above, `timeframe_start` for a given cumulative datapoint is always the beginning of the billing period, and `timeframe_end` is incremented one day at a time to construct the response. When a timeframe is passed in that is not aligned to the current subscription's billing period, the response will contain cumulative totals from multiple billing periods.

Suppose the queried customer has a subscription aligned to the 15th of every month. If this endpoint is queried with the date range `2023-06-01` - `2023-07-01`, the first data point will represent about half a billing period's worth of costs, accounting for accruals from the start of the billing period and inclusive of the first day of the timeframe (`timeframe_start = 2023-05-15 00:00:00`, `timeframe_end = 2023-06-02 00:00:00`)

| datapoint index | timeframe_start | timeframe_end |
| ----------- | -----------| ----------- |
| 0 | 2023-05-15 | 2023-06-02 |
| 1 | 2023-05-15 | 2023-06-03 |
| 2 | ... | ... |
| 3 | 2023-05-15 | 2023-06-14 |
| 4 | 2023-06-15 | 2023-06-16 |
| 5 | 2023-06-15 | 2023-06-17 |
| 6 | ... | ... |
| 7 | 2023-06-15 | 2023-07-01 |

You can see this sliced timeframe visualized [here](https://i.imgur.com/TXhYgme.png).

## Grouping by custom attributes
In order to view costs grouped by a specific _attribute_ that each event is tagged with (i.e. `cluster`), you can additionally specify a `group_by` key. The `group_by` key denotes the event property on which to group.

When returning grouped costs, a separate `price_group` object in the `per_price_costs` array is returned for each value of the `group_by` key present in your events. The `subtotal` value of the `per_price_costs` object is the sum of each `price_group`'s total. 

Orb expects events will contain values in the `properties` dictionary that correspond to the `group_by` key specified. By default, Orb will return a `null` group (i.e. events that match the metric but do not have the key set). Currently, it is only possible to view costs grouped by a single attribute at a time.

### Matrix prices
When a price uses matrix pricing, it's important to view costs grouped by those matrix dimensions. Orb will return `price_groups` with the `grouping_key` and `secondary_grouping_key` based on the matrix price definition, for each `grouping_value` and `secondary_grouping_value` available.


### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetCustomerCostsRequest(
    customer_id='commodi',
    group_by='repudiandae',
    timeframe_end='2022-03-01T05:00:00Z',
    timeframe_start=dateutil.parser.isoparse('2022-02-01T05:00:00Z'),
    view_mode=operations.GetCustomerCostsViewModeEnum.PERIODIC,
)

res = s.customer.get_costs(req)

if res.get_customer_costs_200_application_json_object is not None:
    # handle response
```

## get_costs_by_external_id

This endpoint's resource and semantics exactly mirror [View customer costs](../reference/Orb-API.json/paths/~1customers~1{customer_id}~1costs/get) but operates on an [external customer ID](../docs/Customer-ID-Aliases.md) rather than an Orb issued identifier.

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetExternalCustomerCostsRequest(
    external_customer_id='ipsum',
    group_by='quidem',
    timeframe_end='2022-03-01T05:00:00Z',
    timeframe_start=dateutil.parser.isoparse('2022-02-01T05:00:00Z'),
    view_mode=operations.GetExternalCustomerCostsViewModeEnum.CUMULATIVE,
)

res = s.customer.get_costs_by_external_id(req)

if res.get_external_customer_costs_200_application_json_object is not None:
    # handle response
```

## list



This endpoint returns a list of all customers for an account. The list of customers is ordered starting from the most recently created customer. This endpoint follows Orb's [standardized pagination format](../docs/Pagination.md).

See [Customer](../reference/Orb-API.json/components/schemas/Customer) for an overview of the customer model.

### Example Usage

```python
import orb


s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.list()

if res.list_customers_200_application_json_object is not None:
    # handle response
```

## update

This endpoint can be used to update the `payment_provider`, `payment_provider_id`, `name`, `email`, `shipping_address`, and `billing_address` of an existing customer.

Other fields on a customer are currently immutable.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PutCustomersCustomerIDRequest(
    request_body=operations.PutCustomersCustomerIDRequestBody(
        billing_address=operations.PutCustomersCustomerIDRequestBodyBillingAddress(
            city='Samanthaboro',
            country='US',
            line1='praesentium',
            line2='rem',
            postal_code='09509-2306',
            state='quibusdam',
        ),
        email='Luther.Rau26@gmail.com',
        name='Beth McGlynn Sr.',
        payment_provider=operations.PutCustomersCustomerIDRequestBodyPaymentProviderEnum.NULL,
        payment_provider_id='ipsam',
        shipping_address=operations.PutCustomersCustomerIDRequestBodyShippingAddress(
            city='East Marianostead',
            country='US',
            line1='tempora',
            line2='facilis',
            postal_code='29427-5358',
            state='sint',
        ),
    ),
    customer_id='officia',
)

res = s.customer.update(req)

if res.customer is not None:
    # handle response
```

## update_by_external_id

This endpoint is used to update customer details given an `external_customer_id` (see [Customer ID Aliases](../docs/Customer-ID-Aliases.md)).

Note that the resource and semantics of this endpoint exactly mirror [Update Customer](Orb-API.json/paths/~1customers~1{customer_id}/put).

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PutCustomersExternalCustomerIDExternalCustomerIDRequest(
    request_body=operations.PutCustomersExternalCustomerIDExternalCustomerIDRequestBody(
        billing_address=operations.PutCustomersExternalCustomerIDExternalCustomerIDRequestBodyBillingAddress(
            city='Fort Veda',
            country='US',
            line1='dolorum',
            line2='in',
            postal_code='89612',
            state='cumque',
        ),
        email='Hans_Hyatt24@hotmail.com',
        name='Jon Tillman',
        payment_provider=operations.PutCustomersExternalCustomerIDExternalCustomerIDRequestBodyPaymentProviderEnum.STRIPE_INVOICE,
        payment_provider_id='nam',
        shipping_address=operations.PutCustomersExternalCustomerIDExternalCustomerIDRequestBodyShippingAddress(
            city='Kuvalisstad',
            country='US',
            line1='sapiente',
            line2='amet',
            postal_code='34664-0437',
            state='id',
        ),
    ),
    external_customer_id='labore',
)

res = s.customer.update_by_external_id(req)

if res.customer is not None:
    # handle response
```

## update_usage

This endpoint is used to amend usage within a timeframe for a customer that has an active subscription.

This endpoint will mark _all_ existing events within `[timeframe_start, timeframe_end)` as _ignored_  for billing  purposes, and Orb will only use the _new_ events passed in the body of this request as the source of truth for that timeframe moving forwards. Note that a given time period can be amended any number of times, so events can be overwritten in subsequent calls to this endpoint.

This is a powerful and audit-safe mechanism to retroactively change usage data in cases where you need to:
- decrease historical usage consumption because of degraded service availability in your systems
- account for gaps from your usage reporting mechanism
- make point-in-time fixes for specific event records, while retaining the original time of usage and associated metadata

This amendment API is designed with two explicit goals:
1. Amendments are **always audit-safe**. The amendment process will still retain original events in the timeframe, though they will be ignored for billing calculations. For auditing and data fidelity purposes, Orb never overwrites or permanently deletes ingested usage data.
2. Amendments always preserve data **consistency**. In other words, either an amendment is fully processed by the system (and the new events for the timeframe are honored rather than the existing ones) or the amendment request fails. To maintain this important property, Orb prevents _partial event ingestion_ on this endpoint.


## Response semantics
 - Either all events are ingested successfully, or all fail to ingest (returning a `4xx` or `5xx` response code).
- Any event that fails schema validation will lead to a `4xx` response. In this case, to maintain data consistency, Orb will not ingest any events and will also not deprecate existing events in the time period.
- You can assume that the amendment is successful on receipt of a `2xx` response.While a successful response from this endpoint indicates that the new events have been ingested, updating usage totals happens asynchronously and may be delayed by a few minutes. 

As emphasized above, Orb will never show an inconsistent state (e.g. in invoice previews or dashboards); either it will show the existing state (before the amendment) or the new state (with new events in the requested timeframe).


## Sample request body

```json
{
	"events": [{
		"event_name": "payment_processed",
		"timestamp": "2022-03-24T07:15:00Z",
		"properties": {
			"amount": 100
		}
	}, {
		"event_name": "payment_failed",
		"timestamp": "2022-03-24T07:15:00Z",
		"properties": {
			"amount": 100
		}
	}]
}
```

## Request Validation
- The `timestamp` of each event reported must fall within the bounds of `timeframe_start` and `timeframe_end`. As with ingestion, all timestamps must be sent in ISO8601 format with UTC timezone offset.

- Orb **does not accept an `idempotency_key`** with each event in this endpoint, since the entirety of the event list must be ingested to ensure consistency. On retryable errors, you should retry the request in its entirety, and assume that the amendment operation has not succeeded until receipt of a `2xx`.

- Both `timeframe_start` and `timeframe_end` must be timestamps in the past. Furthermore, Orb will generally validate that the `timeframe_start` and `timeframe_end` fall within the customer's _current_ subscription billing period. However, Orb does allow amendments while in the grace period of the previous billing period; in this instance, the timeframe can start before the current period.


## API Limits
Note that Orb does not currently enforce a hard rate-limit for API usage or a maximum request payload size. Similar to the event ingestion API, this API is architected for high-throughput ingestion. It is also safe to _programmatically_ call this endpoint if your system can automatically detect a need for historical amendment.

In order to overwrite timeframes with a very large number of events, we suggest using multiple calls with small adjacent (e.g. every hour) timeframes.

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PatchCustomersCustomerIDUsageRequest(
    request_body=operations.PatchCustomersCustomerIDUsageRequestBody(
        events=[
            operations.PatchCustomersCustomerIDUsageRequestBodyEvents(
                event_name='suscipit',
                properties={
                    "nobis": 'eum',
                    "vero": 'aspernatur',
                    "architecto": 'magnam',
                },
                timestamp='et',
            ),
            operations.PatchCustomersCustomerIDUsageRequestBodyEvents(
                event_name='excepturi',
                properties={
                    "provident": 'quos',
                    "sint": 'accusantium',
                },
                timestamp='mollitia',
            ),
        ],
    ),
    customer_id='reiciendis',
    timeframe_end=dateutil.parser.isoparse('2022-05-11T17:46:20Z'),
    timeframe_start=dateutil.parser.isoparse('2022-05-11T17:46:20Z'),
)

res = s.customer.update_usage(req)

if res.patch_customers_customer_id_usage_200_application_json_object is not None:
    # handle response
```

## update_usage_by_external_id

This endpoint's resource and semantics exactly mirror [Amend customer usage](../reference/Orb-API.json/paths/~1customers~1{customer_id}~1usage/patch) but operates on an [external customer ID](see (../docs/Customer-ID-Aliases.md)) rather than an Orb issued identifier.

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PatchExternalCustomersCustomerIDUsageRequest(
    request_body=operations.PatchExternalCustomersCustomerIDUsageRequestBody(
        events=[
            operations.PatchExternalCustomersCustomerIDUsageRequestBodyEvents(
                event_name='ad',
                properties={
                    "dolor": 'necessitatibus',
                    "odit": 'nemo',
                },
                timestamp='quasi',
            ),
            operations.PatchExternalCustomersCustomerIDUsageRequestBodyEvents(
                event_name='iure',
                properties={
                    "debitis": 'eius',
                    "maxime": 'deleniti',
                    "facilis": 'in',
                    "architecto": 'architecto',
                },
                timestamp='repudiandae',
            ),
            operations.PatchExternalCustomersCustomerIDUsageRequestBodyEvents(
                event_name='ullam',
                properties={
                    "nihil": 'repellat',
                    "quibusdam": 'sed',
                    "saepe": 'pariatur',
                },
                timestamp='accusantium',
            ),
        ],
    ),
    external_customer_id='consequuntur',
    timeframe_end=dateutil.parser.isoparse('2022-05-11T17:46:20Z'),
    timeframe_start=dateutil.parser.isoparse('2022-05-11T17:46:20Z'),
)

res = s.customer.update_usage_by_external_id(req)

if res.patch_external_customers_customer_id_usage_200_application_json_object is not None:
    # handle response
```
