"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import drink as shared_drink
from ...models.shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GetDrinkRequest:
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetDrinkResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    drink: Optional[shared_drink.Drink] = dataclasses.field(default=None)
    r"""A drink."""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""An unknown error occurred interacting with the API."""
    

