<!-- Start SDK Example Usage -->
```python
import orb


s = orb.Orb(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.availability.ping()

if res.availability is not None:
    # handle response
```
<!-- End SDK Example Usage -->