# AmendedUsage

OK


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `duplicate`                                                                                        | list[[AmendedUsageDuplicate](../../models/shared/amendedusageduplicate.md)]                        | :heavy_minus_sign:                                                                                 | An array of strings, corresponding to idempotency_key's marked as duplicates (previously ingested) |
| `ingested`                                                                                         | list[*str*]                                                                                        | :heavy_minus_sign:                                                                                 | An array of strings, corresponding to idempotency_key's which were successfully ingested.          |