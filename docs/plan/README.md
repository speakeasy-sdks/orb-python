# plan

## Overview

Actions related to plan management.

### Available Operations

* [get](#get) - Retrieve a plan
* [get_by_external_id](#get_by_external_id) - Retrieve a plan by external plan ID
* [list](#list) - List plans

## get

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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.plan.get('eaque')

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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.plan.get_by_external_id('quis', shared.Plan(
    base_plan_id='nesciunt',
    created_at=dateutil.parser.isoparse('2022-12-25T05:44:55.720Z'),
    currency='dolores',
    description='minus',
    discount={
        "dolor": 'vero',
        "nostrum": 'hic',
    },
    external_plan_id='recusandae',
    id='9b90c289-09b3-4fe4-9a8d-9cbf48633323',
    invoicing_currency='hic',
    minimum={
        "cum": 'voluptate',
        "dignissimos": 'reiciendis',
        "amet": 'dolorum',
    },
    name='Ms. Christine Beer',
    plan_phases=[
        shared.PlanPhase(
            description='accusamus',
            discount={
                "voluptatibus": 'voluptas',
                "natus": 'eos',
                "atque": 'sit',
            },
            duration=854614,
            duration_unit=shared.PlanPhaseDurationUnit.MONTHLY,
            minimum={
                "dolorum": 'iusto',
                "voluptate": 'dolorum',
                "deleniti": 'omnis',
            },
            name='Kelvin Zboncak',
            order=456015,
        ),
        shared.PlanPhase(
            description='id',
            discount={
                "eius": 'aspernatur',
                "perferendis": 'amet',
                "optio": 'accusamus',
                "ad": 'saepe',
            },
            duration=383464,
            duration_unit=shared.PlanPhaseDurationUnit.QUARTERLY,
            minimum={
                "minima": 'repellendus',
                "totam": 'similique',
                "alias": 'at',
            },
            name='Rhonda Kautzer',
            order=185636,
        ),
    ],
    prices=[
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='f7a73cf3-be45-43f8-b0b3-26b5a73429cd',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=7470.8,
                per_unit_maximum='dicta',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=5173.79,
                        maximum_amount='incidunt',
                        per_unit_maximum='aspernatur',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=1749.09,
                        maximum_amount='distinctio',
                        per_unit_maximum='facilis',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=3960.6,
                        maximum_amount='quam',
                        per_unit_maximum='molestias',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='qui',
                        unit_amount='neque',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='fugit',
                        unit_amount='magni',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='odio',
                        unit_amount='sunt',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='ullam',
                        unit_amount='nam',
                    ),
                ],
            ),
            cadence=shared.PriceCadence.QUARTERLY,
            created_at=dateutil.parser.isoparse('2022-03-27T15:45:02.604Z'),
            currency='USD',
            discount={
                "nobis": 'et',
                "saepe": 'ipsum',
                "veritatis": 'nobis',
            },
            fixed_price_quantity=5521.93,
            id='b90f3443-a110-48e0-adcf-4b921879fce9',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='quis',
                dimensions=[
                    'delectus',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'vero',
                        ],
                        unit_amount='tenetur',
                    ),
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'hic',
                            'distinctio',
                        ],
                        unit_amount='quod',
                    ),
                ],
            ),
            minimum={
                "similique": 'facilis',
                "vero": 'ducimus',
            },
            model_type=shared.PriceModelType.BULK,
            name='Gilberto Dickinson',
            package_config=shared.PricePackageConfig(
                package_amount='aut',
                package_size=9742.59,
            ),
            plan_phase_order=3472.33,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=1481.41,
                        maximum_amount='porro',
                        minimum_amount='maiores',
                        per_unit_maximum='doloribus',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=4783.7,
                        maximum_amount='eligendi',
                        minimum_amount='ducimus',
                        per_unit_maximum='alias',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=6394.73,
                        maximum_amount='tempora',
                        minimum_amount='ipsam',
                        per_unit_maximum='ea',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=1369,
                        maximum_amount='vel',
                        minimum_amount='possimus',
                        per_unit_maximum='magnam',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='ex',
                        last_unit='laudantium',
                        unit_amount='dicta',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='dolor',
            ),
        ),
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='f16d9f5f-ce6c-4556-946c-3e250fb008c4',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=1469.46,
                per_unit_maximum='accusamus',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=2506.22,
                        maximum_amount='et',
                        per_unit_maximum='dolorum',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='placeat',
                        unit_amount='velit',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='eum',
                        unit_amount='autem',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='nobis',
                        unit_amount='quas',
                    ),
                ],
            ),
            cadence=shared.PriceCadence.QUARTERLY,
            created_at=dateutil.parser.isoparse('2021-11-11T22:59:32.230Z'),
            currency='USD',
            discount={
                "quasi": 'tempora',
                "numquam": 'explicabo',
                "provident": 'ipsa',
            },
            fixed_price_quantity=4764.77,
            id='474778a7-bd46-46d2-8c10-ab3cdca42519',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='consequatur',
                dimensions=[
                    'debitis',
                    'ipsam',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'quo',
                        ],
                        unit_amount='esse',
                    ),
                ],
            ),
            minimum={
                "aperiam": 'distinctio',
                "quod": 'dignissimos',
                "inventore": 'nihil',
                "totam": 'accusamus',
            },
            model_type=shared.PriceModelType.BULK,
            name='Violet Johns',
            package_config=shared.PricePackageConfig(
                package_amount='deserunt',
                package_size=4752.89,
            ),
            plan_phase_order=353.62,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=4304.02,
                        maximum_amount='quas',
                        minimum_amount='praesentium',
                        per_unit_maximum='consequuntur',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=5361.78,
                        maximum_amount='fugit',
                        minimum_amount='fuga',
                        per_unit_maximum='mollitia',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=2775.96,
                        maximum_amount='atque',
                        minimum_amount='explicabo',
                        per_unit_maximum='minima',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=3926.76,
                        maximum_amount='fugit',
                        minimum_amount='sapiente',
                        per_unit_maximum='consequuntur',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='explicabo',
                        last_unit='saepe',
                        unit_amount='occaecati',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='atque',
            ),
        ),
        shared.Price(
            billable_metric=shared.PriceBillableMetric(
                id='17ee17cb-e61e-46b7-b95b-c0ab3c20c4f3',
            ),
            bps_config=shared.PriceBpsConfig(
                bps=4581.39,
                per_unit_maximum='blanditiis',
            ),
            bulk_bps_config=shared.PriceBulkBpsConfig(
                tiers=[
                    shared.PriceBulkBpsConfigTiers(
                        bps=9537.22,
                        maximum_amount='nulla',
                        per_unit_maximum='quas',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=4572.23,
                        maximum_amount='quasi',
                        per_unit_maximum='a',
                    ),
                    shared.PriceBulkBpsConfigTiers(
                        bps=6216.79,
                        maximum_amount='sint',
                        per_unit_maximum='pariatur',
                    ),
                ],
            ),
            bulk_config=shared.PriceBulkConfig(
                tiers=[
                    shared.PriceBulkConfigTiers(
                        maximum_units='quia',
                        unit_amount='eveniet',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='asperiores',
                        unit_amount='facere',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='veritatis',
                        unit_amount='consequuntur',
                    ),
                    shared.PriceBulkConfigTiers(
                        maximum_units='quasi',
                        unit_amount='similique',
                    ),
                ],
            ),
            cadence=shared.PriceCadence.MONTHLY,
            created_at=dateutil.parser.isoparse('2022-01-19T12:09:14.633Z'),
            currency='USD',
            discount={
                "earum": 'vel',
            },
            fixed_price_quantity=4473.78,
            id='4bdb04f1-5756-4082-968e-a19f1d170513',
            matrix_config=shared.PriceMatrixConfig(
                default_unit_amount='adipisci',
                dimensions=[
                    'temporibus',
                    'accusantium',
                    'rem',
                ],
                matrix_values=[
                    shared.PriceMatrixConfigMatrixValues(
                        dimension_values=[
                            'eum',
                            'mollitia',
                            'ab',
                        ],
                        unit_amount='corrupti',
                    ),
                ],
            ),
            minimum={
                "voluptatem": 'dolor',
                "occaecati": 'numquam',
            },
            model_type=shared.PriceModelType.BULK_BPS,
            name='Loretta Anderson DVM',
            package_config=shared.PricePackageConfig(
                package_amount='natus',
                package_size=2446.51,
            ),
            plan_phase_order=9742.57,
            tiered_bps_config=shared.PriceTieredBpsConfig(
                tiers=[
                    shared.PriceTieredBpsConfigTiers(
                        bps=9903.45,
                        maximum_amount='aperiam',
                        minimum_amount='ea',
                        per_unit_maximum='quaerat',
                    ),
                    shared.PriceTieredBpsConfigTiers(
                        bps=1629.54,
                        maximum_amount='repellendus',
                        minimum_amount='officia',
                        per_unit_maximum='maxime',
                    ),
                ],
            ),
            tiered_config=shared.PriceTieredConfig(
                tiers=[
                    shared.PriceTieredConfigTiers(
                        first_unit='officia',
                        last_unit='asperiores',
                        unit_amount='nemo',
                    ),
                    shared.PriceTieredConfigTiers(
                        first_unit='quae',
                        last_unit='quaerat',
                        unit_amount='porro',
                    ),
                ],
            ),
            unit_config=shared.PriceUnitConfig(
                unit_amount='quod',
            ),
        ),
    ],
    product=shared.PlanProduct(
        created_at=dateutil.parser.isoparse('2022-12-06T06:52:56.510Z'),
        id='3aa63aae-8d67-4864-9bb6-75fd5e60b375',
        name='Carroll Gerhold',
    ),
    trial_config=shared.PlanTrialConfig(
        trial_period=9689.72,
        trial_period_unit=shared.PlanTrialConfigTrialPeriodUnit.DAYS,
    ),
))

