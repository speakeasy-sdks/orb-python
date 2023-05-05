"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from orb.models import operations
from typing import Optional

class Availability:
    r"""Actions related to API availability."""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def ping(self) -> operations.GetPingResponse:
        r"""Check availability
        This endpoint allows you to test your connection to the Orb API and check the validity of your API key, passed in the `Authorization` header. This is particularly useful for checking that your environment is set up properly, and is a great choice for connectors and integrations.
        
        This API does not have any side-effects or return any Orb resources.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/ping'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPingResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPing200ApplicationJSON])
                res.get_ping_200_application_json_object = out

        return res

    