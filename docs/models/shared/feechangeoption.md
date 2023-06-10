# FeeChangeOption

Determines when the change takes effect. Note that if `effective_date` is specified, this defautls to `effective_date`. Otherwise, this defaults to `immediate` unless it's explicitly set to `upcoming_invoice.


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `IMMEDIATE`        | immediate          |
| `UPCOMING_INVOICE` | upcoming_invoice   |
| `EFFECTIVE_DATE`   | effective_date     |