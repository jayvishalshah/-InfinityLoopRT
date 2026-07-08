from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class Target(ABC):
    """Interface for the system being red-teamed (e.g., Gemini)."""
    
    @abstractmethod
    def send_prompt(self, prompt: str) -> str:
        """Sends a prompt to the target and returns the text response."""
        pass

class Brain(ABC):
    """Interface for the attacker/red-team model (e.g., Dolphin 3)."""
    
    @abstractmethod
    def generate_attack(self, target_info: str, context: Dict[str, Any]) -> str:
        """Generates the next prompt to test against the target."""
        pass

class Evaluator(ABC):
    """Interface for evaluating if an attack succeeded or failed."""
    
    @abstractmethod
    def evaluate(self, prompt: str, response: str) -> Dict[str, Any]:
        """Analyzes the response and returns a score/flag dictionary."""
        pass
        
class Memory(ABC):
    """Interface for tracking the history of the red-team session."""
    
    @abstractmethod
    def add_interaction(self, prompt: str, response: str, evaluation: Dict[str, Any]) -> None:
        """Stores a single turn of the conversation."""
        pass
        
    @abstractmethod
    def get_context(self) -> Dict[str, Any]:
        """Retrieves the history to feed back into the Brain."""
        pass
