# ListCouponsRequest


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `redemption_code`                                                                      | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Filter to coupons matching this redemption code.                                       |
| `show_archived`                                                                        | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Show archived coupons as well (by default, this endpoint only returns active coupons). |