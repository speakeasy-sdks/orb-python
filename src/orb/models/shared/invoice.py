"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import customer_balance_transaction as shared_customer_balance_transaction
from ..shared import customer_tax_id as shared_customer_tax_id
from ..shared import discount as shared_discount
from ..shared import invoice_line_item as shared_invoice_line_item
from ..shared import minimum_amount as shared_minimum_amount
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from orb import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceAutoCollection:
    r"""Information about payment auto-collection for this invoice."""
    
    next_attempt_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_attempt_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If the invoice is scheduled for auto-collection, this field will reflect when the next attempt will occur. If dunning has been exhausted, or auto-collection is not enabled for this invoice, this field will be `null`."""
    previously_attempted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previously_attempted_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If Orb has ever attempted payment auto-collection for this invoice, this field will reflect when that attempt occurred. In conjunction with `next_attempt_at`, this can be used to tell whether the invoice is currently in dunning (that is, `previously_attempted_at` is non-null, and `next_attempt_time` is non-null), or if dunning has been exhausted (`previously_attempted_at` is non-null, but `next_attempt_time` is null)."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceCreditNotes:
    
    credit_note_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_note_number'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    reason: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason'), 'exclude': lambda f: f is None }})
    total: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    voided_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('voided_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceCustomer:
    r"""The customer receiving this invoice."""
    
    external_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    
class InvoiceStatus(str, Enum):
    r"""The status of this invoice as known to Orb. Invoices start in `\\"draft\\"` state for a given billing period, and are automatically transitioned to `\\"issued\\"` when that billing period ends. Invoices will be marked `\\"paid\\"` upon confirmation of successful automatic payment collection by Orb. Invoices may be manually voided; those will be in the terminal `\\"void\\"` state. Invoices synced to an external billing provider (such as Bill.com, QuickBooks, or Stripe Invoicing) will be marked as `\\"synced\\"`."""
    ISSUED = 'issued'
    PAID = 'paid'
    SYNCED = 'synced'
    VOID = 'void'
    DRAFT = 'draft'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceSubscription:
    r"""The associated subscription for this invoice."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Invoice:
    r"""An [`Invoice`](../guides/concepts#invoice) is a fundamental billing entity, representing the request for payment for a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as the result of an action, such as a cancellation."""
    
    amount_due: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_due') }})
    r"""This is the final amount required to be charged to the customer and reflects the application of the customer balance to the `total` of the invoice."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The creation time of the resource in Orb."""
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""An ISO 4217 currency string or `credits`"""
    customer: InvoiceCustomer = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer') }})
    r"""The customer receiving this invoice."""
    customer_balance_transactions: list[shared_customer_balance_transaction.CustomerBalanceTransaction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_balance_transactions') }})
    r"""A list of Customer balance transactions that may be associated with this invoice."""
    discount: shared_discount.Discount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discount') }})
    due_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""When the invoice payment is due."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    invoice_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Issue date of the invoice"""
    invoice_pdf: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_pdf') }})
    r"""The link to download the PDF representation of the `Invoice`."""
    line_items: list[shared_invoice_line_item.InvoiceLineItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line_items') }})
    r"""The breakdown of prices in this invoice."""
    minimum: shared_minimum_amount.MinimumAmount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimum') }})
    status: InvoiceStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of this invoice as known to Orb. Invoices start in `\\"draft\\"` state for a given billing period, and are automatically transitioned to `\\"issued\\"` when that billing period ends. Invoices will be marked `\\"paid\\"` upon confirmation of successful automatic payment collection by Orb. Invoices may be manually voided; those will be in the terminal `\\"void\\"` state. Invoices synced to an external billing provider (such as Bill.com, QuickBooks, or Stripe Invoicing) will be marked as `\\"synced\\"`."""
    subscription: InvoiceSubscription = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription') }})
    r"""The associated subscription for this invoice."""
    subtotal: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtotal') }})
    r"""The total before any discounts and minimums are applied."""
    total: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    r"""The total after any minimums, discounts, and taxes have been applied."""
    auto_collection: Optional[InvoiceAutoCollection] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auto_collection'), 'exclude': lambda f: f is None }})
    r"""Information about payment auto-collection for this invoice."""
    credit_notes: Optional[list[InvoiceCreditNotes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_notes'), 'exclude': lambda f: f is None }})
    r"""A list of credit notes associated with the invoice"""
    customer_tax_id: Optional[shared_customer_tax_id.CustomerTaxID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_tax_id'), 'exclude': lambda f: f is None }})
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
    hosted_invoice_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hosted_invoice_url'), 'exclude': lambda f: f is None }})
    r"""A URL for the invoice portal."""
    issue_failed_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issue_failed_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If the invoice failed to issue, this will be the last time it failed to issue (even if it is now in a different state.)"""
    issued_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issued_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If the invoice has been issued, this will be the time it transitioned to `issued` (even if it is now in a different state.)"""
    memo: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memo'), 'exclude': lambda f: f is None }})
    r"""Free-form text which is available on the invoice PDF and the Orb invoice portal."""
    paid_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paid_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If the invoice has a status of `paid`, this gives a timestamp when the invoice was paid."""
    payment_failed_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_failed_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If payment was attempted on this invoice but failed, this will be the time of the most recent attempt."""
    payment_started_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_started_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If payment was attempted on this invoice, this will be the start time of the most recent attempt. This field is especially useful for delayed-notification payment mechanisms (like bank transfers), where payment can take 3 days or more."""
    scheduled_issue_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduled_issue_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If the invoice is in draft, this timestamp will reflect when the invoice is scheduled to be issued."""
    sync_failed_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync_failed_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If the invoice failed to sync, this will be the last time an external invoicing provider sync was attempted. This field will always be `null` for invoices using Orb Invoicing."""
    voided_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('voided_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""If the invoice has a status of `void`, this gives a timestamp when the invoice was voided."""
    