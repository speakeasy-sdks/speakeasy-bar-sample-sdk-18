"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import error as shared_error
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from the_speakeasy_bar import utils
from typing import Optional


@dataclasses.dataclass
class LoginSecurity:
    password: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic', 'field_name': 'password' }})
    username: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic', 'field_name': 'username' }})
    


class Type(str, Enum):
    API_KEY = 'apiKey'
    JWT = 'JWT'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoginRequestBody:
    type: Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoginResponseBody:
    r"""The api key to use for authenticated endpoints."""
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class LoginResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""An unknown error occurred interacting with the API."""
    object: Optional[LoginResponseBody] = dataclasses.field(default=None)
    r"""The api key to use for authenticated endpoints."""
    

