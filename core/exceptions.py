%%writefile core/exceptions.py
class ILRTError(Exception):
    """Base exception for all Infinity Loop Red Teaming errors."""
    pass

class TargetConnectionError(ILRTError):
    """Raised when the target model fails to respond or times out."""
    pass

class BrainGenerationError(ILRTError):
    """Raised when the attacker model fails to generate a valid prompt."""
    pass

class EvaluationError(ILRTError):
    """Raised when the evaluator fails to parse or score a response."""
    pass