if res.status_code == 200:
    # handle response
```

## list

This endpoint returns a list of all [plans](../reference/Orb-API.json/components/schemas/Plan) for an account in a list format. 

The list of plans is ordered starting from the most recently created plan. The response also includes [`pagination_metadata`](../reference/Orb-API.json/components/schemas/Pagination-metadata), which lets the caller retrieve the next page of results if they exist. More information about pagination can be found in the [Pagination-metadata schema](../reference/Orb-API.json/components/schemas/Pagination-metadata).


### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListPlansRequestBody(
    data=[
        shared.Plan(
            base_plan_id='saepe',
            created_at=dateutil.parser.isoparse('2022-02-10T06:30:04.103Z'),
            currency='sunt',
            description='asperiores',
            discount={
                "non": 'amet',
            },
            external_plan_id='beatae',
            id='7fe35b60-eb1e-4a42-a555-ba3c28744ed5',
            invoicing_currency='adipisci',
            minimum={
                "blanditiis": 'quas',
                "hic": 'nesciunt',
                "culpa": 'corrupti',
            },
            name='Jimmie Weimann',
            plan_phases=[
                shared.PlanPhase(
                    description='rerum',
                    discount={
                        "reiciendis": 'explicabo',
                    },
                    duration=994401,
                    duration_unit=shared.PlanPhaseDurationUnit.ANNUAL,
                    minimum={
                        "expedita": 'ab',
                        "iste": 'dolore',
                    },
                    name='Aaron King',
                    order=131289,
                ),
            ],
            prices=[
                shared.Price(
                    billable_metric=shared.PriceBillableMetric(
                        id='916fe1f0-8f42-494e-b698-f447f603e8b4',
                    ),
                    bps_config=shared.PriceBpsConfig(
                        bps=2777.73,
                        per_unit_maximum='ipsam',
                    ),
                    bulk_bps_config=shared.PriceBulkBpsConfig(
                        tiers=[
                            shared.PriceBulkBpsConfigTiers(
                                bps=5249.7,
                                maximum_amount='sit',
                                per_unit_maximum='nobis',
                            ),
                            shared.PriceBulkBpsConfigTiers(
                                bps=6256.37,
                                maximum_amount='veniam',
                                per_unit_maximum='minima',
                            ),
                            shared.PriceBulkBpsConfigTiers(
                                bps=9241.59,
                                maximum_amount='reiciendis',
                                per_unit_maximum='nulla',
                            ),
                            shared.PriceBulkBpsConfigTiers(
                                bps=1685.76,
                                maximum_amount='aperiam',
                                per_unit_maximum='saepe',
                            ),
                        ],
                    ),
                    bulk_config=shared.PriceBulkConfig(
                        tiers=[
                            shared.PriceBulkConfigTiers(
                                maximum_units='veniam',
                                unit_amount='in',
                            ),
                            shared.PriceBulkConfigTiers(
                                maximum_units='officiis',
                                unit_amount='beatae',
                            ),
                        ],
                    ),
                    cadence=shared.PriceCadence.MONTHLY,
                    created_at=dateutil.parser.isoparse('2022-06-28T14:53:26.431Z'),
                    currency='USD',
                    discount={
                        "laboriosam": 'dolorum',
                        "voluptatum": 'error',
                        "hic": 'expedita',
                    },
                    fixed_price_quantity=8928.63,
                    id='3a5aa8e4-824d-40ab-8075-088e51862065',
                    matrix_config=shared.PriceMatrixConfig(
                        default_unit_amount='saepe',
                        dimensions=[
                            'consequatur',
                            'incidunt',
                            'reiciendis',
                        ],
                        matrix_values=[
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'dicta',
                                    'architecto',
                                    'occaecati',
                                ],
                                unit_amount='labore',
                            ),
                        ],
                    ),
                    minimum={
                        "atque": 'laborum',
                        "nam": 'tenetur',
                        "laboriosam": 'alias',
                    },
                    model_type=shared.PriceModelType.TIERED,
                    name='Karl Miller',
                    package_config=shared.PricePackageConfig(
                        package_amount='repellendus',
                        package_size=9627.71,
                    ),
                    plan_phase_order=9147.91,
                    tiered_bps_config=shared.PriceTieredBpsConfig(
                        tiers=[
                            shared.PriceTieredBpsConfigTiers(
                                bps=6672.85,
                                maximum_amount='quidem',
                                minimum_amount='reprehenderit',
                                per_unit_maximum='facere',
                            ),
                        ],
                    ),
                    tiered_config=shared.PriceTieredConfig(
                        tiers=[
                            shared.PriceTieredConfigTiers(
                                first_unit='praesentium',
                                last_unit='mollitia',
                                unit_amount='veniam',
                            ),
                            shared.PriceTieredConfigTiers(
                                first_unit='voluptatem',
                                last_unit='quisquam',
                                unit_amount='repudiandae',
                            ),
                            shared.PriceTieredConfigTiers(
                                first_unit='quasi',
                                last_unit='atque',
                                unit_amount='reprehenderit',
                            ),
                        ],
                    ),
                    unit_config=shared.PriceUnitConfig(
                        unit_amount='asperiores',
                    ),
                ),
                shared.Price(
                    billable_metric=shared.PriceBillableMetric(
                        id='86bc173d-689e-4ee9-926f-8d986e881ead',
                    ),
                    bps_config=shared.PriceBpsConfig(
                        bps=2871.19,
                        per_unit_maximum='reiciendis',
                    ),
                    bulk_bps_config=shared.PriceBulkBpsConfig(
                        tiers=[
                            shared.PriceBulkBpsConfigTiers(
                                bps=9197.83,
                                maximum_amount='dicta',
                                per_unit_maximum='accusantium',
                            ),
                        ],
                    ),
                    bulk_config=shared.PriceBulkConfig(
                        tiers=[
                            shared.PriceBulkConfigTiers(
                                maximum_units='dolores',
                                unit_amount='enim',
                            ),
                        ],
                    ),
                    cadence=shared.PriceCadence.MONTHLY,
                    created_at=dateutil.parser.isoparse('2022-01-18T11:13:47.798Z'),
                    currency='USD',
                    discount={
                        "magnam": 'saepe',
                        "consequuntur": 'occaecati',
                        "officiis": 'perspiciatis',
                    },
                    fixed_price_quantity=4463.94,
                    id='3e922a57-a15b-4e3e-8608-07e2b6e3ab88',
                    matrix_config=shared.PriceMatrixConfig(
                        default_unit_amount='aliquam',
                        dimensions=[
                            'repellat',
                            'alias',
                        ],
                        matrix_values=[
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'nihil',
                                    'mollitia',
                                    'voluptas',
                                ],
                                unit_amount='alias',
                            ),
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'reiciendis',
                                    'dolores',
                                    'id',
                                    'minima',
                                ],
                                unit_amount='dolore',
                            ),
                        ],
                    ),
                    minimum={
                        "nesciunt": 'quae',
                        "recusandae": 'omnis',
                        "quaerat": 'molestiae',
                    },
                    model_type=shared.PriceModelType.PACKAGE,
                    name='Molly Ferry',
                    package_config=shared.PricePackageConfig(
                        package_amount='eum',
                        package_size=3679.27,
                    ),
                    plan_phase_order=9282.19,
                    tiered_bps_config=shared.PriceTieredBpsConfig(
                        tiers=[
                            shared.PriceTieredBpsConfigTiers(
                                bps=5920.81,
                                maximum_amount='quis',
                                minimum_amount='eum',
                                per_unit_maximum='reiciendis',
                            ),
                            shared.PriceTieredBpsConfigTiers(
                                bps=5927.8,
                                maximum_amount='aspernatur',
                                minimum_amount='ullam',
                                per_unit_maximum='quasi',
                            ),
                        ],
                    ),
                    tiered_config=shared.PriceTieredConfig(
                        tiers=[
                            shared.PriceTieredConfigTiers(
                                first_unit='nostrum',
                                last_unit='mollitia',
                                unit_amount='provident',
                            ),
                            shared.PriceTieredConfigTiers(
                                first_unit='possimus',
                                last_unit='animi',
                                unit_amount='ex',
                            ),
                            shared.PriceTieredConfigTiers(
                                first_unit='aliquid',
                                last_unit='accusantium',
                                unit_amount='repellat',
                            ),
                        ],
                    ),
                    unit_config=shared.PriceUnitConfig(
                        unit_amount='doloribus',
                    ),
                ),
            ],
            product=shared.PlanProduct(
                created_at=dateutil.parser.isoparse('2022-07-21T10:16:07.152Z'),
                id='bfaad4f9-efc1-4b45-92c1-032648dc2f61',
                name='Teresa McCullough',
            ),
            trial_config=shared.PlanTrialConfig(
                trial_period=7453.98,
                trial_period_unit=shared.PlanTrialConfigTrialPeriodUnit.DAYS,
            ),
        ),
        shared.Plan(
            base_plan_id='hic',
            created_at=dateutil.parser.isoparse('2022-11-04T12:05:06.853Z'),
            currency='earum',
            description='perspiciatis',
            discount={
                "debitis": 'aliquid',
                "porro": 'suscipit',
                "dolorem": 'fugit',
                "cumque": 'fuga',
            },
            external_plan_id='ratione',
            id='aed01179-9631-42fd-a047-71778ff61d01',
            invoicing_currency='odio',
            minimum={
                "esse": 'ex',
                "consectetur": 'aliquid',
            },
            name='Janie Casper',
            plan_phases=[
                shared.PlanPhase(
                    description='aliquid',
                    discount={
                        "suscipit": 'aliquid',
                        "perferendis": 'eum',
                        "voluptas": 'iste',
                    },
                    duration=661607,
                    duration_unit=shared.PlanPhaseDurationUnit.MONTHLY,
                    minimum={
                        "possimus": 'voluptates',
                        "mollitia": 'laborum',
                        "libero": 'ad',
                    },
                    name='Bill Brown',
                    order=775803,
                ),
                shared.PlanPhase(
                    description='ex',
                    discount={
                        "ad": 'expedita',
                        "voluptatem": 'molestias',
                    },
                    duration=737254,
                    duration_unit=shared.PlanPhaseDurationUnit.QUARTERLY,
                    minimum={
                        "voluptatum": 'omnis',
                    },
                    name='Olivia O'Reilly DVM',
                    order=889288,
                ),
                shared.PlanPhase(
                    description='architecto',
                    discount={
                        "pariatur": 'debitis',
                        "voluptatem": 'alias',
                        "deleniti": 'earum',
                    },
                    duration=404244,
                    duration_unit=shared.PlanPhaseDurationUnit.ANNUAL,
                    minimum={
                        "minus": 'nemo',
                        "asperiores": 'ratione',
                        "ullam": 'perferendis',
                    },
                    name='Jimmie Russel',
                    order=373216,
                ),
            ],
            prices=[
                shared.Price(
                    billable_metric=shared.PriceBillableMetric(
                        id='34181430-1042-4181-bd52-08ece7e253b6',
                    ),
                    bps_config=shared.PriceBpsConfig(
                        bps=4269.43,
                        per_unit_maximum='voluptatum',
                    ),
                    bulk_bps_config=shared.PriceBulkBpsConfig(
                        tiers=[
                            shared.PriceBulkBpsConfigTiers(
                                bps=3494.4,
                                maximum_amount='ab',
                                per_unit_maximum='porro',
                            ),
                            shared.PriceBulkBpsConfigTiers(
                                bps=4218.44,
                                maximum_amount='nobis',
                                per_unit_maximum='laboriosam',
                            ),
                        ],
                    ),
                    bulk_config=shared.PriceBulkConfig(
                        tiers=[
                            shared.PriceBulkConfigTiers(
                                maximum_units='consequuntur',
                                unit_amount='voluptatem',
                            ),
                            shared.PriceBulkConfigTiers(
                                maximum_units='exercitationem',
                                unit_amount='necessitatibus',
                            ),
                            shared.PriceBulkConfigTiers(
                                maximum_units='quasi',
                                unit_amount='nisi',
                            ),
                            shared.PriceBulkConfigTiers(
                                maximum_units='at',
                                unit_amount='vero',
                            ),
                        ],
                    ),
                    cadence=shared.PriceCadence.QUARTERLY,
                    created_at=dateutil.parser.isoparse('2022-08-13T07:34:51.264Z'),
                    currency='USD',
                    discount={
                        "repudiandae": 'optio',
                        "occaecati": 'nemo',
                        "voluptate": 'blanditiis',
                        "officia": 'voluptas',
                    },
                    fixed_price_quantity=2540.25,
                    id='584273a8-418d-4162-b09f-b0929921aefb',
                    matrix_config=shared.PriceMatrixConfig(
                        default_unit_amount='omnis',
                        dimensions=[
                            'minima',
                            'praesentium',
                            'maxime',
                            'magnam',
                        ],
                        matrix_values=[
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'commodi',
                                    'itaque',
                                    'commodi',
                                ],
                                unit_amount='totam',
                            ),
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'modi',
                                    'nam',
                                    'vero',
                                    'voluptatem',
                                ],
                                unit_amount='ipsam',
                            ),
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'alias',
                                    'quasi',
                                ],
                                unit_amount='non',
                            ),
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'enim',
                                    'sint',
                                    'nulla',
                                    'deserunt',
                                ],
                                unit_amount='esse',
                            ),
                        ],
                    ),
                    minimum={
                        "reprehenderit": 'est',
                        "quis": 'sint',
                    },
                    model_type=shared.PriceModelType.MATRIX,
                    name='Irvin Tromp',
                    package_config=shared.PricePackageConfig(
                        package_amount='voluptas',
                        package_size=8953.46,
                    ),
                    plan_phase_order=9661.48,
                    tiered_bps_config=shared.PriceTieredBpsConfig(
                        tiers=[
                            shared.PriceTieredBpsConfigTiers(
                                bps=7918.8,
                                maximum_amount='fuga',
                                minimum_amount='laborum',
                                per_unit_maximum='consectetur',
                            ),
                        ],
                    ),
                    tiered_config=shared.PriceTieredConfig(
                        tiers=[
                            shared.PriceTieredConfigTiers(
                                first_unit='atque',
                                last_unit='ipsum',
                                unit_amount='impedit',
                            ),
                        ],
                    ),
                    unit_config=shared.PriceUnitConfig(
                        unit_amount='magni',
                    ),
                ),
                shared.Price(
                    billable_metric=shared.PriceBillableMetric(
                        id='beb47737-3c8d-472f-a4d1-db1f2c431066',
                    ),
                    bps_config=shared.PriceBpsConfig(
                        bps=1076.17,
                        per_unit_maximum='vero',
                    ),
                    bulk_bps_config=shared.PriceBulkBpsConfig(
                        tiers=[
                            shared.PriceBulkBpsConfigTiers(
                                bps=4319.94,
                                maximum_amount='velit',
                                per_unit_maximum='ut',
                            ),
                            shared.PriceBulkBpsConfigTiers(
                                bps=5964.33,
                                maximum_amount='earum',
                                per_unit_maximum='dicta',
                            ),
                            shared.PriceBulkBpsConfigTiers(
                                bps=7722.66,
                                maximum_amount='voluptatibus',
                                per_unit_maximum='iste',
                            ),
                        ],
                    ),
                    bulk_config=shared.PriceBulkConfig(
                        tiers=[
                            shared.PriceBulkConfigTiers(
                                maximum_units='alias',
                                unit_amount='nisi',
                            ),
                            shared.PriceBulkConfigTiers(
                                maximum_units='itaque',
                                unit_amount='velit',
                            ),
                            shared.PriceBulkConfigTiers(
                                maximum_units='laborum',
                                unit_amount='non',
                            ),
                            shared.PriceBulkConfigTiers(
                                maximum_units='dolor',
                                unit_amount='iusto',
                            ),
                        ],
                    ),
                    cadence=shared.PriceCadence.ANNUAL,
                    created_at=dateutil.parser.isoparse('2022-12-29T06:34:38.165Z'),
                    currency='USD',
                    discount={
                        "recusandae": 'ea',
                        "quidem": 'voluptas',
                        "facilis": 'placeat',
                    },
                    fixed_price_quantity=5960.65,
                    id='b8f759ea-c55a-4974-9d31-1352965bb8a7',
                    matrix_config=shared.PriceMatrixConfig(
                        default_unit_amount='fugit',
                        dimensions=[
                            'magni',
                        ],
                        matrix_values=[
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'quae',
                                ],
                                unit_amount='modi',
                            ),
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'exercitationem',
                                ],
                                unit_amount='itaque',
                            ),
                        ],
                    ),
                    minimum={
                        "ipsum": 'unde',
                    },
                    model_type=shared.PriceModelType.BULK_BPS,
                    name='Wilbert Crona',
                    package_config=shared.PricePackageConfig(
                        package_amount='omnis',
                        package_size=7272.5,
                    ),
                    plan_phase_order=1156.61,
                    tiered_bps_config=shared.PriceTieredBpsConfig(
                        tiers=[
                            shared.PriceTieredBpsConfigTiers(
                                bps=7278.88,
                                maximum_amount='fugiat',
                                minimum_amount='officia',
                                per_unit_maximum='quos',
                            ),
                            shared.PriceTieredBpsConfigTiers(
                                bps=8119.39,
                                maximum_amount='sit',
                                minimum_amount='iusto',
                                per_unit_maximum='ipsa',
                            ),
                            shared.PriceTieredBpsConfigTiers(
                                bps=9148.64,
                                maximum_amount='inventore',
                                minimum_amount='aperiam',
                                per_unit_maximum='totam',
                            ),
                        ],
                    ),
                    tiered_config=shared.PriceTieredConfig(
                        tiers=[
                            shared.PriceTieredConfigTiers(
                                first_unit='eligendi',
                                last_unit='distinctio',
                                unit_amount='voluptatem',
                            ),
                            shared.PriceTieredConfigTiers(
                                first_unit='autem',
                                last_unit='esse',
                                unit_amount='dolores',
                            ),
                        ],
                    ),
                    unit_config=shared.PriceUnitConfig(
                        unit_amount='assumenda',
                    ),
                ),
                shared.Price(
                    billable_metric=shared.PriceBillableMetric(
                        id='1ad879ee-b966-45b8-9efb-d02bae0be2d7',
                    ),
                    bps_config=shared.PriceBpsConfig(
                        bps=5101.28,
                        per_unit_maximum='odit',
                    ),
                    bulk_bps_config=shared.PriceBulkBpsConfig(
                        tiers=[
                            shared.PriceBulkBpsConfigTiers(
                                bps=3589.95,
                                maximum_amount='error',
                                per_unit_maximum='earum',
                            ),
                        ],
                    ),
                    bulk_config=shared.PriceBulkConfig(
                        tiers=[
                            shared.PriceBulkConfigTiers(
                                maximum_units='recusandae',
                                unit_amount='similique',
                            ),
                        ],
                    ),
                    cadence=shared.PriceCadence.ANNUAL,
                    created_at=dateutil.parser.isoparse('2022-04-28T01:39:49.849Z'),
                    currency='USD',
                    discount={
                        "unde": 'molestiae',
                    },
                    fixed_price_quantity=9631.98,
                    id='92443da7-ce52-4b89-9c53-7c6454efb0b3',
                    matrix_config=shared.PriceMatrixConfig(
                        default_unit_amount='labore',
                        dimensions=[
                            'occaecati',
                            'voluptas',
                            'quo',
                        ],
                        matrix_values=[
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'fuga',
                                    'nostrum',
                                    'est',
                                    'impedit',
                                ],
                                unit_amount='delectus',
                            ),
                        ],
                    ),
                    minimum={
                        "vero": 'odit',
                        "repellat": 'pariatur',
                        "nemo": 'reprehenderit',
                    },
                    model_type=shared.PriceModelType.UNIT,
                    name='Cathy Kirlin',
                    package_config=shared.PricePackageConfig(
                        package_amount='dolores',
                        package_size=6211.69,
                    ),
                    plan_phase_order=850.76,
                    tiered_bps_config=shared.PriceTieredBpsConfig(
                        tiers=[
                            shared.PriceTieredBpsConfigTiers(
                                bps=4527.29,
                                maximum_amount='pariatur',
                                minimum_amount='itaque',
                                per_unit_maximum='similique',
                            ),
                            shared.PriceTieredBpsConfigTiers(
                                bps=7631.65,
                                maximum_amount='ex',
                                minimum_amount='quaerat',
                                per_unit_maximum='commodi',
                            ),
                        ],
                    ),
                    tiered_config=shared.PriceTieredConfig(
                        tiers=[
                            shared.PriceTieredConfigTiers(
                                first_unit='placeat',
                                last_unit='quidem',
                                unit_amount='exercitationem',
                            ),
                            shared.PriceTieredConfigTiers(
                                first_unit='quam',
                                last_unit='dolorem',
                                unit_amount='modi',
                            ),
                            shared.PriceTieredConfigTiers(
                                first_unit='ipsa',
                                last_unit='sint',
                                unit_amount='vero',
                            ),
                            shared.PriceTieredConfigTiers(
                                first_unit='sequi',
                                last_unit='repudiandae',
                                unit_amount='cum',
                            ),
                        ],
                    ),
                    unit_config=shared.PriceUnitConfig(
                        unit_amount='dicta',
                    ),
                ),
            ],
            product=shared.PlanProduct(
                created_at=dateutil.parser.isoparse('2021-12-30T18:01:47.888Z'),
                id='a2b12eb0-7f11-46db-9954-5fc95fa88970',
                name='Jack Luettgen',
            ),
            trial_config=shared.PlanTrialConfig(
                trial_period=7316.34,
                trial_period_unit=shared.PlanTrialConfigTrialPeriodUnit.DAYS,
            ),
        ),
        shared.Plan(
            base_plan_id='libero',
            created_at=dateutil.parser.isoparse('2022-12-17T22:14:17.851Z'),
            currency='delectus',
            description='impedit',
            discount={
                "ipsum": 'adipisci',
                "saepe": 'deserunt',
                "doloremque": 'quis',
            },
            external_plan_id='veniam',
            id='b197cd44-e2f5-42d8-ad35-13bb6f48b656',
            invoicing_currency='libero',
            minimum={
                "facere": 'facilis',
                "ipsum": 'ad',
                "voluptatibus": 'voluptatibus',
                "consequuntur": 'debitis',
            },
            name='Susie Davis',
            plan_phases=[
                shared.PlanPhase(
                    description='iusto',
                    discount={
                        "rem": 'eligendi',
                        "fugiat": 'unde',
                        "officiis": 'ducimus',
                    },
                    duration=220104,
                    duration_unit=shared.PlanPhaseDurationUnit.MONTHLY,
                    minimum={
                        "porro": 'vitae',
                        "dignissimos": 'esse',
                        "fugiat": 'ad',
                    },
                    name='Jill Wintheiser',
                    order=729828,
                ),
            ],
            prices=[
                shared.Price(
                    billable_metric=shared.PriceBillableMetric(
                        id='14eeb52f-f785-4fc3-b814-d4c98e0c2bb8',
                    ),
                    bps_config=shared.PriceBpsConfig(
                        bps=5908.58,
                        per_unit_maximum='repudiandae',
                    ),
                    bulk_bps_config=shared.PriceBulkBpsConfig(
                        tiers=[
                            shared.PriceBulkBpsConfigTiers(
                                bps=4923.61,
                                maximum_amount='corporis',
                                per_unit_maximum='vero',
                            ),
                            shared.PriceBulkBpsConfigTiers(
                                bps=6293.77,
                                maximum_amount='repellendus',
                                per_unit_maximum='iure',
                            ),
                            shared.PriceBulkBpsConfigTiers(
                                bps=2138.35,
                                maximum_amount='commodi',
                                per_unit_maximum='impedit',
                            ),
                        ],
                    ),
                    bulk_config=shared.PriceBulkConfig(
                        tiers=[
                            shared.PriceBulkConfigTiers(
                                maximum_units='aut',
                                unit_amount='voluptatem',
                            ),
                            shared.PriceBulkConfigTiers(
                                maximum_units='ad',
                                unit_amount='quae',
                            ),
                        ],
                    ),
                    cadence=shared.PriceCadence.ANNUAL,
                    created_at=dateutil.parser.isoparse('2021-06-24T23:38:28.956Z'),
                    currency='USD',
                    discount={
                        "cum": 'amet',
                        "quasi": 'dicta',
                        "laudantium": 'doloremque',
                    },
                    fixed_price_quantity=9384.12,
                    id='739ae9e0-57eb-4809-a281-0331f3981d4c',
                    matrix_config=shared.PriceMatrixConfig(
                        default_unit_amount='esse',
                        dimensions=[
                            'perferendis',
                        ],
                        matrix_values=[
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'aperiam',
                                    'dignissimos',
                                ],
                                unit_amount='repellat',
                            ),
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'porro',
                                ],
                                unit_amount='provident',
                            ),
                            shared.PriceMatrixConfigMatrixValues(
                                dimension_values=[
                                    'eligendi',
                                ],
                                unit_amount='dignissimos',
                            ),
                        ],
                    ),
                    minimum={
                        "soluta": 'natus',
                    },
                    model_type=shared.PriceModelType.BULK_BPS,
                    name='Marvin White',
                    package_config=shared.PricePackageConfig(
                        package_amount='itaque',
                        package_size=8483.46,
                    ),
                    plan_phase_order=6707.62,
                    tiered_bps_config=shared.PriceTieredBpsConfig(
                        tiers=[
                            shared.PriceTieredBpsConfigTiers(
                                bps=8762.85,
                                maximum_amount='qui',
                                minimum_amount='consectetur',
                                per_unit_maximum='repellat',
                            ),
                            shared.PriceTieredBpsConfigTiers(
                                bps=1286.96,
                                maximum_amount='explicabo',
                                minimum_amount='exercitationem',
                                per_unit_maximum='nihil',
                            ),
                        ],
                    ),
                    tiered_config=shared.PriceTieredConfig(
                        tiers=[
                            shared.PriceTieredConfigTiers(
                                first_unit='ab',
                                last_unit='illo',
                                unit_amount='hic',
                            ),
                            shared.PriceTieredConfigTiers(
                                first_unit='deserunt',
                                last_unit='delectus',
                                unit_amount='non',
                            ),
                        ],
                    ),
                    unit_config=shared.PriceUnitConfig(
                        unit_amount='distinctio',
                    ),
                ),
            ],
            product=shared.PlanProduct(
                created_at=dateutil.parser.isoparse('2022-08-26T06:03:44.896Z'),
                id='44e472e8-0285-47a5-b404-63a7d575f140',
                name='Olive Kub',
            ),
            trial_config=shared.PlanTrialConfig(
                trial_period=6770.45,
                trial_period_unit=shared.PlanTrialConfigTrialPeriodUnit.DAYS,
            ),
        ),
    ],
    pagination_metadata={
        "voluptate": 'consectetur',
        "nesciunt": 'quaerat',
        "itaque": 'minus',
        "sunt": 'distinctio',
    },
)

res = s.plan.list(req)

if res.status_code == 200:
    # handle response
```
