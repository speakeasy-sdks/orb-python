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


res = s.plan.fetch('error')

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


res = s.plan.get_by_external_id('eaque', shared.Plan(
    base_plan=shared.PlanBasePlan(
        external_plan_id='occaecati',
        id='b3fe49a8-d9cb-4f48-a333-23f9b77f3a41',
        name='Angela Kerluke',
    ),
    base_plan_id='accusamus',
    created_at=dateutil.parser.isoparse('2021-01-18T05:23:42.271Z'),
    currency='voluptas',
    default_invoice_memo='natus',
    description='eos',
    discount=shared.Discount(
        amount_discount='atque',
        applies_to_price_ids=[
            'fugiat',
        ],
        discount_type=shared.DiscountDiscountType.PERCENTAGE,
        percentage_discount=0.15,
        trial_amount_discount='ab',
        usage_discount=7438.35,
    ),
    external_plan_id='dolorum',
    id='77a89ebf-737a-4e42-83ce-5e6a95d8a0d4',
    invoicing_currency='tempora',
    minimum=shared.MinimumAmount(
        applies_to_price_ids=[
            'quod',
            'officiis',
        ],
        minimum_amount='qui',
    ),
    name='Randal Klocko',
    net_terms=215507,
    plan_phases=[
        shared.PlanPhase(
            description='tenetur',
            discount=shared.Discount(
                amount_discount='amet',
                applies_to_price_ids=[
                    'accusamus',
                    'numquam',
                    'enim',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='dolorem',
                usage_discount=9574.51,
            ),
            duration=518201,
            duration_unit=shared.PlanPhaseDurationUnit.QUARTERLY,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'expedita',
                ],
                minimum_amount='neque',
            ),
            name='Gina Renner',
            order=463575,
        ),
        shared.PlanPhase(
            description='ipsum',
            discount=shared.Discount(
                amount_discount='incidunt',
                applies_to_price_ids=[
                    'cupiditate',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='maxime',
                usage_discount=8638.56,
            ),
            duration=747080,
            duration_unit=shared.PlanPhaseDurationUnit.MONTHLY,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'totam',
                    'incidunt',
                    'aspernatur',
                ],
                minimum_amount='dolores',
            ),
            name='Cesar Hyatt',
            order=840429,
        ),
        shared.PlanPhase(
            description='qui',
            discount=shared.Discount(
                amount_discount='neque',
                applies_to_price_ids=[
                    'magni',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='odio',
                usage_discount=1248.33,
            ),
            duration=355613,
            duration_unit=shared.PlanPhaseDurationUnit.ANNUAL,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'voluptatem',
                    'cumque',
                    'soluta',
                    'nobis',
                ],
                minimum_amount='et',
            ),
            name='Dale Boehm',
            order=731694,
        ),
        shared.PlanPhase(
            description='cupiditate',
            discount=shared.Discount(
                amount_discount='aperiam',
                applies_to_price_ids=[
                    'dolorem',
                    'dolore',
                    'labore',
                    'adipisci',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='dolorum',
                usage_discount=1002.94,
            ),
            duration=63038,
            duration_unit=shared.PlanPhaseDurationUnit.MONTHLY,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'itaque',
                    'consequatur',
                    'est',
                ],
                minimum_amount='repellendus',
            ),
            name='Domingo Grady',
            order=181631,
        ),
    ],
    prices=[
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='879fce95-3f73-4ef7-bbc7-abd74dd39c0f',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=3472.33,
                per_unit_maximum='nulla',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=7804.27,
                        maximum_amount='maiores',
                        per_unit_maximum='doloribus',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='eligendi',
                        unit_amount='ducimus',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='alias',
                        unit_amount='officia',
                    ),
                ],
            ),
            cadence=shared.PriceCadence.ANNUAL,
            created_at=dateutil.parser.isoparse('2022-08-04T04:05:19.236Z'),
            currency='USD',
            discount=shared.Discount(
                amount_discount='aspernatur',
                applies_to_price_ids=[
                    'possimus',
                    'magnam',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='ratione',
                usage_discount=4011.32,
            ),
            fixed_price_quantity=5113.19,
            id='13f16d9f-5fce-46c5-9614-6c3e250fb008',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='impedit',
                dimensions=[
                    'fugit',
                    'accusamus',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'et',
                            'dolorum',
                        ],
                        unit_amount='laborum',
                    ),
                ],
            ),
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'velit',
                    'eum',
                    'autem',
                    'nobis',
                ],
                minimum_amount='quas',
            ),
            model_type=shared.PriceModelType.BULK_BPS,
            name='Mrs. Shane Reinger',
            package_config=shared.PricePackageConfig(
                package_amount='explicabo',
                package_size=5919.35,
            ),
            plan_phase_order=553.74,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=3015.98,
                        maximum_amount='odio',
                        minimum_amount='eius',
                        per_unit_maximum='esse',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=4561.41,
                        maximum_amount='rem',
                        minimum_amount='fuga',
                        per_unit_maximum='reprehenderit',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='fugiat',
                        last_unit='ut',
                        unit_amount='eum',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='suscipit',
                        last_unit='assumenda',
                        unit_amount='eos',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='praesentium',
                        last_unit='quisquam',
                        unit_amount='veritatis',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='ipsa',
            ),
        ),
    ],
    product=shared.PlanProduct(
        created_at=dateutil.parser.isoparse('2021-08-10T04:36:29.661Z'),
        id='3cdca425-1904-4e52-bc7e-0bc7178e4796',
        name='Todd Oberbrunner DDS',
    ),
    trial_config=shared.PlanTrialConfig(
        trial_period=4304.02,
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
