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


res = s.plan.fetch('blanditiis')

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


res = s.plan.get_by_external_id('error', shared.Plan(
    base_plan=shared.PlanBasePlan(
        external_plan_id='eaque',
        id='9b3fe49a-8d9c-4bf4-8633-323f9b77f3a4',
        name='Melissa Bednar',
    ),
    base_plan_id='quaerat',
    created_at=dateutil.parser.isoparse('2020-11-29T12:05:35.198Z'),
    currency='voluptatibus',
    default_invoice_memo='voluptas',
    description='natus',
    discount=shared.Discount(
        amount_discount='eos',
        applies_to_price_ids=[
            'sit',
            'fugiat',
            'ab',
        ],
        discount_type=shared.DiscountDiscountType.PERCENTAGE,
        percentage_discount=0.15,
        trial_amount_discount='soluta',
        usage_discount=6793.93,
    ),
    external_plan_id='iusto',
    id='7a89ebf7-37ae-4420-bce5-e6a95d8a0d44',
    invoicing_currency='vel',
    minimum=shared.MinimumAmount(
        applies_to_price_ids=[
            'officiis',
            'qui',
            'dolorum',
            'a',
        ],
        minimum_amount='esse',
    ),
    name='Tyrone Emard',
    net_terms=229442,
    plan_phases=[
        shared.PlanPhase(
            description='accusamus',
            discount=shared.Discount(
                amount_discount='numquam',
                applies_to_price_ids=[
                    'dolorem',
                    'sapiente',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='totam',
                usage_discount=4717.52,
            ),
            duration=25662,
            duration_unit=shared.PlanPhaseDurationUnit.ANNUAL,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'sed',
                ],
                minimum_amount='vel',
            ),
            name='Glen Oberbrunner',
            order=277628,
        ),
        shared.PlanPhase(
            description='qui',
            discount=shared.Discount(
                amount_discount='cupiditate',
                applies_to_price_ids=[
                    'pariatur',
                    'soluta',
                    'dicta',
                    'laborum',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='totam',
                usage_discount=2768.94,
            ),
            duration=132068,
            duration_unit=shared.PlanPhaseDurationUnit.MONTHLY,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'facilis',
                    'aliquid',
                    'quam',
                ],
                minimum_amount='molestias',
            ),
            name='Shawn Doyle',
            order=488056,
        ),
        shared.PlanPhase(
            description='sunt',
            discount=shared.Discount(
                amount_discount='ullam',
                applies_to_price_ids=[
                    'hic',
                    'voluptatem',
                    'cumque',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='soluta',
                usage_discount=7486.64,
            ),
            duration=92596,
            duration_unit=shared.PlanPhaseDurationUnit.ANNUAL,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'veritatis',
                ],
                minimum_amount='nobis',
            ),
            name='Dr. Randolph McDermott',
            order=292147,
        ),
    ],
    prices=[
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='3a1108e0-adcf-44b9-a187-9fce953f73ef',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=4922.68,
                per_unit_maximum='hic',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=7992.03,
                        maximum_amount='odio',
                        per_unit_maximum='similique',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=7085.48,
                        maximum_amount='vero',
                        per_unit_maximum='ducimus',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=2930.2,
                        maximum_amount='quibusdam',
                        per_unit_maximum='illum',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='natus',
                        unit_amount='impedit',
                    ),
                ],
            ),
            cadence=shared.PriceCadence.ANNUAL,
            created_at=dateutil.parser.isoparse('2021-12-16T18:42:11.269Z'),
            currency='USD',
            discount=shared.Discount(
                amount_discount='nulla',
                applies_to_price_ids=[
                    'porro',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='maiores',
                usage_discount=9850.33,
            ),
            fixed_price_quantity=4783.7,
            id='c70a4562-6d43-4681-bf16-d9f5fce6c556',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='inventore',
                dimensions=[
                    'ea',
                    'quo',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'aspernatur',
                            'minima',
                            'eaque',
                            'a',
                        ],
                        unit_amount='libero',
                    ),
                ],
            ),
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'aut',
                ],
                minimum_amount='deleniti',
            ),
            model_type=shared.PriceModelType.BULK_BPS,
            name='Mrs. Denise Tillman MD',
            package_config=shared.PricePackageConfig(
                package_amount='laborum',
                package_size=8104.24,
            ),
            plan_phase_order=2453.67,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=4205.39,
                        maximum_amount='nobis',
                        minimum_amount='quas',
                        per_unit_maximum='assumenda',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=8605.52,
                        maximum_amount='voluptas',
                        minimum_amount='libero',
                        per_unit_maximum='quasi',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='numquam',
                        last_unit='explicabo',
                        unit_amount='provident',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='ipsa',
                        last_unit='molestiae',
                        unit_amount='magnam',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='odio',
            ),
        ),
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='4778a7bd-466d-428c-90ab-3cdca4251904',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=8920.5,
                per_unit_maximum='ipsam',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=1970.54,
                        maximum_amount='quo',
                        per_unit_maximum='esse',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='aperiam',
                        unit_amount='distinctio',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='quod',
                        unit_amount='dignissimos',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='inventore',
                        unit_amount='nihil',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='totam',
                        unit_amount='accusamus',
                    ),
                ],
            ),
            cadence=shared.PriceCadence.ANNUAL,
            created_at=dateutil.parser.isoparse('2022-06-04T04:43:25.138Z'),
            currency='USD',
            discount=shared.Discount(
                amount_discount='commodi',
                applies_to_price_ids=[
                    'dolores',
                    'deserunt',
                    'molestiae',
                    'accusantium',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='porro',
                usage_discount=4304.02,
            ),
            fixed_price_quantity=5564.29,
            id='8282aa48-2562-4f22-ae98-17ee17cbe61e',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='vel',
                dimensions=[
                    'molestiae',
                    'rerum',
                    'occaecati',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'eligendi',
                            'sit',
                            'culpa',
                        ],
                        unit_amount='tempore',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'cumque',
                        ],
                        unit_amount='consequuntur',
                    ),
                ],
            ),
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'minus',
                ],
                minimum_amount='quaerat',
            ),
            model_type=shared.PriceModelType.MATRIX,
            name='Joy Labadie',
            package_config=shared.PricePackageConfig(
                package_amount='nulla',
                package_size=5578.11,
            ),
            plan_phase_order=4572.23,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=9518.75,
                        maximum_amount='error',
                        minimum_amount='sint',
                        per_unit_maximum='pariatur',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='quia',
                        last_unit='eveniet',
                        unit_amount='asperiores',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='facere',
                        last_unit='veritatis',
                        unit_amount='consequuntur',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='quasi',
                        last_unit='similique',
                        unit_amount='culpa',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='aliquid',
                        last_unit='tenetur',
                        unit_amount='quae',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='earum',
            ),
        ),
    ],
    product=shared.PlanProduct(
        created_at=dateutil.parser.isoparse('2022-07-21T16:57:57.397Z'),
        id='4bdb04f1-5756-4082-968e-a19f1d170513',
        name='Ms. Cora Spencer IV',
    ),
    trial_config=shared.PlanTrialConfig(
        trial_period=4287.96,
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

if res.list_plans_200_application_json_object is not None:
    # handle response
```
