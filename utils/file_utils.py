"""
File utility functions
"""

import os
from typing import Optional
import aiofiles

async def save_uploaded_file(content: bytes, filename: str) -> str:
    """Save uploaded file to temporary location"""
    temp_path = f"uploads/temp_{os.urandom(8).hex()}_{filename}"
    
    async with aiofiles.open(temp_path, 'wb') as f:
        await f.write(content)
    
    return temp_path

def cleanup_temp_file(file_path: str) -> None:
    """Clean up temporary file"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except:
        pass