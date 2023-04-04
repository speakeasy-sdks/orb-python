<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PostCustomersRequestBody(
    billing_address=operations.PostCustomersRequestBodyBillingAddress(
        city="Laruecester",
        country="US",
        line1="quibusdam",
        line2="unde",
        postal_code="58466-3428",
        state="ipsa",
    ),
    currency="delectus",
    email="Geraldine_Kreiger52@gmail.com",
    external_customer_id="iusto",
    name="excepturi",
    payment_provider="bill.com",
    payment_provider_id="recusandae",
    shipping_address=operations.PostCustomersRequestBodyShippingAddress(
        city="Belleville",
        country="US",
        line1="quis",
        line2="veritatis",
        postal_code="03897-1889",
        state="molestiae",
    ),
    timezone="Etc/UTC",
)
    
res = s.customer.create(req)

if res.customer is not None:
    # handle response
```
<!-- End SDK Example Usage -->