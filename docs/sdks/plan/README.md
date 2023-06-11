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


res = s.plan.fetch('voluptatem')

if res.plan is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `plan_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.FetchPlanResponse](../../models/operations/fetchplanresponse.md)**


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


res = s.plan.get_by_external_id('porro', shared.Plan(
    base_plan=shared.PlanBasePlan(
        external_plan_id='consequuntur',
        id='8909b3fe-49a8-4d9c-bf48-633323f9b77f',
        name='Mr. Lee Funk III',
    ),
    base_plan_id='odio',
    created_at=dateutil.parser.isoparse('2022-02-13T10:24:00.119Z'),
    currency='quidem',
    default_invoice_memo='voluptatibus',
    description='voluptas',
    discount=shared.Discount(
        amount_discount='natus',
        applies_to_price_ids=[
            'atque',
        ],
        discount_type=shared.DiscountType.PERCENTAGE,
        percentage_discount=0.15,
        trial_amount_discount='sit',
        usage_discount=8546.14,
    ),
    external_plan_id='ab',
    id='ba77a89e-bf73-47ae-8203-ce5e6a95d8a0',
    invoicing_currency='at',
    minimum=shared.MinimumAmount(
        applies_to_price_ids=[
            'tempora',
            'vel',
        ],
        minimum_amount='quod',
    ),
    name='Clarence Parisian',
    net_terms=687488,
    plan_phases=[
        shared.PlanPhase(
            description='ipsum',
            discount=shared.Discount(
                amount_discount='quisquam',
                applies_to_price_ids=[
                    'amet',
                    'tempore',
                    'accusamus',
                    'numquam',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='enim',
                usage_discount=2133.12,
            ),
            duration=957451,
            duration_unit=shared.DurationUnit.QUARTERLY,
            minimum=shared.MinimumAmount(
                applies_to_price_ids=[
                    'sit',
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
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='maxime',
                usage_discount=8638.56,
            ),
            duration=747080,
            duration_unit=shared.DurationUnit.MONTHLY,
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
    ],
    prices=[
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='322715bf-0cbb-41e3-9b8b-90f3443a1108',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=9295.3,
                per_unit_maximum='consequatur',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
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
                    shared.PriceBulkBpsConfigTiers(
                        bps=1816.31,
                        maximum_amount='quae',
                        per_unit_maximum='laudantium',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='occaecati',
                        unit_amount='voluptatibus',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='quisquam',
                        unit_amount='vero',
                    ),
                ],
            ),
            cadence=shared.Cadence.MONTHLY,
            created_at=dateutil.parser.isoparse('2022-10-13T06:47:27.001Z'),
            currency='USD',
            discount=shared.Discount(
                amount_discount='delectus',
                applies_to_price_ids=[
                    'consectetur',
                    'vero',
                ],
                discount_type=shared.DiscountType.PERCENTAGE,
                percentage_discount=0.15,
                trial_amount_discount='tenetur',
                usage_discount=4922.68,
            ),
            fixed_price_quantity=9413.78,
            id='bc7abd74-dd39-4c0f-9d2c-ff7c70a45626',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='possimus',
                dimensions=[
                    'ratione',
                    'ex',
                ],
                matrix_values=[
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

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `external_plan_id`                                   | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |
| `plan`                                               | [Optional[shared.Plan]](../../models/shared/plan.md) | :heavy_minus_sign:                                   | N/A                                                  |


### Response

**[operations.FetchPlanExternalIDResponse](../../models/operations/fetchplanexternalidresponse.md)**


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


### Response

**[operations.ListPlansResponse](../../models/operations/listplansresponse.md)**

