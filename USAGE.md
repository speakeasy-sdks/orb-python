<!-- Start SDK Example Usage -->
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
        amount_discount='corrupti',
        applies_to_price_ids=[
            'distinctio',
            'quibusdam',
            'unde',
        ],
        discount_type=shared.DiscountType.PERCENTAGE,
        percentage_discount=0.15,
        trial_amount_discount='nulla',
        usage_discount=5448.83,
    ),
    duration_in_months=847252,
    id='69a674e0-f467-4cc8-b96e-d151a05dfc2d',
    max_redemptions=870088,
    redemption_code='maiores',
    times_redeemed=473608,
)

res = s.coupon.create(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->