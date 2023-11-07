<!-- Start SDK Example Usage -->


```python
import the_speakeasy_bar
from the_speakeasy_bar.models import operations, shared

s = the_speakeasy_bar.TheSpeakeasyBar(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.ListDrinksRequest()

res = s.drinks.list_drinks(req)

if res.classes is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->