<!-- Start SDK Example Usage [usage] -->
### Sign in

First you need to send an authentication request to the API by providing your username and password.
In the request body, you should specify the type of token you would like to receive: API key or JSON Web Token.
If your credentials are valid, you will receive a token in the response object: `res.object.token: str`.

```python
import the_speakeasy_bar
from the_speakeasy_bar.models import operations

s = the_speakeasy_bar.TheSpeakeasyBar()

req = operations.LoginRequestBody(
    type=operations.Type.API_KEY,
)

res = s.authentication.login(req, operations.LoginSecurity(
    password="<PASSWORD>",
    username="<USERNAME>",
))

if res.object is not None:
    # handle response
    pass

```

### Browse available drinks

Once you are authenticated, you can use the token you received for all other authenticated endpoints.
For example, you can filter the list of available drinks by type.

```python
import the_speakeasy_bar
from the_speakeasy_bar.models import operations, shared

s = the_speakeasy_bar.TheSpeakeasyBar(
    security=shared.Security(
        api_key="<YOUR_API_KEY>",
    ),
)

req = operations.ListDrinksRequest()

res = s.drinks.list_drinks(req)

if res.classes is not None:
    # handle response
    pass

```

### Create an order

When you submit an order, you can include a callback URL along your request.
This URL will get called whenever the supplier updates the status of your order.

```python
import the_speakeasy_bar
from the_speakeasy_bar.models import operations, shared

s = the_speakeasy_bar.TheSpeakeasyBar(
    security=shared.Security(
        api_key="<YOUR_API_KEY>",
    ),
)

req = operations.CreateOrderRequest(
    request_body=[
        shared.OrderInput(
            product_code='APM-1F2D3',
            quantity=26535,
            type=shared.OrderType.DRINK,
        ),
    ],
)

res = s.orders.create_order(req)

if res.order is not None:
    # handle response
    pass

```

### Subscribe to webhooks to receive stock updates

```python
import the_speakeasy_bar
from the_speakeasy_bar.models import operations, shared

s = the_speakeasy_bar.TheSpeakeasyBar(
    security=shared.Security(
        api_key="<YOUR_API_KEY>",
    ),
)

req = [
    operations.RequestBody(),
]

res = s.config.subscribe_to_webhooks(req)

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->