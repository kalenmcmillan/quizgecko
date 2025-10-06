from __future__ import annotations

from typing import Any, Dict, Generator, Optional, Union
from ..client import Client

def get_quiz(client: Client, quiz_id: Union[int, str]) -> Dict[str, Any]:
    """Fetch a quiz by ID."""
    return client.request('GET', f'/quiz/{quiz_id}')

def list_quizzes(client: Client, *, page: int = 1) -> Dict[str, Any]:
    """Return one page of quizzes."""
    return client.request('GET', '/quiz', params = {'page': page})

def iterate_quizzes(client: Client, *, start_page: int = 1) -> Generator[Dict[str, Any], None, None]:
    """Yield quizzes across pages until empty."""
    page = start_page
    while True:
        batch = list_quizzes(client, page = page)
        items = batch.get('data') or batch.get('quizzes') or []
        for item in items:
            yield item

        next_page = batch.get('next_page') or batch.get('next')
        if next_page:
            try:
                page = int(next_page)
            except Exception:
                page = page + 1
            continue
        if not items:
            break
        
        page = page + 1

def update_quiz(
    client: Client,
    quiz_id: Union[int, str],
    *,
    title: Optional[str] = None,
    description: Optional[str] = None
) -> Dict[str, Any]:
    """Update a quiz title or description."""
    payload = {}
    if title is not None:
        payload['title'] = title
    if description is not None:
        payload['description'] = description

    return client.request('PUT', f'/quiz/{quiz_id}', json = payload)
