from __future__ import annotations

import os
from typing import Any, Dict, Optional, IO
from ..client import Client
from ..errors import APIError

def upload_file_path(client: Client, file_path: str) -> Dict[str, Any]:
    """Upload a file from a local path."""
    if not file_path:
        raise APIError('A file path is required', 400)
    
    with open(file_path, 'rb') as file:
        files = {'file': (os.path.basename(file_path), file)}
        return client.request('POST', '/file/upload', files = files)

def upload_file_obj(client: Client, file_obj: IO[bytes], filename: str = 'upload.bin') -> Dict[str, Any]:
    """Upload a file from a file-like object."""
    if not file_obj:
        raise APIError('A file object is required', 400)
    
    files = {'file': (filename, file_obj)}
    return client.request('POST', '/file/upload', files = files)
