<!-- Start SDK Example Usage -->
```python
import orb
from orb.models import operations, shared

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.Customer(
    balance="33.00",
    billing_address=shared.BillingAddress(
        city="Laruecester",
        country="US",
        line1="quibusdam",
        line2="unde",
        postal_code="58466-3428",
        state="ipsa",
    ),
    created_at="2022-03-08T10:35:32.561Z",
    currency="suscipit",
    email="Paxton.Schulist@yahoo.com",
    external_customer_id="excepturi",
    id="nisi",
    name="recusandae",
    payment_provider="null",
    payment_provider_id="ab",
    shipping_address=shared.ShippingAddress(
        city="North Lydia",
        country="US",
        line1="perferendis",
        line2="ipsam",
        postal_code="97188-9478",
        state="esse",
    ),
    timezone="America/Los_Angeles",
)
    
res = s.customer.create(req)

if res.customer is not None:
    # handle response
```
<!-- End SDK Example Usage -->