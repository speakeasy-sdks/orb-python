"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class EntryType(str, Enum):
    r"""Filter to a single type of ledger entry"""
    INCREMENT = 'increment'
    DECREMENT = 'decrement'
    EXPIRATION_CHANGE = 'expiration_change'
    CREDIT_BLOCK_EXPIRY = 'credit_block_expiry'