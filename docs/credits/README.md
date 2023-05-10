# credits

## Overview

Actions related to credit management.

### Available Operations

* [get](#get) - Add credit ledger entry
* [get_credits](#get_credits) - Retrieve credit balance
* [get_credits_ledger](#get_credits_ledger) - View credits ledger

## get

This endpoint allows you to create a new ledger entry for a specified customer's balance. This can be used to increment balance, deduct credits, and change the expiry date of existing credits.

## Effects of adding a ledger entry
1. After calling this endpoint, [Fetch Credit Balance](../reference/Orb-API.json/paths/~1customers~1{customer_id}~1credits/get) will return a credit block that represents the changes (i.e. balance changes or transfers).
2. A ledger entry will be added to the credits ledger for this customer, and therefore returned in the [View Credits Ledger](../reference/Orb-API.json/paths/~1customers~1{customer_id}~1credits~1ledger/get) response as well as serialized in the response to this request. In the case of deductions without a specified block, multiple ledger entries may be created if the deduction spans credit blocks.


## Adding credits
Adding credits is done by creating an entry of type `increment`. This requires the caller to specify a number of credits as well as an optional expiry date in `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with auditing. When adding credits, the caller can also specify a cost basis per-credit, to indicate how much in USD a customer paid for a single credit in a block. This can later be used for revenue recognition.

The following snippet illustrates a sample request body to increment credits which will expire in January of 2022.

```json
{
  "entry_type": "increment",
  "amount": 100,
  "expiry_date": "2022-12-28",
  "per_unit_cost_basis": "0.20",
  "description": "Purchased 100 credits"
}
```

Note that by default, Orb will always first increment any _negative_ balance in existing blocks before adding the remaining amount to the desired credit block.

## Deducting Credits
Orb allows you to deduct credits from a customer by creating an entry of type `decrement`. Orb matches the algorithm for [Automatic Deductions](Orb-API.json/paths/~1customers~1{customer_id}~1credits~1ledger/get) for determining which credit blocks to decrement from. In the case that the deduction leads to multiple ledger entries, the response from this endpoint will be the final deduction. Orb also optionally allows specifying a description to assist with auditing.

The following snippet illustrates a sample request body to decrement credits.

```json
{
  "entry_type": "decrement",
  "amount": 20,
  "description": "Removing excess credits"
}
```

## Changing credits expiry
If you'd like to change when existing credits expire, you should create a ledger entry of type `expiration_change`. For this entry, the required parameter `expiry_date` identifies the _originating_ block, and the required parameter `target_expiry_date` identifies when the transferred credits should now expire. A new credit block will be created with expiry date `target_expiry_date`, with the same cost basis data as the original credit block, if present.

Note that the balance of the block with the given `expiry_date` must be at least equal to the desired transfer amount determined by the `amount` parameter.

The following snippet illustrates a sample request body to extend the expiration date of credits by one year:

```json
{
  "entry_type": "expiration_change",
  "amount": 10,
  "expiry_date": "2022-12-28",
  "block_id": "UiUhFWeLHPrBY4Ad",
  "target_expiry_date": "2023-12-28",
  "description": "Extending credit validity"
}
```

### Example Usage

```python
import orb
import dateutil.parser
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.credits.get('laboriosam', operations.PostCustomersCustomerIDCreditsLedgerEntryRequestBody(
    amount=9437.49,
    block_id='saepe',
    description='fuga',
    entry_type=operations.PostCustomersCustomerIDCreditsLedgerEntryRequestBodyEntryTypeEnum.DECREMENT,
    expiry_date=dateutil.parser.parse('2023-01-01').date(),
    per_unit_cost_basis='corporis',
    target_expiry_date=dateutil.parser.parse('2023-02-01').date(),
))

if res.credit_ledger_entry is not None:
    # handle response
```

## get_credits

This [paginated endpoint](docs/Pagination.md) can be used to fetch the current state of credit balance for the specified `customer_id`.

Orb keeps track of credit balances in _credit blocks_, where each block is optionally associated with an `expiry_date`. Each time credits are added, a new credit block is created. Credits which do not expire have an `expiry_date` of `null`. To aid in revenue recognition, credit blocks can optionally have a `per_unit_cost_basis`, to indicate how much in USD a customer paid for a single credit in a block.

Orb only returns _unexpired_ credit blocks in this response. For credits that have already expired, you can view this deduction from the customer's balance in the [Credit Ledger](../reference/Orb-API.json/paths/~1customers~1{customer_id}~1credits~1ledger/get) response.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.credits.get_credits('iste')

if res.get_customers_customer_id_credits_200_application_json_object is not None:
    # handle response
```

## get_credits_ledger

The credits ledger provides _auditing_ functionality over Orb's credits system with a list of actions that have taken place to modify a customer's credit balance. This [paginated endpoint](../docs/Pagination.md) lists these entries, starting from the most recent ledger entry.

More details on using Orb's real-time credit feature are [here](../docs/Credits.md).

There are four major types of modifications to credit balance, detailed below.

## Increment
Credits (which optionally expire on a future date) can be added via the API ([Add Ledger Entry](../reference/Orb-API.json/paths/~1customers~1{customer_id}~1credits~1ledger_entry/post)). The ledger entry for such an action will always contain the total eligible starting and ending balance for the customer at the time the entry was added to the ledger. 

## Decrement

Deductions can occur as a result of an API call to create a ledger entry (see [Add Ledger Entry](../reference/Orb-API.json/paths/~1customers~1{customer_id}~1credits~1ledger_entry/post)), or automatically as a result of incurring usage. Both ledger entries present the `decrement` entry type.

As usage for a customer is reported into Orb, credits may be deducted according to the customer's plan configuration. An automated deduction of this type will result in a ledger entry, also with a starting and ending balance. In order to provide better tracing capabilities for automatic deductions, Orb always associates each automatic deduction with the `event_id` at the time of ingestion, used to pinpoint _why_ credit deduction took place and to ensure that credits are never deducted without an associated usage event. 

By default, Orb uses an algorithm that automatically deducts from the *soonest expiring credit block* first in order to ensure that all credits are utilized appropriately. As an example, if trial credits are present for a customer, they will be used before any deduction take place from non-expiring credits. 

It's also possible for a single usage event's deduction to _span_ credit blocks. In this case, Orb will deduct from the next block, ending at the credit block which consists of unexpiring credits. Each of these deductions will lead to a _separate_ ledger entry, one per credit block that is deducted from. By default, the customer's total credit balance in Orb can be negative as a result of a decrement. 

## Expiration change

The expiry of credits can be changed as a result of the API (See [Add Ledger Entry](../reference/Orb-API.json/paths/~1customers~1{customer_id}~1credits~1ledger_entry/post)). This will create a ledger entry that specifies the balance as well as the initial and target expiry dates. 

Note that for this entry type, `starting_balance` will equal `ending_balance`, and the `amount` represents the balance transferred. The credit block linked to the ledger entry is the source credit block from which there was an expiration change.


## Credits expiry

When a set of credits expire on pre-set expiration date, the customer's balance automatically reflects this change and adds an entry to the ledger indicating this event. Note that credit expiry should always happen close to a date boundary in the customer's timezone.

### Example Usage

```python
import orb
from orb.models import operations

s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.credits.get_credits_ledger('iure', operations.GetCustomersCustomerIDCreditsLedgerEntryStatusEnum.PENDING, operations.GetCustomersCustomerIDCreditsLedgerEntryTypeEnum.EXPIRATION_CHANGE, 992.8)

if res.get_customers_customer_id_credits_ledger_200_application_json_object is not None:
    # handle response
```
