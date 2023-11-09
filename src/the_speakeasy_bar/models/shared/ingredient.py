"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .ingredienttype import IngredientType
from dataclasses_json import Undefined, dataclass_json
from the_speakeasy_bar import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Ingredient:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the ingredient."""
    type: IngredientType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of ingredient."""
    product_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productCode'), 'exclude': lambda f: f is None }})
    r"""The product code of the ingredient, only available when authenticated."""
    stock: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stock'), 'exclude': lambda f: f is None }})
    r"""The number of units of the ingredient in stock, only available when authenticated."""
    

