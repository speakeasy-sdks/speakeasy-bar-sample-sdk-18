# Drinks
(*drinks*)

## Overview

The drinks endpoints.

### Available Operations

* [get_drink](#get_drink) - Get a drink.
* [list_drinks](#list_drinks) - Get a list of drinks.

## get_drink

Get a drink by name, if authenticated this will include stock levels and product codes otherwise it will only include public information.

### Example Usage

```python
import the_speakeasy_bar
from the_speakeasy_bar.models import operations, shared

s = the_speakeasy_bar.TheSpeakeasyBar(
    security=shared.Security(
        api_key="<YOUR_API_KEY>",
    ),
)

req = operations.GetDrinkRequest(
    name='<value>',
)

res = s.drinks.get_drink(req)

if res.drink is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetDrinkRequest](../../models/operations/getdrinkrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetDrinkResponse](../../models/operations/getdrinkresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## list_drinks

Get a list of drinks, if authenticated this will include stock levels and product codes otherwise it will only include public information.

### Example Usage

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

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListDrinksRequest](../../models/operations/listdrinksrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `server_url`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | An optional server URL to use.                                               |


### Response

**[operations.ListDrinksResponse](../../models/operations/listdrinksresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
