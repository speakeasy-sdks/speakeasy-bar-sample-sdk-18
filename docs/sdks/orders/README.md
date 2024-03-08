# Orders
(*orders*)

## Overview

The orders endpoints.

### Available Operations

* [create_order](#create_order) - Create an order.

## create_order

Create an order for a drink.

### Example Usage

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

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateOrderRequest](../../models/operations/createorderrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
