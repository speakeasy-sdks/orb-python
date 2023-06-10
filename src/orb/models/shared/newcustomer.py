"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import billing_address as shared_billing_address
from ..shared import customer_tax_id as shared_customer_tax_id
from ..shared import paymentprovider as shared_paymentprovider
from ..shared import shipping_address as shared_shipping_address
from dataclasses_json import Undefined, dataclass_json
from orb import utils
from typing import Optional



@dataclasses.dataclass
class NewCustomerMetadata:
    r"""User-specified key value pairs, often useful for referencing internal resources or IDs. Returned as-is in the customer resource."""
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class NewCustomer:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""A valid customer email, to be used for invoicing and notifications."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The full name of the customer"""
    auto_collection: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auto_collection'), 'exclude': lambda f: f is None }})
    r"""Used to determine if invoices for this customer will automatically attempt to charge a saved payment method, if available. This parameter defaults to `True` when a payment provider is provided on customer creation."""
    billing_address: Optional[shared_billing_address.BillingAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    r"""The customer's billing address; all fields in the address are optional. This address appears on customer invoices."""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""An ISO 4217 currency string used for the customer's invoices and balance. If not set at creation time, will be set at subscription creation time."""
    external_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id'), 'exclude': lambda f: f is None }})
    r"""An optional user-defined ID for this customer resource, used throughout the system as an alias for this Customer. Use this field to identify a customer by an existing identifier in your system."""
    metadata: Optional[NewCustomerMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""User-specified key value pairs, often useful for referencing internal resources or IDs. Returned as-is in the customer resource."""
    payment_provider: Optional[shared_paymentprovider.PaymentProvider] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_provider'), 'exclude': lambda f: f is None }})
    r"""This is used for creating charges or invoices in an external system via Orb. When not in test mode:
    - the connection must first be configured in the Orb webapp. 
    - if the provider is an invoicing provider (`stripe_invoice`, `quickbooks`, `bill.com`), any product mappings must first be configured with the Orb team.
    """
    payment_provider_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_provider_id'), 'exclude': lambda f: f is None }})
    r"""The ID of this customer in an external payments solution, such as Stripe. This is used for creating charges or invoices in the external system via Orb."""
    shipping_address: Optional[shared_shipping_address.ShippingAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_address'), 'exclude': lambda f: f is None }})
    r"""The customer's shipping address; all fields in the address are optional. Note that downstream tax calculations are based on the shipping address."""
    tax_id: Optional[shared_customer_tax_id.CustomerTaxID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_id'), 'exclude': lambda f: f is None }})
    r"""Tax IDs are commonly required to be displayed on customer invoices, which are added to the headers of invoices.
    
    
    ### Supported Tax ID Countries and Types
    
    
    | Country        | Type         | Description                                 |
    |----------------|--------------|---------------------------------------------|
    | Australia      | `au_abn`     | Australian Business Number (AU ABN)	        |
    | Australia      | `au_arn`     | Australian Taxation Office Reference Number |
    | Austria        | `eu_vat`     | European VAT number                         |
    | Belgium        | `eu_vat`     | European VAT number                         |
    | Brazil         | `br_cnpj`    | Brazilian CNPJ number                       |
    | Brazil         | `br_cpf`     | Brazilian CPF number	                       |
    | Bulgaria       | `bg_uic`     | Bulgaria Unified Identification Code        |
    | Bulgaria       | `eu_vat`     | European VAT number                         |
    | Canada         | `ca_bn`      | Canadian BN                                 |
    | Canada         | `ca_gst_hst` | Canadian GST/HST number                     |
    | Canada         | `ca_pst_bc`  | Canadian PST number (British Columbia)      |
    | Canada         | `ca_pst_mb`  | Canadian PST number (Manitoba)              |
    | Canada         | `ca_pst_sk`  | Canadian PST number (Saskatchewan)          |
    | Canada         | `ca_qst`     | Canadian QST number (Québec)                |
    | Chile          | `cl_tin`     | Chilean TIN                                 |
    | Croatia        | `eu_vat`     | European VAT number                         |
    | Cyprus         | `eu_vat`     | European VAT number                         |
    | Czech Republic | `eu_vat`     | European VAT number                         |
    | Denmark        | `eu_vat`     | European VAT number                         |
    | Egypt          | `eg_tin`     | Egyptian Tax Identification Number	         |
    | Estonia   | `eu_vat`     | European VAT number   |                                                                             
    | EU        | `eu_oss_vat` | European One Stop Shop VAT number for non-Union scheme                                                   |
    | Finland   | `eu_vat`     | European VAT number                                                                                      |
    | France    | `eu_vat`     | European VAT number                                                                                      |
    | Georgia   | `ge_vat`     | Georgian VAT                                                                                             |
    | Germany   | `eu_vat`     | European VAT number                                                                                      |
    | Greece    | `eu_vat`     | European VAT number                                                                                      |
    | Hong Kong | `hk_br`      | Hong Kong BR number                                                                                      |
    | Hungary   | `eu_vat`     | European VAT number                                                                                      |
    | Hungary   | `hu_tin`     | Hungary tax number (adószám)	                                                                            |
    | Iceland   | `is_vat`     | Icelandic VAT                                                                                            |
    | India     | `in_gst`     | Indian GST number                                                                                        |
    | Indonesia | `id_npwp`    | Indonesian NPWP number                                                                                   |
    | Ireland   | `eu_vat`     | European VAT number                                                                                      |
    | Israel    | `il_vat`     | Israel VAT                                                                                               |
    | Italy     | `eu_vat`     | European VAT number                                                                                      |
    | Japan     | `jp_cn`      | Japanese Corporate Number (*Hōjin Bangō*)                                                                |
    | Japan     | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (*Tōroku Kokugai Jigyōsha no Tōroku Bangō*)	 |
    | Japan     | `jp_trn`     | Japanese Tax Registration Number (*Tōroku Bangō*)	                                                       |
    | Kenya     | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                   |
    | Latvia    | `eu_vat`     | European VAT number                                                                                  |
    | Liechtenstein | `li_uid`  | Liechtensteinian UID number           |
    | Lithuania     | `eu_vat`  | European VAT number	                  |
    | Luxembourg    | `eu_vat`  | European VAT number	                  |
    | Malaysia      | `my_frp`  | Malaysian FRP number                  |
    | Malaysia      | `my_itn`  | Malaysian ITN                         |
    | Malaysia      | `my_sst`  | Malaysian SST number                  |
    | Malta         | `eu_vat ` | European VAT number                   |
    | Mexico        | `mx_rfc`  | Mexican RFC number                    |
    | Netherlands   | `eu_vat`  | European VAT number	                  |
    | New Zealand   | `nz_gst`  | New Zealand GST number	               |
    | Norway        | `no_vat`  | Norwegian VAT number                  |
    | Philippines   | `ph_tin	` | Philippines Tax Identification Number |
    | Poland        | `eu_vat`  | European VAT number                   |
    | Portugal      | `eu_vat`  | European VAT number                   |
    | Romania       | `eu_vat`  | European VAT number                   |
    | Russia        | `ru_inn`  | Russian INN                           |
    | Russia        | `ru_kpp`  | Russian KPP                           |
    | Saudi Arabia  | `sg_gst`  | Singaporean GST                       |
    | Singapore     | `sg_uen`  | Singaporean UEN	                      |
    | Slovakia      | `eu_vat`  | European VAT number                   |
    | Slovenia      | `eu_vat`  | European VAT number                   |
    | Slovenia             | `si_tin` | Slovenia tax number (davčna številka)	             |
    | South Africa	        | `za_vat` | South African VAT number                           |
    | South Korea          | `kr_brn` | Korean BRN                                         |
    | Spain                | `es_cif` | Spanish NIF number (previously Spanish CIF number) |
    | Spain                | `eu_vat` | European VAT number	                               |
    | Sweden               | `eu_vat` | European VAT number                                |
    | Switzerland          | `ch_vat` | Switzerland VAT number	                            |
    | Taiwan               | `tw_vat` | Taiwanese VAT	                                     |
    | Thailand             | `th_vat` | Thai VAT                                           |
    | Turkey               | `tr_tin` | Turkish Tax Identification Number                  |
    | Ukraine              | `ua_vat` | Ukrainian VAT                                      |
    | United Arab Emirates | `ae_trn` | United Arab Emirates TRN	                          |
    | United Kingdom       | `eu_vat` | Northern Ireland VAT number                        |
    | United Kingdom       | `gb_vat` | United Kingdom VAT number                          |
    | United States        | `us_ein` | United States EIN                                  |
    """
    timezone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone'), 'exclude': lambda f: f is None }})
    r"""A timezone identifier from the IANA timezone database, such as \\"America/Los_Angeles\\". This defaults to your account's timezone if not set. This cannot be changed after customer creation."""
    

