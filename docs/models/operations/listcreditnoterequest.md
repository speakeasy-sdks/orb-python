# ListCreditNoteRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `customer_id`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Filter by a specific customer (cannot be used with `external_customer_id`) |
| `external_customer_id`                                                     | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Filter by a specific customer (cannot be used with `customer_id`)          |
| `subscription_id`                                                          | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Filter by a specific subscription                                          |