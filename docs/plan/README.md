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
        api_key_auth="",
    ),
)


res = s.plan.fetch('quam')

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
        api_key_auth="",
    ),
)


res = s.plan.get_by_external_id('ipsum', shared.Plan(
    base_plan=shared.PlanBasePlan(
        external_plan_id='incidunt',
        id='29cdb1a8-422b-4b67-9d23-22715bf0cbb1',
        name='Dale Boehm',
    ),
    base_plan_id='tempore',
    created_at=dateutil.parser.isoparse('2022-11-28T16:49:52.722Z'),
    currency='delectus',
    default_invoice_memo='dolorem',
    description='dolore',
    discount=shared.Discount(
        amount_discount='labore',
        applies_to_price_ids=[
            'dolorum',
        ],
        discount_type=shared.DiscountType.PERCENTAGE,
        percentage_discount=0.15,
        trial_amount_discount='architecto',
        usage_discount=630.38,
    ),
    external_plan_id='aut',
    id='8e0adcf4-b921-4879-bce9-53f73ef7fbc7',
    invoicing_currency='similique',
    minimum=shared.MinimumAmount(
        applies_to_price_ids=[
            'vero',
            'ducimus',
            'dolore',
        ],
        minimum_amount='quibusdam',
    ),
    name='Earl Mosciski DVM',
    net_terms=347233,
    plan_phases=[
        shared.PlanPhase(
            description='fugit',
            discount=shared.Discount(
                amount_discount='porro',
                applies_to_price_ids=[
                    'doloribus',
                    'iusto',
                    'eligendi',
                    'ducimus',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='alias',
                usage_discount=6394.73,
            ),
            duration=269479,
            duration_unit=shared.DurationUnit.QUARTERLY,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'aspernatur',
                    'vel',
                ],
                minimum_amount='possimus',
            ),
            name='Paula Jacobs I',
            order=980700,
        ),
        shared.PlanPhase(
            description='quasi',
            discount=shared.Discount(
                amount_discount='ex',
                applies_to_price_ids=[
                    'excepturi',
                    'voluptatibus',
                    'nostrum',
                    'sapiente',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='quisquam',
                usage_discount=9065.56,
            ),
            duration=411372,
            duration_unit=shared.DurationUnit.ANNUAL,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'veniam',
                    'aliquid',
                ],
                minimum_amount='inventore',
            ),
            name='Rosemary Ryan',
            order=132487,
        ),
        shared.PlanPhase(
            description='minima',
            discount=shared.Discount(
                amount_discount='eaque',
                applies_to_price_ids=[
                    'libero',
                    'aut',
                    'aut',
                    'deleniti',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='impedit',
                usage_discount=3045.82,
            ),
            duration=146946,
            duration_unit=shared.DurationUnit.ANNUAL,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'non',
                ],
                minimum_amount='et',
            ),
            name='Neal Schroeder',
            order=420539,
        ),
        shared.PlanPhase(
            description='nobis',
            discount=shared.Discount(
                amount_discount='quas',
                applies_to_price_ids=[
                    'nulla',
                    'voluptas',
                    'libero',
                    'quasi',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='tempora',
                usage_discount=2561.39,
            ),
            duration=131482,
            duration_unit=shared.DurationUnit.QUARTERLY,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'molestiae',
                ],
                minimum_amount='magnam',
            ),
            name='Esther Koch',
            order=683282,
        ),
    ],
    prices=[
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='bd466d28-c10a-4b3c-9ca4-251904e523c7',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=9251.64,
                per_unit_maximum='aperiam',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=7997.96,
                        maximum_amount='dignissimos',
                        per_unit_maximum='inventore',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=4694.98,
                        maximum_amount='totam',
                        per_unit_maximum='accusamus',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=3068.1,
                        maximum_amount='odio',
                        per_unit_maximum='occaecati',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='sapiente',
                        unit_amount='dolores',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='deserunt',
                        unit_amount='molestiae',
                    ),
                ],
            ),
            cadence=shared.Cadence.ANNUAL,
            created_at=dateutil.parser.isoparse('2021-09-16T17:01:25.429Z'),
            currency='USD',
            discount=shared.Discount(
                amount_discount='quas',
                applies_to_price_ids=[
                    'consequuntur',
                    'deleniti',
                    'fugit',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='fuga',
                usage_discount=6494.63,
            ),
            fixed_price_quantity=2775.96,
            id='82562f22-2e98-417e-a17c-be61e6b7b95b',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='eligendi',
                dimensions=[
                    'culpa',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'cumque',
                        ],
                        unit_amount='consequuntur',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'minus',
                        ],
                        unit_amount='quaerat',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'consectetur',
                            'esse',
                            'blanditiis',
                            'provident',
                        ],
                        unit_amount='a',
                    ),
                ],
            ),
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'quas',
                    'esse',
                    'quasi',
                    'a',
                ],
                minimum_amount='error',
            ),
            model_type=shared.PriceModelType.BPS,
            name='Rufus Crona',
            package_config=shared.PricePackageConfig(
                package_amount='facere',
                package_size=850.01,
            ),
            plan_phase_order=1594.14,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=6288.99,
                        maximum_amount='culpa',
                        minimum_amount='aliquid',
                        per_unit_maximum='tenetur',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='earum',
                        last_unit='vel',
                        unit_amount='in',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='eius',
            ),
        ),
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='bdb04f15-7560-482d-a8ea-19f1d1705133',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=6144.65,
                per_unit_maximum='temporibus',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=5223.71,
                        maximum_amount='aut',
                        per_unit_maximum='laudantium',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='mollitia',
                        unit_amount='ab',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='corrupti',
                        unit_amount='non',
                    ),
                ],
            ),
            cadence=shared.Cadence.ANNUAL,
            created_at=dateutil.parser.isoparse('2022-06-03T05:52:14.954Z'),
            currency='USD',
            discount=shared.Discount(
                amount_discount='numquam',
                applies_to_price_ids=[
                    'explicabo',
                    'voluptas',
                    'aut',
                    'dignissimos',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='dicta',
                usage_discount=9816.4,
            ),
            fixed_price_quantity=6184.8,
            id='3f5f0642-dac7-4af5-95cc-413aa63aae8d',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='vel',
                dimensions=[
                    'quos',
                    'vel',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'facilis',
                            'cum',
                            'commodi',
                            'in',
                        ],
                        unit_amount='corporis',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'assumenda',
                            'nemo',
                            'recusandae',
                            'aliquid',
                        ],
                        unit_amount='aperiam',
                    ),
                ],
            ),
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'consectetur',
                    'in',
                    'exercitationem',
                ],
                minimum_amount='earum',
            ),
            model_type=shared.PriceModelType.BULK_BPS,
            name='Melba Homenick',
            package_config=shared.PricePackageConfig(
                package_amount='saepe',
                package_size=8970.71,
            ),
            plan_phase_order=2965.56,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=9920.12,
                        maximum_amount='adipisci',
                        minimum_amount='non',
                        per_unit_maximum='amet',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='dignissimos',
                        last_unit='a',
                        unit_amount='debitis',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='consectetur',
            ),
        ),
    ],
    product=shared.PlanProduct(
        created_at=dateutil.parser.isoparse('2022-04-24T05:37:47.670Z'),
        id='60eb1ea4-2655-45ba-bc28-744ed53b88f3',
        name='Byron Stroman',
    ),
    trial_config=shared.PlanTrialConfig(
        trial_period=3487.83,
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
        api_key_auth="",
    ),
)


res = s.plan.list()

if res.plans is not None:
    # handle response
```
