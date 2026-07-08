%%writefile core/config.py
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class ILRTConfig:
    """Global configuration for the Infinity Loop Red Teaming framework."""
    
    # Target Model Settings (The system being tested)
    target_api_key: Optional[str] = None
    target_model_name: str = "gemini-1.5-pro-latest" 
    
    # Brain Model Settings (The attacker)
    hf_token: Optional[str] = None
    brain_model_name: str = "cognitivecomputations/dolphin-2.9-llama3-8b"
    
    # Loop & Strategy Settings
    max_turns: int = 5
    temperature: float = 0.7
    
    # Storage Paths
    output_dir: str = "outputs"
    
    def __post_init__(self):
        """Automatically create the output directory if it doesn't exist."""
        os.makedirs(self.output_dir, exist_ok=True)
