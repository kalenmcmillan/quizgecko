from __future__ import annotations

import time
from typing import Any, Dict, Optional, List, Union
from ..client import Client
from ..errors import APIError

def create_quiz(
    client: Client,
    *,
    text: Optional[str] = None,
    url: Optional[str] = None,
    question_type: str = 'auto',
    number_of_questions: Optional[int] = None,
    difficulty: str = 'easy',
    language: str = 'en',
    upload_ids: Optional[List[int]] = None,
    import_mode: bool = False,
    subtopics: Optional[List[str]] = None,
    custom_instructions: Optional[str] = None
) -> Dict[str, Any]:
    """Start a quiz generation job."""
    payload = {
        'text': text,
        'url': url,
        'question_type': question_type,
        'number_of_questions': number_of_questions,
        'difficulty': difficulty,
        'language': language,
        'upload_ids': upload_ids or [],
        'import_mode': import_mode,
        'subtopics': subtopics or [],
        'custom_instructions': custom_instructions
    }
    return client.request('POST', '/generate', json = payload)

def wait_for_completion(
    client: Client,
    quiz_id: Union[int, str],
    *,
    poll_seconds: int = 2,
    timeout_seconds: int = 180
) -> Dict[str, Any]:
    """Poll until quiz.status == 'completed' or timeout."""
    deadline = time.time() + timeout_seconds
    while True:
        quiz = client.request('GET', f'/quiz/{quiz_id}')
        status = str(quiz.get('status', '')).lower()
        if status == 'completed':
            return quiz
        if time.time() > deadline:
            raise APIError('Timeout while waiting for quiz to complete', 408)
        
        time.sleep(poll_seconds)
