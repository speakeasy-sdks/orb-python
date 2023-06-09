# subscription

## Overview

The Subscription resource represents a customer's subscription to a plan. Subscriptions are created when a customer subscribes to a plan, and are updated when a customer's plan is changed.

### Available Operations

* [cancel](#cancel) - Cancel subscription
* [create](#create) - Create subscription
* [fetch](#fetch) - Retrieve a subscription
* [fetch_costs](#fetch_costs) - View subscription costs
* [fetch_schedule](#fetch_schedule) - View subscription schedule
* [fetch_usage](#fetch_usage) - View subscription usage
* [list](#list) - List subscriptions
* [schedule_plan_change](#schedule_plan_change) - Schedule plan change
* [unschedule_cancellation](#unschedule_cancellation) - Unschedule pending cancellation
* [unschedule_plan_change](#unschedule_plan_change) - Unschedule pending plan changes
* [update_fixed_fee_quantity](#update_fixed_fee_quantity) - Update fixed fee quantity

## cancel

This endpoint can be used to cancel an existing subscription. It returns the serialized subscription object with an `end_date` parameter that signifies when the subscription will transition to an ended state.

The body parameter `cancel_option` determines the cancellation behavior. Orb supports two cancellation options: 

- `end_of_subscription_term`: stops the subscription from auto-renewing. Subscriptions that have been cancelled with this option can still incur charges for the remainder of their term:
    - Issuing this cancellation request for a monthly subscription will keep the subscription active until the start of the subsequent month, and potentially issue an invoice for any usage charges incurred in the intervening period.
    - Issuing this cancellation request for a quarterly subscription will keep the subscription active until the end of the quarter and potentially issue an invoice for any usage charges incurred in the intervening period.
    - Issuing this cancellation request for a yearly subscription will keep the subscription active for the full year. For example, a yearly subscription starting on 2021-11-01 and cancelled on 2021-12-08 will remain active until 2022-11-01 and potentially issue charges in the intervening months for any recurring monthly usage charges in its plan.
    - **Note**: If a subscription's plan contains prices with difference cadences, the end of term date will be determined by the largest cadence value. For example, cancelling end of term for a subscription with a quarterly fixed fee with a monthly usage fee will result in the subscription ending at the end of the quarter.

- `immediate`: ends the subscription immediately, setting the `end_date` to the current time:
  - Subscriptions that have been cancelled with this option will be invoiced immediately. This invoice will include any usage fees incurred in the billing period up to the cancellation, along with any prorated recurring fees for the billing period, if applicable. 
  - **Note**: If the subscription has a recurring fee that was paid in-advance, the prorated amount for the remaining time period will be added to the [customer's balance](list-balance-transactions) upon immediate cancellation. However, if the customer is ineligible to use the customer balance, the subscription cannot be cancelled immediately.
  
- `requested_date`: ends the subscription on a specified date, which requires a `cancellation_date` to be passed in. If no timezone is provided, the customer's timezone is used.  For example, a subscription starting on January 1st with a monthly price can be set to be cancelled on the first of any month after January 1st (e.g. March 1st, April 1st, May 1st). A subscription with multiple prices with different cadences defines the "term" to be the highest cadence of the prices.


Upcoming subscriptions are only eligible for immediate cancellation, which will set the `end_date` equal to the `start_date` upon cancellation.

## Backdated cancellations
Orb allows you to cancel a subscription in the past as long as there are no paid invoices between the `requested_date` and the current time. If the cancellation is after the latest issued invoice, Orb will generate a balance refund for the current period. If the cancellation is before the most recently issued invoice, Orb will void the intervening invoice and generate a new one based on the new dates for the subscription. See the section on [cancellation behaviors](../guides/product-catalog/subscription-management).

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.subscription.cancel('nobis', shared.SubscriptionCancellation(
    cancel_option=shared.CancelOptions.IMMEDIATE,
    cancellation_date=dateutil.parser.isoparse('2017-07-21T17:32:28Z'),
))

if res.subscription is not None:
    # handle response
```

## create

A subscription represents the purchase of a plan by a customer. The customer is identified by either the `customer_id` or the `external_customer_id`, and exactly one of these fields must be provided.

By default, subscriptions begin on the day that they're created and renew automatically for each billing cycle at the cadence that's configured in the plan definition.

The default configuration for subscriptions in Orb is **In-advance billing** and **Beginning of month alignment** (see [Subscription](../guides/concepts#subscription) for more details).

In order to change the alignment behavior, Orb also supports billing subscriptions on the day of the month they are created. If `align_billing_with_subscription_start_date = true` is specified, subscriptions have billing cycles that are aligned with their `start_date`. For example, a subscription that begins on January 15th will have a billing cycle from January 15th to February 15th. Every subsequent billing cycle will continue to start and invoice on the 15th.

If the "day" value is greater than the number of days in the month, the next billing cycle will start at the end of the month. For example, if the start_date is January 31st, the next billing cycle will start on February 28th.

If a customer was created with a currency, Orb only allows subscribing the customer to a plan with a matching `invoicing_currency`. If the customer does not have a currency set, on subscription creation, we set the customer's currency to be the `invoicing_currency` of the plan.

## Price overrides

Price overrides are used to update some or all prices in a plan for the specific subscription being created. This is useful when a new customer has negotiated one or more different prices for a specific plan than the plan's default prices. Any type of price can be overridden, if the correct data is provided. The billable metric, cadence, type, and name of a price can not be overridden.


To override prices, provide a list of objects with the key `price_overrides`. The price object in the list of overrides is expected to contain the existing price id, the `model_type` and config value in the format below. The specific numerical values can be updated, but the config value and `model_type` must match the existing price that is being overridden

### Request format for price overrides

Orb supports a few different pricing models out of the box. The `model_type` field determines the key for the configuration object that is present.

### Unit pricing

With unit pricing, each unit costs a fixed amount.

```json
{
    ...
    "id": "price_id",
    "model_type": "unit",
    "unit_config": {
       "unit_amount": "0.50"
    }
    ...
}
```

### Tiered pricing

In tiered pricing, the cost of a given unit depends on the tier range that it falls into, where each tier range is defined by an upper and lower bound. For example, the first ten units may cost $0.50 each and all units thereafter may cost $0.10 each. Tiered prices can be overridden with a new number of tiers or new values for `first_unit`, `last_unit`, or `unit_amount`.

```json
{
    ...
    "id": "price_id",
    "model_type": "tiered",
    "tiered_config": {
        "tiers": [ 
           {
                "first_unit":"1",
                "last_unit": "10",
                "unit_amount": "0.50"
            },
            {
                "first_unit": "10",
                "last_unit": null,
                "unit_amount": "0.10"
            }
        ]
    }
    ...
}
```

### Bulk pricing

Bulk pricing applies when the number of units determine the cost of _all_ units. For example, if you've bought less than 10 units, they may each be $0.50 for a total of $5.00. Once you've bought more than 10 units, all units may now be priced at $0.40 (i.e. 101 units total would be $40.40). Bulk prices can be overridden with a new number of tiers or new values for `maximum_units`, or `unit_amount`.

```json
{
    ...
    "id": "price_id",
    "model_type": "bulk",
    "bulk_config": {
        "tiers": [ 
            {
                "maximum_units": "10",
                "unit_amount": "0.50"
            },
            {
                "maximum_units": "1000",
                "unit_amount": "0.40"
            }
          ]
    }
    ...
}
```
### Package pricing

```json
{
    ...
    "id": "price_id",
    "model_type": "package",
    "package_config": {
       "package_amount": "0.80",
       "package_size": 10
    }
    ...
 }
 ```
### BPS pricing

BPS pricing specifies a per-event (e.g. per-payment) rate in one hundredth of a percent (the number of basis points to charge), as well as a cap per event to assess. For example, this would allow you to assess a fee of 0.25% on every payment you process, with a maximum charge of $25 per payment.

```json
{
    ...
    "id": "price_id"
    "model_type": "bps",
    "bps_config": {
       "bps": 125,
       "per_event_cap": "11.00"
    }
    ...
 }
```
### Bulk BPS pricing

Bulk BPS pricing specifies BPS parameters in a tiered manner, dependent on the total quantity across all events. Similar to bulk pricing, the BPS parameters of a given event depends on the tier range that the billing period falls into. Each tier range is defined by an upper and lower bound. For example, after $1.5M of payment volume is reached, each individual payment may have a lower cap or a smaller take-rate.

```json
{
    ...
    "id": "price_id"
    "model_type": "bulk_bps",
    "bulk_bps_config": {
        "tiers": [ 
           {
                "minimum_amount": "0.00",
                "maximum_amount": "1000000.00",
                "bps": 125,
                "per_event_cap": "19.00"
           },
          {
                "minimum_amount":"1000000.00",
                "maximum_amount": null,
                "bps": 115,
                "per_event_cap": "4.00"
            }
        ]
    }
    ...
 }
```
### Tiered BPS pricing
Tiered BPS pricing specifies BPS parameters in a graduated manner, where an event's applicable parameter is a function of its marginal addition to the period total. Similar to tiered pricing, the BPS parameters of a given event depends on the tier range that it falls into, where each tier range is defined by an upper and lower bound. For example, the first few payments may have a 0.8 BPS take-rate and all payments after a specific volume may incur a take-rate of 0.5 BPS each.

```json
{
    ...
    "id": "price_id"
    "model_type": "tiered_bps",
    "tiered_bps_config": {
        "tiers": [ 
           {
                "minimum_amount": "0.00",
                "maximum_amount": "1000000.00",
                "bps": 125,
                "per_event_cap": "19.00"
           },
          {
                "minimum_amount":"1000000",
                "maximum_amount": null,
                "bps": 115,
                "per_event_cap": "4.00"
            }
        ]
    }
    ...
 }
```
### Matrix pricing
Matrix pricing defines a set of unit prices in a one or two-dimensional matrix. `dimensions` defines the two event property values evaluated in this pricing model. In a one-dimensional matrix, the second value is `null`. Every configuration has a list of `matrix_values` which give the unit prices for specified property values. In a one-dimensional matrix, the matrix values will have `dimension_values` where the second value of the pair is null. If an event does not match any of the dimension values in the matrix, it will resort to the `default_unit_amount`.
```json
...
"model_type": "matrix"
"matrix_config": {
    "default_unit_amount": "3.00",
    "dimensions": [
        "cluster_name",
        "region"
    ],
    "matrix_values": [
        {
            "dimension_values": [
                "alpha",
                "west"
            ],
            "unit_amount": "2.00"
        },
        ...
    ]
}
...
```

### Fixed fees
Fixed fees follow unit pricing, and also have an additional parameter `fixed_price_quantity` that indicates how many of a fixed fee that should be applied for a subscription. This parameter defaults to 1. 

```json
{
    ...
    "id": "price_id",
    "model_type": "unit",
    "unit_config": {
       "unit_amount": "2.00"
    },
    "fixed_price_quantity": 3.0
    ...
}
```

## Minimums
Minimums, much like price overrides, can be useful when a new customer has negotiated a new or different minimum than the default for the plan. Minimums can be added to either a price or a plan. If a minimum exists for a price or plan and null is provided for the minimum override on creation, then there will be no minimum on the new subscription. If no minimum is provided, then the default plan minimum is used.

To add a minimum for a specific price, add `minimum_amount` to the specific price in the `price_overrides` object. To add a minimum to a plan, add `minimum_amount` to the base object. The value for `minimum_amount` should be a string with the minimum dollar amount in decimal format.


### Minimum override example

Price minimum override example:

```json
{
    ...
    "id": "price_id",
    "model_type": "unit",
    "unit_config": {
        "unit_amount": "0.50"
    },
    "minimum_amount": "100.00"
    ...
}
```


Plan minimum override example:

```json
{
    "customer_id": "customer_id",
    "plan_id": "plan_id",
    "minimum_amount": "1000.00",
    "price_overrides": [ ... ]
    ...
}
```

Removing an existing minimum example
```json
{
    ...
    "id": "price_id",
    "model_type": "unit",
    "unit_config": {
        "unit_amount": "0.50"
    },
    "minimum_amount": null
    ...
}
```

Using the plan's minimum example
```json
{
    ...
    "id": "price_id",
    "model_type": "unit",
    "unit_config": {
        "unit_amount": "0.50"
    },
    ...
}
```

## Discounts
Discounts, like price overrides, can be useful when a new customer has negotiated a new or custom discount than the default for the plan. Discounts can be added to either a price or a plan, and a single plan or price can have at most one discount. If a discount exists for a price or a plan and a null discount is provided on creation, then there will be no discount on the new subscription.

To add a discount for a specific price, add `discount` to the price in the `price_overrides` object. To add a discount to a plan, add `discount` to the base object. 
Discount should be a dictionary of the format:
```json
{
  "discount_type": "amount" | "percentage" | "usage", 
  "amount_discount": string, 
  "percentage_discount": string,
  "usage_discount": string
}
```
where either `amount_discount`, `percentage_discount`, or `usage_discount` is provided.

The `usage` type discount can only be created on individual prices and not on the plan.

Price discount example
```json
{
  ...
  "id": "price_id",
  "model_type": "unit",
  "unit_config": {
      "unit_amount": "0.50"
  },
  "discount": {"discount_type": "amount", "amount_discount": "175"},
}
```

Plan discount example
```json
{
    "customer_id": "customer_id",
    "plan_id": "plan_id",
    "discount": {"discount_type": "percentage", "percentage_discount": "12.5"},
    "price_overrides": [ ... ]
    ...
}
```

Removing an existing discount example
```json
{
    "customer_id": "customer_id",
    "plan_id": "plan_id",
    "discount": null,
    "price_overrides": [ ... ]
    ...
}
```

Using the plan's discount example
```json
{
    ...
    "id": "price_id",
    "model_type": "unit",
    "unit_config": {
        "unit_amount": "0.50"
    },
    ...
}
```

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.NewSubscription(
    align_billing_with_subscription_start_date=False,
    auto_collection=False,
    coupon_redemption_code='sit',
    customer_id='97DPcZE9hxsbb9Y9',
    default_invoice_memo='rerum',
    external_customer_id='sed',
    external_marketplace=shared.ExternalMarketplace.GOOGLE,
    external_marketplace_reporting_id='project_number:983410661111',
    external_plan_id='reiciendis',
    metadata={
        "asperiores": 'facilis',
    },
    minimum_amount='1.23',
    net_terms=0,
    phase_overrides=[
        shared.PhaseOverride(
            discount=shared.Discount(
                amount_discount='expedita',
                applies_to_price_ids=[
                    'iste',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='dolore',
                usage_discount=6719.07,
            ),
            minimum_amount='sed',
            order=4475.16,
        ),
        shared.PhaseOverride(
            discount=shared.Discount(
                amount_discount='commodi',
                applies_to_price_ids=[
                    'explicabo',
                    'voluptas',
                    'unde',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='architecto',
                usage_discount=3828.08,
            ),
            minimum_amount='sapiente',
            order=8953.86,
        ),
    ],
    plan_id='ZMwNQefe7J3ecf7W',
    price_overrides=[
        shared.TieredBPSPriceOverride(
            id='08f4294e-3698-4f44-bf60-3e8b445e80ca',
            minimum_amount='1.23',
            model_type=shared.TieredBpsModelType.TIERED_BPS,
            tiered_bps_config=shared.TieredBPSPriceOverrideTieredBPSConfig(
                tiers=[
                    shared.TieredBPSPriceOverrideTieredBPSConfigTiers(
                        bps=3295.43,
                        maximum_amount='recusandae',
                        minimum_amount='reiciendis',
                        per_unit_maximum='nulla',
                    ),
                    shared.TieredBPSPriceOverrideTieredBPSConfigTiers(
                        bps=1685.76,
                        maximum_amount='aperiam',
                        minimum_amount='saepe',
                        per_unit_maximum='numquam',
                    ),
                ],
            ),
        ),
    ],
    start_date=dateutil.parser.parse('2022-01-01').date(),
)

res = s.subscription.create(req)

if res.subscription is not None:
    # handle response
```

## fetch

This endpoint is used to fetch a [Subscription](../guides/concepts#subscription) given an identifier.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.subscription.fetch('veniam')

if res.subscription is not None:
    # handle response
```

## fetch_costs

This endpoint is used to fetch a day-by-day snapshot of a subscription's costs in Orb, calculated by applying pricing information to the underlying usage (see the [subscription usage endpoint](fetch-subscription-usage) to fetch usage per metric, in usage units rather than a currency). 


The semantics of this endpoint exactly mirror those of [fetching a customer's costs](fetch-customer-costs). Use this endpoint to limit your analysis of costs to a specific subscription for the customer (e.g. to de-aggregate costs when a customer's subscription has started and stopped on the same day).

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.FetchSubscriptionCostsRequest(
    group_by='in',
    subscription_id='officiis',
    timeframe_end='2022-03-01T05:00:00Z',
    timeframe_start=dateutil.parser.isoparse('2022-02-01T05:00:00Z'),
    view_mode=shared.ViewMode.PERIODIC,
)

res = s.subscription.fetch_costs(req)

if res.subscription_costs is not None:
    # handle response
```

## fetch_schedule

This endpoint returns a [paginated](../api/pagination) list of all plans associated with a subscription along with their start and end dates. This list contains the subscription's initial plan along with past and future plan changes.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.subscription.fetch_schedule('laudantium')

if res.subscription_schedule is not None:
    # handle response
```

## fetch_usage

This endpoint is used to fetch a subscription's usage in Orb. Especially when combined with optional query parameters, this endpoint is a powerful way to build visualizations on top of Orb's event data and metrics.

With no query parameters specified, this endpoint returns usage for the subscription's _current billing period_ across each billable metric that participates in the subscription. Usage quantities returned are the result of evaluating the metric definition for the entirety of the customer's billing period.

### Default response shape

Orb returns a `data` array with an object corresponding to each billable metric. Nested within this object is a `usage` array which has a `quantity` value and a corresponding `timeframe_start` and `timeframe_end`.  The `quantity` value represents the calculated usage value for the billable metric over the specified timeframe (inclusive of the `timeframe_start` timestamp and exclusive of the `timeframe_end` timestamp).

Orb will include _every_ window in the response starting from the beginning of the billing period, even when there were no events (and therefore no usage) in the window. This increases the size of the response but prevents the caller from filling in gaps and handling cumbersome time-based logic.

The query parameters in this endpoint serve to override this behavior and provide some key functionality, as listed below. Note that this functionality can also be used _in conjunction_ with each other, e.g. to display grouped usage on a custom timeframe.

## Custom timeframe

In order to view usage for a custom timeframe rather than the current billing period, specify a `timeframe_start` and `timeframe_end`. This will calculate quantities for usage incurred between timeframe_start (inclusive) and timeframe_end (exclusive), i.e. `[timeframe_start, timeframe_end)`.

Note:
- These timestamps must be specified in ISO 8601 format and UTC timezone, e.g. `2022-02-01T05:00:00Z`.
- Both parameters must be specified if either is specified.

## Grouping by custom attributes
In order to view a single metric grouped by a specific _attribute_ that each event is tagged with (e.g. `cluster`), you must additionally specify a `billable_metric_id` and a `group_by` key. The `group_by` key denotes the event property on which to group. 

When returning grouped usage, only usage for `billable_metric_id` is  returned, and a separate object in the `data` array is returned for each value of the `group_by` key present in your events. The `quantity` value is the result of evaluating the billable metric for events filtered to a single value of the `group_by` key.

Orb expects that events that match the billable metric will contain values in the `properties` dictionary that correspond to the `group_by` key specified. By default, Orb will not return a `null` group (i.e. events that match the metric but do not have the key set). Currently, it is only possible to view usage grouped by a single attribute at a time.

The following example shows usage for an "API Requests" billable metric grouped by `region`. Note the extra `metric_group` dictionary in the response, which provides metadata about the group:

```json
{
  "data": [
    {
      "usage": [
        {
          "quantity": 0.19291,
          "timeframe_start": "2021-10-01T07:00:00Z",
          "timeframe_end": "2021-10-02T07:00:00Z",
        },
        ...
      ],
      “metric_group”: {
         “property_key”: “region”,
         “property_value”: “asia/pacific”
      },
      "billable_metric": {
        "id": "Fe9pbpMk86xpwdGB",
        "name": "API Requests"
       },
      "view_mode": "periodic"
    },
    ...
  ]
}
```

## Windowed usage
The `granularity` parameter can be used to _window_ the usage `quantity` value into periods. When not specified, usage is returned for the entirety of the time range. 

When `granularity = day` is specified with a timeframe longer than a day, Orb will return a `quantity` value for each full day between `timeframe_start` and `timeframe_end`. Note that the days are demarcated by the _customer's local midnight_.

For example, with `timeframe_start = 2022-02-01T05:00:00Z`, `timeframe_end = 2022-02-04T01:00:00Z` and `granularity=day`, the following windows will be returned for a customer in the `America/Los_Angeles` timezone since local midnight is `08:00` UTC:
- `[2022-02-01T05:00:00Z, 2022-02-01T08:00:00Z)`
- `[2022-02-01T08:00:00, 2022-02-02T08:00:00Z)`
- `[2022-02-02T08:00:00, 2022-02-03T08:00:00Z)`
- `[2022-02-03T08:00:00, 2022-02-04T01:00:00Z)`

```json
{
    "data": [
        {
            "billable_metric": {
                "id": "Q8w89wjTtBdejXKsm",
                "name": "API Requests"
            },
            "usage": [
                {
                    "quantity": 0,
                    "timeframe_end": "2022-02-01T08:00:00+00:00",
                    "timeframe_start": "2022-02-01T05:00:00+00:00"
                },
                {
                    "quantity": 0,
                    "timeframe_end": "2022-02-02T08:00:00+00:00",
                    "timeframe_start": "2022-02-01T08:00:00+00:00"
                },
                {
                    "quantity": 0,
                    "timeframe_end": "2022-02-03T08:00:00+00:00",
                    "timeframe_start": "2022-02-02T08:00:00+00:00"
                },
                {
                    "quantity": 0,
                    "timeframe_end": "2022-02-04T01:00:00+00:00",
                    "timeframe_start": "2022-02-03T08:00:00+00:00"
                }
            ],
            "view_mode": "periodic"
        },
        ...
    ]
}
```

## Decomposable vs. non-decomposable metrics
Billable metrics fall into one of two categories: decomposable and non-decomposable. A decomposable billable metric, such as a sum or a count, can be displayed and aggregated across arbitrary timescales. On the other hand, a non-decomposable metric is not meaningful when only a slice of the billing window is considered. 

As an example, if we have a billable metric that's defined to count unique users, displaying a graph of unique users for each day is not representative of the billable metric value over the month (days could have an overlapping set of 'unique' users). Instead, what's useful for any given day is the number of unique users in the billing period so far, which are the _cumulative_ unique users.

Accordingly, this endpoint returns treats these two types of metrics differently when `group_by` is specified:
- Decomposable metrics can be grouped by any event property.
- Non-decomposable metrics can only be grouped by the corresponding price's invoice grouping key. If no invoice grouping key is present, the metric does not support `group_by`.

## Matrix prices
When a billable metric is attached to a price that uses matrix pricing, it's important to view usage grouped by those matrix dimensions. In this case, use the query parameters `first_dimension_key`, `first_dimension_value` and `second_dimension_key`, `second_dimension_value` while filtering to a specific `billable_metric_id`. 

For example, if your compute metric has a separate unit price (i.e. a matrix pricing model) per `region` and `provider`, your request might provide the following parameters:

- `first_dimension_key`: `region`
- `first_dimension_value`: `us-east-1` 
- `second_dimension_key`: `provider`
- `second_dimension_value`: `aws`

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.FetchSubscriptionUsageRequest(
    billable_metric_id='exercitationem',
    granularity=operations.FetchSubscriptionUsageGranularity.DAY,
    group_by='praesentium',
    subscription_id='cum',
    timeframe_end='2022-03-01T05:00:00Z',
    timeframe_start=dateutil.parser.isoparse('2022-02-01T05:00:00Z'),
    view_mode=shared.ViewMode.PERIODIC,
)

res = s.subscription.fetch_usage(req)

if res.subscription_usage is not None:
    # handle response
```

## list

This endpoint returns a list of all subscriptions for an account as a [paginated](../api/pagination) list, ordered starting from the most recently created subscription. For a full discussion of the subscription resource, see [Subscription](../guides/concepts#subscription).

Subscriptions can be filtered to a single customer by passing in the `customer_id` query parameter or the `external_customer_id` query parameter. 

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.subscription.list('dolorum', 'voluptatum')

if res.subscriptions is not None:
    # handle response
```

## schedule_plan_change

This endpoint can be used to change the plan on an existing subscription. It returns the serialized updated subscription object.

The body parameter `change_option` determines the timing of the plan change. Orb supports three options: 

- `end_of_subscription_term`: changes the plan at the end of the existing plan's term.
    - Issuing this plan change request for a monthly subscription will keep the existing plan active until the start of the subsequent month, and potentially issue an invoice for any usage charges incurred in the intervening period.
    - Issuing this plan change request for a yearly subscription will keep the existing plan active for the full year.

- `immediate`: changes the plan immediately. Subscriptions that have their plan changed with this option will be invoiced immediately. This invoice will include any usage fees incurred in the billing period up to the change, along with any prorated recurring fees for the billing period, if applicable.

- `requested_date`: changes the plan on the requested date (`change_date`). If no timezone is provided, the customer's timezone is used. The `change_date` body parameter is required if this option is chosen.

Note that one of `plan_id` or `external_plan_id` is required in the request body for this operation.

## Price overrides and minimums
Price overrides are used to update some or all prices in the target plan. Minimums, much like price overrides, can be useful when a new customer has negotiated a new or different minimum than the default for the plan. The request format for price overrides and minimums are the same as those in [subscription creation](create-subscription).

## Prorations for in-advance fees
By default, Orb calculates the prorated difference in any fixed fees when making a plan change, adjusting the customer balance as needed. For details on this behavior, [Subscription management](../guides/product-catalog/subscription-management).

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.subscription.schedule_plan_change('error', shared.SubscriptionPlanChange(
    align_billing_with_plan_change_date=False,
    change_date=dateutil.parser.isoparse('2017-07-21T17:32:28Z'),
    change_option=shared.ChangeOptions.IMMEDIATE,
    coupon_redemption_code='expedita',
    external_plan_id='ZMwNQefe7J3ecf7W',
    minimum_amount='1.23',
    plan_id='ZMwNQefe7J3ecf7W',
    price_overrides=[
        shared.UnitPriceOverride(
            id='a5aa8e48-24d0-4ab4-8750-88e51862065e',
            minimum_amount='1.23',
            model_type=shared.UnitModelType.UNIT,
            unit_config=shared.UnitPriceOverrideUnitConfig(
                unit_amount='error',
            ),
        ),
        shared.TieredPriceOverride(
            id='mqBkze6HoCwL4ytV',
            minimum_amount='1.23',
            model_type=shared.TieredModelType.TIERED,
            tiered_config=shared.TieredPriceOverrideTieredConfig(
                tiers=[
                    shared.TieredPriceOverrideTieredConfigTiers(
                        first_unit='0',
                        last_unit='10',
                        unit_amount='2.5',
                    ),
                    shared.TieredPriceOverrideTieredConfigTiers(
                        first_unit='0',
                        last_unit='10',
                        unit_amount='2.5',
                    ),
                ],
            ),
        ),
        shared.TieredBPSPriceOverride(
            id='3b1194b8-abf6-403a-b9f9-dfe0ab7da8a5',
            minimum_amount='1.23',
            model_type=shared.TieredBpsModelType.TIERED_BPS,
            tiered_bps_config=shared.TieredBPSPriceOverrideTieredBPSConfig(
                tiers=[
                    shared.TieredBPSPriceOverrideTieredBPSConfigTiers(
                        bps=7908.4,
                        maximum_amount='repudiandae',
                        minimum_amount='quasi',
                        per_unit_maximum='atque',
                    ),
                ],
            ),
        ),
        shared.PackagePriceOverride(
            id='f86bc173-d689-4eee-9526-f8d986e881ea',
            minimum_amount='1.23',
            model_type=shared.PackageModelType.PACKAGE,
            package_config=shared.PackagePriceOverridePackageConfig(
                num_units=8298.98,
                unit_amount='labore',
            ),
        ),
    ],
))

if res.subscription is not None:
    # handle response
```

## unschedule_cancellation

This endpoint can be used to unschedule any pending cancellations for a subscription. 

To be eligible, the subscription must currently be active and have a future cancellation ("Auto-renew turned off"). This operation will turn on auto-renew, ensuring that the subscription does not end at the currently scheduled cancellation time.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.subscription.unschedule_cancellation('reiciendis')

if res.subscription is not None:
    # handle response
```

## unschedule_plan_change

This endpoint can be used to unschedule any pending plan changes on an existing subscription.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.subscription.unschedule_plan_change('doloremque')

if res.subscription is not None:
    # handle response
```

## update_fixed_fee_quantity

This endpoint can be used to update the quantity for a fixed fee.

To be eligible, the subscription must currently be active and the price specified must be a fixed fee (not usage-based). This operation will immediately update the quantity for the fee, or if a `effective_date` is passed in, will update the quantity on the requested date at midnight in the customer's timezone. 

In order to change the fixed fee quantity as of the next draft invoice for this subscription, pass `change_option=upcoming_invoice` without an `effective_date` specified.

If the fee is an in-advance fixed fee, it will also issue an immediate invoice for the difference for the remainder of the billing period.

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.subscription.update_fixed_fee_quantity('repudiandae', shared.FixedFeeQuantityChange(
    change_option=shared.FeeChangeOption.EFFECTIVE_DATE,
    effective_date=dateutil.parser.parse('"2022-12-21"').date(),
    price_id='dicta',
    quantity=360.33,
))

if res.subscription is not None:
    # handle response
```
