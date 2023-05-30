# plan

## Overview

The Plan resource represents a plan that can be subscribed to by a customer. Plans define the amount of credits that a customer will receive, the price of the plan, and the billing interval.

### Available Operations

* [fetch](#fetch) - Retrieve a plan
* [get_by_external_id](#get_by_external_id) - Retrieve a plan by external plan ID
* [list](#list) - List plans

## fetch

This endpoint is used to fetch [plan](../reference/Orb-API.json/components/schemas/Plan) details given a plan identifier. It returns information about the prices included in the plan and their configuration, as well as the product that the plan is attached to.

## Serialized prices
Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a given [Price](../reference/Orb-API.json/components/schemas/Price) object. The `model_type` field determines the key for the configuration object that is present. A detailed explanation of price types can be found in the [Price schema](../reference/Orb-API.json/components/schemas/Price). 

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


res = s.plan.fetch('iste')

if res.plan is not None:
    # handle response
```

## get_by_external_id

This endpoint is used to fetch [plan](../reference/Orb-API.json/components/schemas/Plan) details given an external_plan_id identifier. It returns information about the prices included in the plan and their configuration, as well as the product that the plan is attached to.

## Serialized prices
Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a given [Price](../reference/Orb-API.json/components/schemas/Price) object. The `model_type` field determines the key for the configuration object that is present. A detailed explanation of price types can be found in the [Price schema](../reference/Orb-API.json/components/schemas/Price). 

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


res = s.plan.get_by_external_id('dolorum', shared.Plan(
    base_plan=shared.PlanBasePlan(
        external_plan_id='deleniti',
        id='d9cbf486-3332-43f9-b77f-3a4100674ebf',
        name='Faye Daugherty PhD',
    ),
    base_plan_id='ab',
    created_at=dateutil.parser.isoparse('2021-08-23T01:02:18.527Z'),
    currency='iusto',
    default_invoice_memo='voluptate',
    description='dolorum',
    discount=shared.Discount(
        amount_discount='deleniti',
        applies_to_price_ids=[
            'necessitatibus',
            'distinctio',
            'asperiores',
        ],
        discount_type=shared.DiscountDiscountType.PERCENTAGE,
        percentage_discount=0.15,
        trial_amount_discount='nihil',
        usage_discount=2168.97,
    ),
    external_plan_id='voluptate',
    id='ae4203ce-5e6a-495d-8a0d-446ce2af7a73',
    invoicing_currency='quisquam',
    minimum=shared.MinimumAmount(
        applies_to_price_ids=[
            'amet',
            'tempore',
            'accusamus',
            'numquam',
        ],
        minimum_amount='enim',
    ),
    name='Jeannie Leannon MD',
    net_terms=207470,
    plan_phases=[
        shared.PlanPhase(
            description='vel',
            discount=shared.Discount(
                amount_discount='libero',
                applies_to_price_ids=[
                    'deserunt',
                    'quam',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='ipsum',
                usage_discount=2776.28,
            ),
            duration=186458,
            duration_unit=shared.PlanPhaseDurationUnit.QUARTERLY,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'pariatur',
                    'soluta',
                    'dicta',
                    'laborum',
                ],
                minimum_amount='totam',
            ),
            name='Kelly Daniel',
            order=396060,
        ),
    ],
    prices=[
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='9d232271-5bf0-4cbb-9e31-b8b90f3443a1',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=630.38,
                per_unit_maximum='aut',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=9295.3,
                        maximum_amount='consequatur',
                        per_unit_maximum='est',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=8330.38,
                        maximum_amount='porro',
                        per_unit_maximum='doloribus',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=2817.3,
                        maximum_amount='facilis',
                        per_unit_maximum='cupiditate',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='quae',
                        unit_amount='laudantium',
                    ),
                ],
            ),
            cadence=shared.PriceCadence.MONTHLY,
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
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
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
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='44290747-4778-4a7b-9466-d28c10ab3cdc',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=6813.59,
                per_unit_maximum='eius',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=3738.13,
                        maximum_amount='ab',
                        per_unit_maximum='cupiditate',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='tempora',
                        unit_amount='debitis',
                    ),
                ],
            ),
            cadence=shared.PriceCadence.MONTHLY,
            created_at=dateutil.parser.isoparse('2022-10-21T01:48:15.498Z'),
            currency='USD',
            discount=shared.Discount(
                amount_discount='quo',
                applies_to_price_ids=[
                    'recusandae',
                    'aperiam',
                ],
                discount_type=shared.DiscountDiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='distinctio',
                usage_discount=7997.96,
            ),
            fixed_price_quantity=4908.19,
            id='178e4796-f2a7-40c6-8828-2aa482562f22',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='explicabo',
                dimensions=[
                    'occaecati',
                    'atque',
                    'et',
                    'esse',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'veritatis',
                            'esse',
                            'quod',
                            'nam',
                        ],
                        unit_amount='vero',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'quasi',
                            'saepe',
                        ],
                        unit_amount='vel',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'molestiae',
                            'rerum',
                            'occaecati',
                        ],
                        unit_amount='minima',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'eligendi',
                            'sit',
                            'culpa',
                        ],
                        unit_amount='tempore',
                    ),
                ],
            ),
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'cumque',
                ],
                minimum_amount='consequuntur',
            ),
            model_type=shared.PriceModelType.UNIT,
            name='Calvin Williamson',
            package_config=shared.PricePackageConfig(
                package_amount='blanditiis',
                package_size=5909.84,
            ),
            plan_phase_order=9537.22,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=5578.11,
                        maximum_amount='esse',
                        minimum_amount='quasi',
                        per_unit_maximum='a',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=6216.79,
                        maximum_amount='sint',
                        minimum_amount='pariatur',
                        per_unit_maximum='possimus',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=1576.32,
                        maximum_amount='eveniet',
                        minimum_amount='asperiores',
                        per_unit_maximum='facere',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=850.01,
                        maximum_amount='consequuntur',
                        minimum_amount='quasi',
                        per_unit_maximum='similique',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='aliquid',
                        last_unit='tenetur',
                        unit_amount='quae',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='earum',
                        last_unit='vel',
                        unit_amount='in',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='eius',
                        last_unit='libero',
                        unit_amount='illum',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='soluta',
            ),
        ),
    ],
    product=shared.PlanProduct(
        created_at=dateutil.parser.isoparse('2022-09-10T22:48:07.154Z'),
        id='f1575608-2d68-4ea1-9f1d-17051339d080',
        name='Ms. Duane O'Conner',
    ),
    trial_config=shared.PlanTrialConfig(
        trial_period=324.65,
        trial_period_unit=shared.PlanTrialConfigTrialPeriodUnit.DAYS,
    ),
))

if res.plan is not None:
    # handle response
```

## list

This endpoint returns a list of all [plans](../reference/Orb-API.json/components/schemas/Plan) for an account in a list format. 

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
