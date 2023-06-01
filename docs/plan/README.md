# plan

## Overview

The Plan resource represents a plan that can be subscribed to by a customer. Plans define the amount of credits that a customer will receive, the price of the plan, and the billing interval.

### Available Operations

* [fetch](#fetch) - Retrieve a plan
* [get_by_external_id](#get_by_external_id) - Retrieve a plan by external plan ID
* [list](#list) - List plans

## fetch

This endpoint is used to fetch [plan](../guides/concepts##plan-and-price) details given a plan identifier. It returns information about the prices included in the plan and their configuration, as well as the product that the plan is attached to.

## Serialized prices
Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a given [Price](../guides/concepts#plan-and-price) object. The `model_type` field determines the key for the configuration object that is present. A detailed explanation of price types can be found in the [Price schema](../guides/concepts#plan-and-price). 

## Phases
Orb supports plan phases, also known as contract ramps. For plans with phases, the serialized prices refer to all prices across all phases.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.plan.fetch('rerum')

if res.plan is not None:
    # handle response
```

## get_by_external_id

This endpoint is used to fetch [plan](../guides/concepts##plan-and-price) details given an external_plan_id identifier. It returns information about the prices included in the plan and their configuration, as well as the product that the plan is attached to.

## Serialized prices
Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a given [Price](../guides/concepts#plan-and-price) object. The `model_type` field determines the key for the configuration object that is present. A detailed explanation of price types can be found in the [Price schema](../guides/concepts#plan-and-price). 

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


res = s.plan.get_by_external_id('adipisci', shared.Plan(
    base_plan=shared.PlanBasePlan(
        external_plan_id='asperiores',
        id='e49a8d9c-bf48-4633-b23f-9b77f3a41006',
        name='Bertha Thompson',
    ),
    base_plan_id='voluptas',
    created_at=dateutil.parser.isoparse('2022-08-22T21:20:36.034Z'),
    currency='atque',
    default_invoice_memo='sit',
    description='fugiat',
    discount=shared.Discount(
        amount_discount='ab',
        applies_to_price_ids=[
            'dolorum',
            'iusto',
            'voluptate',
        ],
        discount_type=shared.DiscountType.PERCENTAGE,
        percentage_discount=0.15,
        trial_amount_discount='dolorum',
        usage_discount=5365.79,
    ),
    external_plan_id='omnis',
    id='ebf737ae-4203-4ce5-a6a9-5d8a0d446ce2',
    invoicing_currency='dolorum',
    minimum=shared.MinimumAmount(
        applies_to_price_ids=[
            'esse',
            'harum',
            'iusto',
            'ipsum',
        ],
        minimum_amount='quisquam',
    ),
    name='Marvin Renner',
    net_terms=313692,
    plan_phases=[
        shared.PlanPhase(
            description='sapiente',
            discount=shared.Discount(
                amount_discount='totam',
                applies_to_price_ids=[
                    'sit',
                    'expedita',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='neque',
                usage_discount=1536.94,
            ),
            duration=424685,
            duration_unit=shared.DurationUnit.ANNUAL,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'deserunt',
                    'quam',
                ],
                minimum_amount='ipsum',
            ),
            name='Norma McGlynn',
            order=747080,
        ),
    ],
    prices=[
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='a8422bb6-79d2-4322-b15b-f0cbb1e31b8b',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=5844.76,
                per_unit_maximum='aperiam',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=2091.57,
                        maximum_amount='dolore',
                        per_unit_maximum='labore',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=2408.29,
                        maximum_amount='dolorum',
                        per_unit_maximum='architecto',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=630.38,
                        maximum_amount='aut',
                        per_unit_maximum='quas',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=9295.3,
                        maximum_amount='consequatur',
                        per_unit_maximum='est',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='porro',
                        unit_amount='doloribus',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='ut',
                        unit_amount='facilis',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='cupiditate',
                        unit_amount='qui',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='quae',
                        unit_amount='laudantium',
                    ),
                ],
            ),
            cadence=shared.Cadence.MONTHLY,
            created_at=dateutil.parser.isoparse('2021-01-17T10:17:06.805Z'),
            currency='USD',
            discount=shared.Discount(
                amount_discount='quisquam',
                applies_to_price_ids=[
                    'omnis',
                    'quis',
                    'ipsum',
                    'delectus',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='voluptate',
                usage_discount=2317.01,
            ),
            fixed_price_quantity=8788.7,
            id='f7fbc7ab-d74d-4d39-80f5-d2cff7c70a45',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='ea',
                dimensions=[
                    'vel',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'ratione',
                            'ex',
                        ],
                        unit_amount='laudantium',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'dolor',
                        ],
                        unit_amount='maiores',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'ex',
                        ],
                        unit_amount='nulla',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'voluptatibus',
                            'nostrum',
                            'sapiente',
                        ],
                        unit_amount='quisquam',
                    ),
                ],
            ),
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'ea',
                    'impedit',
                    'corporis',
                    'veniam',
                ],
                minimum_amount='aliquid',
            ),
            model_type=shared.PriceModelType.UNIT,
            name='Rosemary Ryan',
            package_config=shared.PricePackageConfig(
                package_amount='aspernatur',
                package_size=3253.1,
            ),
            plan_phase_order=534.27,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=7255.95,
                        maximum_amount='aut',
                        minimum_amount='aut',
                        per_unit_maximum='deleniti',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=7705.81,
                        maximum_amount='aliquam',
                        minimum_amount='fugit',
                        per_unit_maximum='accusamus',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=795.22,
                        maximum_amount='non',
                        minimum_amount='et',
                        per_unit_maximum='dolorum',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=6720.48,
                        maximum_amount='placeat',
                        minimum_amount='velit',
                        per_unit_maximum='eum',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='nobis',
                        last_unit='quas',
                        unit_amount='assumenda',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='nulla',
                        last_unit='voluptas',
                        unit_amount='libero',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='quasi',
            ),
        ),
    ],
    product=shared.PlanProduct(
        created_at=dateutil.parser.isoparse('2022-09-29T12:13:01.368Z'),
        id='29074747-78a7-4bd4-a6d2-8c10ab3cdca4',
        name='Brittany Bernier II',
    ),
    trial_config=shared.PlanTrialConfig(
        trial_period=8920.5,
        trial_period_unit=shared.PlanTrialConfigTrialPeriodUnit.DAYS,
    ),
))

if res.plan is not None:
    # handle response
```

## list

This endpoint returns a list of all [plans](../guides/concepts##plan-and-price) for an account in a list format. 

The list of plans is ordered starting from the most recently created plan. The response also includes [`pagination_metadata`](../api/pagination), which lets the caller retrieve the next page of results if they exist.


### Example Usage

```python
import orb


s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.plan.list()

if res.plans is not None:
    # handle response
```
