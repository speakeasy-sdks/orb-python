"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from orb import utils
from orb.models import operations, shared
from typing import Any, Optional

class Invoice:
    r"""The Invoice resource represents an invoice that has been generated for a customer. Invoices are generated when a customer's billing interval has elapsed, and are updated when a customer's invoice is paid."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create(self, request: shared.NewInvoiceLineItem) -> operations.CreateInvoiceLineItemResponse:
        r"""Create invoice line item
        This creates a one-off fixed fee invoice line item on an [Invoice](../guides/concepts#invoice). This can only be done for invoices that are in a `draft` status.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/invoice_line_items'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateInvoiceLineItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InvoiceLineItem])
                res.invoice_line_item = out

        return res

    
    def fetch(self, invoice_id: str) -> operations.FetchInvoiceResponse:
        r"""Retrieve an Invoice
        This endpoint is used to fetch an [`Invoice`](../guides/concepts#invoice) given an identifier.
        """
        request = operations.FetchInvoiceRequest(
            invoice_id=invoice_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.FetchInvoiceRequest, base_url, '/invoices/{invoice_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FetchInvoiceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Invoice])
                res.invoice = out

        return res

    
    def fetch_upcoming(self, subscription_id: str) -> operations.FetchUpcomingInvoiceResponse:
        r"""Retrieve upcoming invoice
        This endpoint can be used to fetch the upcoming [invoice](../guides/concepts#invoice) for the current billing period given a subscription.
        """
        request = operations.FetchUpcomingInvoiceRequest(
            subscription_id=subscription_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/invoices/upcoming'
        headers = {}
        query_params = utils.get_query_params(operations.FetchUpcomingInvoiceRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FetchUpcomingInvoiceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UpcomingInvoice])
                res.upcoming_invoice = out

        return res

    
    def list(self, customer_id: Optional[str] = None, external_customer_id: Optional[str] = None, status: Optional[Any] = None, subscription_id: Optional[str] = None) -> operations.ListInvoicesResponse:
        r"""List invoices
        This endpoint returns a list of all [`Invoice`](../guides/concepts#invoice)s for an account in a list format. 
        
        The list of invoices is ordered starting from the most recently issued invoice date. The response also includes [`pagination_metadata`](../api/pagination), which lets the caller retrieve the next page of results if they exist.
        
        By default, this only returns invoices that are `issued`, `paid`, or `synced`.
        """
        request = operations.ListInvoicesRequest(
            customer_id=customer_id,
            external_customer_id=external_customer_id,
            status=status,
            subscription_id=subscription_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/invoices'
        headers = {}
        query_params = utils.get_query_params(operations.ListInvoicesRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListInvoicesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Invoices])
                res.invoices = out

        return res

    
    def void(self, invoice_id: str) -> operations.PostInvoicesInvoiceIDVoidResponse:
        r"""Void an invoice
        This endpoint allows an invoice's status to be set the `void` status. This can only be done to invoices that are in the `issued` status.
        
        If the associated invoice has used the customer balance to change the amount due, the customer balance operation will be reverted. For example, if the invoice used $10 of customer balance, that amount will be added back to the customer balance upon voiding.
        """
        request = operations.PostInvoicesInvoiceIDVoidRequest(
            invoice_id=invoice_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostInvoicesInvoiceIDVoidRequest, base_url, '/invoices/{invoice_id}/void', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostInvoicesInvoiceIDVoidResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Invoice])
                res.invoice = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostInvoicesInvoiceIDVoid400ApplicationJSON])
                res.post_invoices_invoice_id_void_400_application_json_object = out

        return res

    