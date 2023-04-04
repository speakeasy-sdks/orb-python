<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

    
res = s.availability.ping()

if res.get_ping_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->