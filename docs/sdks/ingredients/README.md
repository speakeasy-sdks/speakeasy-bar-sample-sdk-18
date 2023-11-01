# Ingredients
(*ingredients*)

## Overview

The ingredients endpoints.

### Available Operations

* [list_ingredients](#list_ingredients) - Get a list of ingredients.

## list_ingredients

Get a list of ingredients, if authenticated this will include stock levels and product codes otherwise it will only include public information.

### Example Usage

```python
import the_speakeasy_bar
from the_speakeasy_bar.models import operations, shared

s = the_speakeasy_bar.TheSpeakeasyBar(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.ListIngredientsRequest(
    ingredients=[
        'string',
    ],
)

res = s.ingredients.list_ingredients(req)

if res.ingredients is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListIngredientsRequest](../../models/operations/listingredientsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListIngredientsResponse](../../models/operations/listingredientsresponse.md)**

