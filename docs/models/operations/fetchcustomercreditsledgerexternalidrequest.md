# FetchCustomerCreditsLedgerExternalIDRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `external_customer_id`                                             | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `entry_status`                                                     | [Optional[shared.EntryStatus]](../../models/shared/entrystatus.md) | :heavy_minus_sign:                                                 | Filters to a single status of ledger entry                         |
| `entry_type`                                                       | *Optional[Any]*                                                    | :heavy_minus_sign:                                                 | Filter to a single type of ledger entry                            |
| `minimum_amount`                                                   | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | Filter to ledger entries that affect at least this amount          |