<!-- Start SDK Example Usage -->
```python
import orb
import dateutil.parser
from orb.models import shared

s = orb.Orb(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.Customer(
    balance='33.00',
    billing_address=shared.BillingAddress(
        city='Laruecester',
        country='US',
        line1='quibusdam',
        line2='unde',
        postal_code='58466-3428',
        state='ipsa',
    ),
    created_at=dateutil.parser.isoparse('2022-03-08T10:35:32.561Z'),
    currency='suscipit',
    email='Paxton.Schulist@yahoo.com',
    external_customer_id='excepturi',
    id='6ed151a0-5dfc-42dd-b7cc-78ca1ba928fc',
    name='Jack Johns',
    payment_provider=shared.CustomerPaymentProvider.QUICKBOOKS,
    payment_provider_id='impedit',
    shipping_address=shared.ShippingAddress(
        city='Klockoberg',
        country='US',
        line1='excepturi',
        line2='aspernatur',
        postal_code='36162',
        state='natus',
    ),
    timezone='America/Los_Angeles',
)

res = s.customer.create(req)

if res.customer is not None:
    # handle response
```
<!-- End SDK Example Usage -->