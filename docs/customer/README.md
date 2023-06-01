# customer

## Overview

The Customer resource represents a customer of your service. Customers are created when a customer is created in your service, and are updated when a customer's information is updated in your service.

### Available Operations

* [amend](#amend) - Amend customer usage
* [amend_by_external_id](#amend_by_external_id) - Amend customer usage by external ID
* [create](#create) - Create customer
* [create_transaction](#create_transaction) - Create a customer balance transaction
* [delete](#delete) - Delete a customer
* [fetch](#fetch) - Retrieve a customer
* [fetch_by_external_id](#fetch_by_external_id) - Retrieve a customer by external ID
* [fetch_costs](#fetch_costs) - View customer costs
* [fetch_costs_by_external_id](#fetch_costs_by_external_id) - View customer costs by external customer ID
* [fetch_transactions](#fetch_transactions) - Get customer balance transactions
* [list](#list) - List customers
* [update_by_external_id](#update_by_external_id) - Update a customer by external ID
* [update_customer](#update_customer) - Update customer

## amend

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
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.amend('architecto', [
    shared.Event(
        customer_id='reiciendis',
        event_name='est',
        external_customer_id='mollitia',
        idempotency_key='laborum',
        properties={
            "dolorem": 'corporis',
        },
        timestamp='2020-12-09T16:09:53Z',
    ),
], '2022-03-01T05:00:00Z', dateutil.parser.isoparse('2022-02-01T05:00:00Z'))

if res.amended_usage is not None:
    # handle response
```

## amend_by_external_id

This endpoint's resource and semantics exactly mirror [Amend customer usage](amend-usage) but operates on an [external customer ID](../guides/events-and-metrics/customer-aliases) rather than an Orb issued identifier.

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.amend_by_external_id('explicabo', [
    shared.Event(
        customer_id='enim',
        event_name='omnis',
        external_customer_id='nemo',
        idempotency_key='minima',
        properties={
            "accusantium": 'iure',
            "culpa": 'doloribus',
            "sapiente": 'architecto',
        },
        timestamp='2020-12-09T16:09:53Z',
    ),
    shared.Event(
        customer_id='mollitia',
        event_name='dolorem',
        external_customer_id='culpa',
        idempotency_key='consequuntur',
        properties={
            "mollitia": 'occaecati',
            "numquam": 'commodi',
            "quam": 'molestiae',
            "velit": 'error',
        },
        timestamp='2020-12-09T16:09:53Z',
    ),
    shared.Event(
        customer_id='quia',
        event_name='quis',
        external_customer_id='vitae',
        idempotency_key='laborum',
        properties={
            "enim": 'odit',
            "quo": 'sequi',
            "tenetur": 'ipsam',
        },
        timestamp='2020-12-09T16:09:53Z',
    ),
    shared.Event(
        customer_id='id',
        event_name='possimus',
        external_customer_id='aut',
        idempotency_key='quasi',
        properties={
            "temporibus": 'laborum',
            "quasi": 'reiciendis',
            "voluptatibus": 'vero',
        },
        timestamp='2020-12-09T16:09:53Z',
    ),
], '2022-03-01T05:00:00Z', dateutil.parser.isoparse('2022-02-01T05:00:00Z'))

if res.amended_usage is not None:
    # handle response
```

## create

This operation is used to create an Orb customer, who is party to the core billing relationship. See [Customer](../guides/concepts#customer) for an overview of the customer resource.

This endpoint is critical in the following Orb functionality:
* Automated charges can be configured by setting `payment_provider` and `payment_provider_id` to automatically issue invoices
* [Customer ID Aliases](../guides/events-and-metrics/customer-aliases) can be configured by setting `external_customer_id`
* [Timezone localization](../guides/product-catalog/timezones) can be configured on a per-customer basis by setting the `timezone` parameter

### Example Usage

```python
import orb
from orb.models import shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.NewCustomer(
    auto_collection=False,
    billing_address=shared.BillingAddress(
        city='Johnworth',
        country='US',
        line1='ipsa',
        line2='omnis',
        postal_code='70042',
        state='maiores',
    ),
    currency='dicta',
    email='Elena68@yahoo.com',
    external_customer_id='enim',
    metadata={
        "commodi": 'repudiandae',
        "quae": 'ipsum',
        "quidem": 'molestias',
        "excepturi": 'pariatur',
    },
    name='Irma Ledner DVM',
    payment_provider=shared.PaymentProvider.STRIPE_CHARGE,
    payment_provider_id='veritatis',
    shipping_address=shared.ShippingAddress(
        city='El Monte',
        country='US',
        line1='enim',
        line2='consequatur',
        postal_code='81678-2213',
        state='cupiditate',
    ),
    tax_id=shared.CustomerTaxID(
        country='Marshall Islands',
        type='perferendis',
        value='magni',
    ),
    timezone='Etc/UTC',
)

res = s.customer.create(req)

if res.customer is not None:
    # handle response
```

## create_transaction

Creates an immutable balance transaction that updates the customer's balance and returns back the newly created transaction.

### Example Usage

```python
import orb
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.create_transaction('assumenda', shared.NewTransaction(
    amount='1.00',
    description='ipsam',
    type=shared.NewTransactionType.INCREMENT,
))

if res.transaction is not None:
    # handle response
```

## delete

This performs a deletion of this customer, its subscriptions, and its invoices. This operation is irreversible. Note that this is a _soft_ deletion, but the data will be inaccessible through the API and Orb dashboard. For hard-deletion, please reach out to the Orb team directly.

**Note**: This operation happens asynchronously and can be expected to take a few minutes to propagate to related resources. However, querying for the customer on subsequent GET requests while deletion is in process will reflect its deletion with a `deleted: true` property. Once the customer deletion has been fully processed, the customer will not be returned in the API.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.delete('fugit')

if res.status_code == 200:
    # handle response
```

## fetch

This endpoint is used to fetch customer details given an identifier. If the `Customer` is in the process of being deleted, only the properties `id` and `deleted: true` will be returned.

See the [Customer resource](Orb-API.json/components/schemas/Customer) for a full discussion of the Customer model.


### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.fetch('dolorum')

if res.customer is not None:
    # handle response
```

## fetch_by_external_id

This endpoint is used to fetch customer details given an `external_customer_id` (see [Customer ID Aliases](../guides/events-and-metrics/customer-aliases)).

Note that the resource and semantics of this endpoint exactly mirror [Get Customer](fetch-customer).

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.fetch_by_external_id('excepturi')

if res.customer is not None:
    # handle response
```

## fetch_costs

This endpoint is used to fetch a day-by-day snapshot of a customer's costs in Orb, calculated by applying pricing information to the underlying usage (see the [subscription usage endpoint](gcription-usage) to fetch usage per metric, in usage units rather than a currency). 

This endpoint can be leveraged for internal tooling and to provide a more transparent billing experience for your end users:

1. Understand the cost breakdown per line item historically and in real-time for the current billing period. 
2. Provide customer visibility into how different services are contributing to the overall invoice with a per-day timeseries (as compared to the [upcoming invoice](fetch-upcoming-invoice) resource, which represents a snapshot for the current period).
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
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FetchCustomerCostsRequest(
    customer_id='tempora',
    group_by='facilis',
    timeframe_end='2022-03-01T05:00:00Z',
    timeframe_start=dateutil.parser.isoparse('2022-02-01T05:00:00Z'),
    view_mode=shared.ViewMode.CUMULATIVE,
)

res = s.customer.fetch_costs(req)

if res.customer_costs is not None:
    # handle response
```

## fetch_costs_by_external_id

This endpoint's resource and semantics exactly mirror [View customer costs](fetch-customer-costs) but operates on an [external customer ID](../guides/events-and-metrics/customer-aliases) rather than an Orb issued identifier.

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FetchCustomerCostsExternalIDRequest(
    external_customer_id='labore',
    group_by='delectus',
    timeframe_end='2022-03-01T05:00:00Z',
    timeframe_start=dateutil.parser.isoparse('2022-02-01T05:00:00Z'),
    view_mode=shared.ViewMode.PERIODIC,
)

res = s.customer.fetch_costs_by_external_id(req)

if res.customer_costs is not None:
    # handle response
```

## fetch_transactions

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
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.fetch_transactions('non')

if res.transactions is not None:
    # handle response
```

## list



This endpoint returns a list of all customers for an account. The list of customers is ordered starting from the most recently created customer. This endpoint follows Orb's [standardized pagination format](../api/pagination).

See [Customer](../guides/concepts#customer) for an overview of the customer model.

### Example Usage

```python
import orb


s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.list()

if res.customers is not None:
    # handle response
```

## update_by_external_id

This endpoint is used to update customer details given an `external_customer_id` (see [Customer ID Aliases](../guides/events-and-metrics/customer-aliases)).

Note that the resource and semantics of this endpoint exactly mirror [Update Customer](update-customer).

### Example Usage

```python
import orb
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.update_by_external_id('eligendi', shared.NewCustomer(
    auto_collection=False,
    billing_address=shared.BillingAddress(
        city='Gracestead',
        country='US',
        line1='necessitatibus',
        line2='sint',
        postal_code='28964-4896',
        state='dicta',
    ),
    currency='magnam',
    email='Raquel_Jenkins@hotmail.com',
    external_customer_id='accusamus',
    metadata={
        "occaecati": 'enim',
    },
    name='Toby Pouros',
    payment_provider=shared.PaymentProvider.STRIPE_INVOICE,
    payment_provider_id='blanditiis',
    shipping_address=shared.ShippingAddress(
        city='Verlieburgh',
        country='US',
        line1='deserunt',
        line2='nisi',
        postal_code='66404',
        state='magnam',
    ),
    tax_id=shared.CustomerTaxID(
        country='Portugal',
        type='id',
        value='labore',
    ),
    timezone='Etc/UTC',
))

if res.customer is not None:
    # handle response
```

## update_customer

This endpoint can be used to update the `payment_provider`, `payment_provider_id`, `name`, `email`, `email_delivery`, `auto_collection`, `shipping_address`, and `billing_address` of an existing customer.

Other fields on a customer are currently immutable.

### Example Usage

```python
import orb
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.customer.update_customer('labore', shared.NewCustomer(
    auto_collection=False,
    billing_address=shared.BillingAddress(
        city='New Nellie',
        country='US',
        line1='eum',
        line2='vero',
        postal_code='12053',
        state='provident',
    ),
    currency='quos',
    email='Alexis_OHara32@yahoo.com',
    external_customer_id='eum',
    metadata={
        "necessitatibus": 'odit',
    },
    name='Joyce Kertzmann',
    payment_provider=shared.PaymentProvider.BILL_COM,
    payment_provider_id='maxime',
    shipping_address=shared.ShippingAddress(
        city='Mckennaport',
        country='US',
        line1='architecto',
        line2='architecto',
        postal_code='37498-1980',
        state='consequuntur',
    ),
    tax_id=shared.CustomerTaxID(
        country='Lithuania',
        type='natus',
        value='magni',
    ),
    timezone='Etc/UTC',
))

if res.customer is not None:
    # handle response
```
