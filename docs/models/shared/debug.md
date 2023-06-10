# Debug

Optional debug information (only present when debug=true is passed to the endpoint). Contains ingested and duplicate event idempotency keys.


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `duplicate`        | list[*str*]        | :heavy_minus_sign: | N/A                |
| `ingested`         | list[*str*]        | :heavy_minus_sign: | N/A                |