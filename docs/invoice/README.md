# invoice

## Overview

The Invoice resource represents an invoice that has been generated for a customer. Invoices are generated when a customer's billing interval has elapsed, and are updated when a customer's invoice is paid.

### Available Operations

* [create](#create) - Create invoice line item
* [fetch](#fetch) - Retrieve an Invoice
* [fetch_upcoming](#fetch_upcoming) - Retrieve upcoming invoice
* [list](#list) - List invoices
* [void](#void) - Void an invoice

## create

This creates a one-off fixed fee invoice line item on an [Invoice](../guides/concepts#invoice). This can only be done for invoices that are in a `draft` status.

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import shared

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.NewInvoiceLineItem(
    amount='minus',
    end_date=dateutil.parser.parse('2022-10-11').date(),
    invoice_id='4khy3nwzktxv7',
    name='Dean Welch',
    quantity=47hhsws4z2i13,
    start_date=dateutil.parser.parse('2021-10-22').date(),
)

res = s.invoice.create(req)

if res.invoice_line_item is not None:
    # handle response
```

## fetch

This endpoint is used to fetch an [`Invoice`](../guides/concepts#invoice) given an identifier.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.invoice.fetch('voluptatem')

if res.invoice is not None:
    # handle response
```

## fetch_upcoming

This endpoint can be used to fetch the upcoming [invoice](../guides/concepts#invoice) for the current billing period given a subscription.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.invoice.fetch_upcoming('porro')

if res.upcoming_invoice is not None:
    # handle response
```

## list

This endpoint returns a list of all [`Invoice`](../guides/concepts#invoice)s for an account in a list format. 

The list of invoices is ordered starting from the most recently issued invoice date. The response also includes [`pagination_metadata`](../api/pagination), which lets the caller retrieve the next page of results if they exist.

By default, this only returns invoices that are `issued`, `paid`, or `synced`.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.invoice.list('consequuntur', 'blanditiis', 'error', 'eaque')

if res.invoices is not None:
    # handle response
```

## void

This endpoint allows an invoice's status to be set the `void` status. This can only be done to invoices that are in the `issued` status.

If the associated invoice has used the customer balance to change the amount due, the customer balance operation will be reverted. For example, if the invoice used $10 of customer balance, that amount will be added back to the customer balance upon voiding.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.invoice.void('occaecati')

if res.invoice is not None:
    # handle response
```
