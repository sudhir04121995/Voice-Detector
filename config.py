"""
Configuration and constants
"""

LANGUAGE_DATABASE = {
    'ta': {'name': 'Tamil', 'region': 'South India', 'speakers': '78M'},
    'en': {'name': 'English', 'region': 'Global', 'speakers': '1.5B'},
    'hi': {'name': 'Hindi', 'region': 'North India', 'speakers': '600M'},
    'ml': {'name': 'Malayalam', 'region': 'Kerala', 'speakers': '38M'},
    'te': {'name': 'Telugu', 'region': 'Andhra/Telangana', 'speakers': '82M'},
    'kn': {'name': 'Kannada', 'region': 'Karnataka', 'speakers': '44M'},
    'mr': {'name': 'Marathi', 'region': 'Maharashtra', 'speakers': '83M'},
    'bn': {'name': 'Bengali', 'region': 'West Bengal/Bangladesh', 'speakers': '230M'},
    'gu': {'name': 'Gujarati', 'region': 'Gujarat', 'speakers': '55M'},
    'ur': {'name': 'Urdu', 'region': 'Pakistan/India', 'speakers': '230M'},
}

# Audio characteristics for language detection
AUDIO_FEATURES_BY_LANGUAGE = {
    'ta': {'pitch_range': 'high', 'tempo': 'medium', 'rhythm': 'flowing'},
    'en': {'pitch_range': 'medium', 'tempo': 'medium', 'rhythm': 'stress-timed'},
    'hi': {'pitch_range': 'medium', 'tempo': 'fast', 'rhythm': 'syllable-timed'},
    'ml': {'pitch_range': 'high', 'tempo': 'medium', 'rhythm': 'flowing'},
    'te': {'pitch_range': 'medium', 'tempo': 'medium', 'rhythm': 'syllable-timed'},
}

# File upload configuration
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_AUDIO_TYPES = ['audio/mpeg', 'audio/wav', 'audio/x-wav', 'audio/mp4', 'audio/ogg']