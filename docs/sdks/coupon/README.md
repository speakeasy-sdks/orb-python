# coupon

## Overview

The Coupon resource represents a discount that can be applied to a customer's invoice. Coupons can be applied to a customer's invoice either by the customer or by the Orb API.

### Available Operations

* [archive](#archive) - Archive a coupon
* [create](#create) - Create a coupon
* [fetch](#fetch) - Retrieve a coupon
* [list](#list) - List coupons
* [list_subscriptions](#list_subscriptions) - List subscriptions for a coupon

## archive

This endpoint allows a coupon to be archived. Archived coupons can no longer be redeemed, and will be hidden from lists of active coupons. Additionally, once a coupon is archived, its redemption code can be reused for a different coupon.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.coupon.archive('quod')

if res.coupon is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `coupon_id`        | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ArchiveCouponResponse](../../models/operations/archivecouponresponse.md)**


## create

This endpoint allows the creation of coupons, which can then be redeemed at subscription creation or plan change.

### Example Usage

```python
import orb
from orb.models import shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CouponInput(
    discount=shared.Discount(
        amount_discount='quod',
        applies_to_price_ids=[
            'totam',
            'porro',
        ],
        discount_type=shared.DiscountType.PERCENTAGE,
        percentage_discount=0.15,
        trial_amount_discount='dolorum',
        usage_discount=1182.74,
    ),
    duration_in_months=720633,
    id='a928fc81-6742-4cb7-b920-5929396fea75',
    max_redemptions=613064,
    redemption_code='iure',
    times_redeemed=902349,
)

res = s.coupon.create(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.CouponInput](../../models/shared/couponinput.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.CreateCouponResponse](../../models/operations/createcouponresponse.md)**


## fetch

This endpoint retrieves a coupon by its ID. To fetch coupons by their redemption code, use the [List coupons](list-coupons) endpoint with the `redemption_code` parameter.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.coupon.fetch('quidem')

if res.coupon is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `coupon_id`        | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.FetchCouponResponse](../../models/operations/fetchcouponresponse.md)**


## list

This endpoint returns a list of all coupons for an account in a list format. 

The list of coupons is ordered starting from the most recently created coupon. The response also includes [`pagination_metadata`](../api/pagination), which lets the caller retrieve the next page of results if they exist. More information about pagination can be found in the [Pagination-metadata schema](pagination).

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.coupon.list('architecto', False)

if res.coupons is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `redemption_code`                                                                      | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Filter to coupons matching this redemption code.                                       |
| `show_archived`                                                                        | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Show archived coupons as well (by default, this endpoint only returns active coupons). |


### Response

**[operations.ListCouponsResponse](../../models/operations/listcouponsresponse.md)**


## list_subscriptions

This endpoint returns a list of all subscriptions that have redeemed a given coupon as a [paginated](../api/pagination) list, ordered starting from the most recently created subscription. For a full discussion of the subscription resource, see [Subscription](../guides/concepts#subscription).

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.coupon.list_subscriptions('ipsa')

if res.subscriptions is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `coupon_id`        | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ListCouponSubscriptionsResponse](../../models/operations/listcouponsubscriptionsresponse.md)**

