# invoice

## Overview

Actions related to invoice management.

### Available Operations

* [get](#get) - Retrieve an Invoice
* [get_upcoming](#get_upcoming) - Retrieve upcoming invoice
* [list](#list) - List invoices

## get

This endpoint is used to fetch an [`Invoice`](../reference/Orb-API.json/components/schemas/Invoice) given an identifier.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetInvoiceInvoiceIDRequest(
    invoice_id='dolores',
)

res = s.invoice.get(req)

if res.invoice is not None:
    # handle response
```

## get_upcoming

This endpoint can be used to fetch the [`UpcomingInvoice`](../reference/Orb-API.json/components/schemas/Upcoming%20Invoice) for the current billing period given a subscription.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetInvoicesUpcomingRequest(
    subscription_id='minus',
)

res = s.invoice.get_upcoming(req)

if res.upcoming_invoice is not None:
    # handle response
```

## list

This endpoint returns a list of all [`Invoice`](../reference/Orb-API.json/components/schemas/Invoice)s for an account in a list format. 

The list of invoices is ordered starting from the most recently issued invoice date. The response also includes `pagination_metadata`, which lets the caller retrieve the next page of results if they exist.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListInvoicesRequest(
    customer_id='quam',
    external_customer_id='dolor',
    subscription_id='vero',
)

res = s.invoice.list(req)

if res.list_invoices_200_application_json_object is not None:
    # handle response
```
