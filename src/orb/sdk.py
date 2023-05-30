"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .availability import Availability
from .coupon import Coupon
from .credit import Credit
from .credit_note import CreditNote
from .customer import Customer
from .event import Event
from .invoice import Invoice
from .plan import Plan
from .subscription import Subscription
from orb.models import shared

SERVERS = [
    "https://api.withorb.com/v1",
    r"""Production server"""
]
"""Contains the list of servers available to the SDK"""

class Orb:
    r"""Orb powers usage-based billing for the fastest-growing software companies.
    Orb's API is built with the following principles in mind:
    
    1. **Predictable developer experience**: Where applicable, the Orb API uses industry-standard patterns such as cursor-based pagination and standardized error output. To help with debugging in critical API actions, the API always strives to provide detailed and actionable error messages. Aliases such as external customer IDs aid in fast integration times.
    2. **Reliably real time**: Orb's event-based APIs, such as event ingestion are designed to handle extremely high throughput and scale with concurrent load. Orb also provides a real-time event-level credits ledger and a highly performant webhooks architecture.
    3. **Flexibility at the forefront**: Features like timezone localization and the ability to amend historical usage show the flexible nature of the platform.
    """
    availability: Availability
    r"""The Availability resource represents a customer's availability. Availability is created when a customer's invoice is paid, and is updated when a customer's transaction is refunded."""
    coupon: Coupon
    r"""The Coupon resource represents a discount that can be applied to a customer's invoice. Coupons can be applied to a customer's invoice either by the customer or by the Orb API."""
    credit: Credit
    r"""The Credits resource represents a customer's credits. Credits are created when a customer's invoice is paid, and are updated when a customer's transaction is refunded."""
    credit_note: CreditNote
    r"""The Credit Note resource represents a credit note that has been generated for a customer. Credit Notes are generated when a customer's billing interval has elapsed, and are updated when a customer's invoice is paid."""
    customer: Customer
    r"""The Customer resource represents a customer of your service. Customers are created when a customer is created in your service, and are updated when a customer's information is updated in your service."""
    event: Event
    r"""The Event resource represents an event that has been created for a customer. Events are created when a customer's invoice is paid, and are updated when a customer's transaction is refunded."""
    invoice: Invoice
    r"""The Invoice resource represents an invoice that has been generated for a customer. Invoices are generated when a customer's billing interval has elapsed, and are updated when a customer's invoice is paid."""
    plan: Plan
    r"""The Plan resource represents a plan that can be subscribed to by a customer. Plans define the amount of credits that a customer will receive, the price of the plan, and the billing interval."""
    subscription: Subscription
    r"""The Subscription resource represents a customer's subscription to a plan. Subscriptions are created when a customer subscribes to a plan, and are updated when a customer's plan is changed."""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.11.0"
    _gen_version: str = "2.32.7"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.availability = Availability(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.coupon = Coupon(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.credit = Credit(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.credit_note = CreditNote(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.customer = Customer(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.event = Event(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.invoice = Invoice(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.plan = Plan(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.subscription = Subscription(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    