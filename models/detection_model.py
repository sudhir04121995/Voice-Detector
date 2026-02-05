"""
Detection model for AI voice detection and language identification
"""

import random
import hashlib
from datetime import datetime
from typing import Dict, Any
from config import LANGUAGE_DATABASE, AUDIO_FEATURES_BY_LANGUAGE

class DetectionModel:
    """Mock detection model with language identification"""
    
    def __init__(self):
        self.languages = LANGUAGE_DATABASE
    
    def detect_language(self, audio_data: bytes, filename: str) -> Dict[str, Any]:
        """
        Simulated language detection based on audio characteristics
        """
        # Generate deterministic "fingerprint" from audio
        audio_hash = hashlib.md5(audio_data).hexdigest()
        random.seed(int(audio_hash[:8], 16))
        
        # Simulate language probabilities
        candidates = list(self.languages.keys())
        probabilities = {}
        
        for lang in candidates:
            # Base probability + hash-based variation
            base_prob = 0.1 + (ord(audio_hash[0]) % 90) / 100
            variation = random.uniform(-0.05, 0.05)
            probabilities[lang] = max(0.01, min(0.99, base_prob + variation))
        
        # Normalize probabilities
        total = sum(probabilities.values())
        for lang in probabilities:
            probabilities[lang] = round(probabilities[lang] / total, 3)
        
        # Get top 3 languages
        sorted_langs = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
        detected_lang = sorted_langs[0][0]
        
        return {
            'detected_language': detected_lang,
            'language_name': self.languages[detected_lang]['name'],
            'confidence': round(probabilities[detected_lang] * 100, 1),
            'all_probabilities': probabilities,
            'top_3': [{'code': k, 'name': self.languages[k]['name'], 'prob': v} 
                     for k, v in sorted_langs[:3]],
            'audio_features': AUDIO_FEATURES_BY_LANGUAGE.get(detected_lang, {})
        }
    
    def detect_ai_vs_human(self, audio_data: bytes, language: str = None) -> Dict[str, Any]:
        """
        Detect if audio is AI-generated or human
        """
        # Generate deterministic result from audio hash
        audio_hash = hashlib.md5(audio_data).hexdigest()
        random.seed(int(audio_hash[:8], 16))
        
        # Determine AI probability based on hash
        hash_int = int(audio_hash[:4], 16)
        ai_probability = (hash_int % 100) / 100
        
        # Add some randomness for realistic results
        ai_probability = ai_probability * 0.8 + random.uniform(0, 0.2)
        ai_probability = max(0.05, min(0.95, ai_probability))
        
        if ai_probability > 0.7:
            classification = "AI-generated"
            confidence = ai_probability
            explanation = (
                f"This audio shows strong patterns consistent with AI-generated speech. "
                f"The voice has unusual consistency in pitch and timing."
            )
            risk_level = "High"
        elif ai_probability > 0.55:
            classification = "Likely AI-generated"
            confidence = ai_probability
            explanation = (
                f"This audio exhibits several characteristics of synthetic speech. "
                f"Some unnatural patterns detected in spectral features."
            )
            risk_level = "Medium"
        elif ai_probability > 0.45:
            classification = "Likely Human"
            confidence = 1 - ai_probability
            explanation = (
                f"This audio appears to be human speech with some unusual characteristics. "
                f"Most features match natural human voice patterns."
            )
            risk_level = "Low"
        else:
            classification = "Human"
            confidence = 1 - ai_probability
            explanation = (
                f"This audio shows natural human speech characteristics. "
                f"Breath patterns, pitch variation, and spectral features match organic speech."
            )
            risk_level = "Very Low"
        
        # Generate feature analysis
        features = {
            'pitch_consistency': round(random.uniform(0.3, 0.9), 2),
            'spectral_variance': round(random.uniform(0.2, 0.95), 2),
            'breath_patterns': 'detected' if classification == 'Human' else 'minimal',
            'background_noise': random.choice(['low', 'medium', 'high']),
            'clarity_score': round(random.uniform(0.5, 0.98), 2)
        }
        
        return {
            'classification': classification,
            'confidence': round(confidence * 100, 1),
            'explanation': explanation,
            'risk_level': risk_level,
            'ai_probability': round(ai_probability * 100, 1),
            'human_probability': round((1 - ai_probability) * 100, 1),
            'features': features,
            'audio_hash': audio_hash[:12],
            'analysis_timestamp': datetime.now().isoformat()
        }