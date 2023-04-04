"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Invoice:
    r"""Actions related to invoice management."""
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
        
    def get(self, request: operations.GetInvoiceInvoiceIDRequest) -> operations.GetInvoiceInvoiceIDResponse:
        r"""Retrieve an Invoice
        This endpoint is used to fetch an [`Invoice`](../reference/Orb-API.json/components/schemas/Invoice) given an identifier.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetInvoiceInvoiceIDRequest, base_url, '/invoices/{invoice_id}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetInvoiceInvoiceIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Invoice])
                res.invoice = out

        return res

    def get_upcoming(self, request: operations.GetInvoicesUpcomingRequest) -> operations.GetInvoicesUpcomingResponse:
        r"""Retrieve upcoming invoice
        This endpoint can be used to fetch the [`UpcomingInvoice`](../reference/Orb-API.json/components/schemas/Upcoming%20Invoice) for the current billing period given a subscription.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/invoices/upcoming'
        
        query_params = utils.get_query_params(operations.GetInvoicesUpcomingRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetInvoicesUpcomingResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UpcomingInvoice])
                res.upcoming_invoice = out

        return res

    def list(self, request: operations.ListInvoicesRequest) -> operations.ListInvoicesResponse:
        r"""List invoices
        This endpoint returns a list of all [`Invoice`](../reference/Orb-API.json/components/schemas/Invoice)s for an account in a list format. 
        
        The list of invoices is ordered starting from the most recently issued invoice date. The response also includes `pagination_metadata`, which lets the caller retrieve the next page of results if they exist.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/invoices'
        
        query_params = utils.get_query_params(operations.ListInvoicesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListInvoicesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListInvoices200ApplicationJSON])
                res.list_invoices_200_application_json_object = out

        return res

    