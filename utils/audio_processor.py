"""
Audio processing utilities
"""

import base64
from datetime import datetime
from typing import Dict, Any
from fastapi import UploadFile, HTTPException
import aiofiles

from config import MAX_FILE_SIZE, ALLOWED_AUDIO_TYPES

async def process_audio_upload(
    audio_file: UploadFile,
    language_hint: str = None,
    model=None,
    include_audio_data: bool = True
) -> Dict[str, Any]:
    """Process uploaded audio file and return analysis results"""
    
    try:
        # Read file content
        content = await audio_file.read()
        
        # Validate file size
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(400, f"File too large. Maximum size is {MAX_FILE_SIZE/(1024*1024)}MB")
        
        # Validate file type
        if audio_file.content_type not in ALLOWED_AUDIO_TYPES:
            raise HTTPException(400, f"Unsupported audio format. Allowed: {ALLOWED_AUDIO_TYPES}")
        
        # Get file info
        file_size_mb = round(len(content) / (1024 * 1024), 2)
        
        # Perform analysis
        if model:
            language_result = model.detect_language(content, audio_file.filename)
            ai_result = model.detect_ai_vs_human(content, language_hint)
        else:
            # Mock results if no model provided
            language_result = {
                'detected_language': 'en',
                'language_name': 'English',
                'confidence': 85.5,
                'top_3': [
                    {'code': 'en', 'name': 'English', 'prob': 0.855},
                    {'code': 'hi', 'name': 'Hindi', 'prob': 0.095},
                    {'code': 'ta', 'name': 'Tamil', 'prob': 0.050}
                ],
                'audio_features': {'pitch_range': 'medium', 'tempo': 'medium'}
            }
            ai_result = {
                'classification': 'Human',
                'confidence': 92.3,
                'explanation': 'Mock analysis result',
                'risk_level': 'Low',
                'ai_probability': 7.7,
                'human_probability': 92.3,
                'features': {
                    'pitch_consistency': 0.65,
                    'spectral_variance': 0.78,
                    'breath_patterns': 'detected',
                    'background_noise': 'low',
                    'clarity_score': 0.92
                },
                'audio_hash': 'mock12345678',
                'analysis_timestamp': datetime.now().isoformat()
            }
        
        # Combine results
        result = {
            **language_result,
            **ai_result,
            'filename': audio_file.filename,
            'file_size': f"{file_size_mb} MB",
            'upload_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'language_hint': language_hint if language_hint else 'Auto-detected'
        }
        
        # Add audio data URL if requested
        if include_audio_data:
            audio_base64 = base64.b64encode(content).decode('utf-8')
            result['audio_data_url'] = f"data:{audio_file.content_type};base64,{audio_base64}"
        
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Error processing audio: {str(e)}")