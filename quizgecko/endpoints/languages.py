
from __future__ import annotations

from typing import Dict, Any, Union, Optional
from ..client import Client

def list_languages(client: Client, *, text: bool = False) -> Union[Dict[str, str], str]:
    """Fetch supported languages. If text=True, returns plain text."""
    params = {'text': 1} if text else None
    return client.request('GET', '/languages', params = params)
