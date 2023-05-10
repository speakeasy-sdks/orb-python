# availability

## Overview

Actions related to API availability.

### Available Operations

* [ping](#ping) - Check availability

## ping

This endpoint allows you to test your connection to the Orb API and check the validity of your API key, passed in the `Authorization` header. This is particularly useful for checking that your environment is set up properly, and is a great choice for connectors and integrations.

This API does not have any side-effects or return any Orb resources.

### Example Usage

```python
import orb


s = orb.Orb(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.availability.ping()

if res.get_ping_200_application_json_object is not None:
    # handle response
```
