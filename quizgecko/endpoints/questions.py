from __future__ import annotations

from typing import Any, Dict, Optional, Union, List
from ..client import Client

def update_question(
    client: Client,
    question_id: Union[int, str],
    *,
    text: Optional[str] = None,
    info: Optional[str] = None,
    answers: Optional[List[Dict[str, Any]]] = None,
    use_generate_path: bool = False
) -> Dict[str, Any]:
    """Update a question and its answers."""
    payload = {}
    if text is not None:
        payload['text'] = text
    if info is not None:
        payload['info'] = info
    if answers is not None:
        payload['answers'] = answers

    path = f'/generate/{question_id}' if use_generate_path else f'/questions/{question_id}'
    return client.request('PUT', path, json = payload)
