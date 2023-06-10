# InvoiceStatus

The status of this invoice as known to Orb. Invoices start in `"draft"` state for a given billing period, and are automatically transitioned to `"issued"` when that billing period ends. Invoices will be marked `"paid"` upon confirmation of successful automatic payment collection by Orb. Invoices may be manually voided; those will be in the terminal `"void"` state. Invoices synced to an external billing provider (such as Bill.com, QuickBooks, or Stripe Invoicing) will be marked as `"synced"`.


## Values

| Name     | Value    |
| -------- | -------- |
| `ISSUED` | issued   |
| `PAID`   | paid     |
| `SYNCED` | synced   |
| `VOID`   | void     |
| `DRAFT`  | draft    |