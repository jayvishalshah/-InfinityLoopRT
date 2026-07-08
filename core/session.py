%%writefile core/session.py
import time
from typing import Any, Dict
from core.interfaces import Target, Brain, Evaluator, Memory
from core.config import ILRTConfig

class RedTeamSession:
    """Manages a single automated red-teaming session."""
    
    def __init__(
        self, 
        config: ILRTConfig,
        target: Target,
        brain: Brain,
        evaluator: Evaluator,
        memory: Memory
    ):
        self.config = config
        self.target = target
        self.brain = brain
        self.evaluator = evaluator
        self.memory = memory
        self.turn_count = 0
        
    def run(self) -> Dict[str, Any]:
        """Executes the Infinity Loop until max turns or a successful attack."""
        print(f"🚀 Starting ILRT Session against {self.config.target_model_name}")
        
        while self.turn_count < self.config.max_turns:
            self.turn_count += 1
            print(f"\n--- Turn {self.turn_count}/{self.config.max_turns} ---")
            
            # Step 1: Brain generates the attack prompt based on memory context
            context = self.memory.get_context()
            attack_prompt = self.brain.generate_attack(
                target_info=self.config.target_model_name,
                context=context
            )
            print(f"🧠 Brain generated prompt: '{attack_prompt[:50]}...'")
            
            # Step 2: Send the attack to the Target model
            try:
                response = self.target.send_prompt(attack_prompt)
                print(f"🎯 Target responded: '{response[:50]}...'")
            except Exception as e:
                print(f"⚠️ Target connection failed: {e}")
                break
                
            # Step 3: Evaluate if the attack bypassed safety filters
            evaluation = self.evaluator.evaluate(attack_prompt, response)
            print(f"⚖️ Evaluation: {evaluation}")
            
            # Step 4: Save everything to Memory so the Brain learns for next time
            self.memory.add_interaction(attack_prompt, response, evaluation)
            
            # Step 5: Check for early victory
            if evaluation.get("success", False):
                print(f"🚨 Attack successful on turn {self.turn_count}!")
                break
                
            # Brief pause to respect API rate limits
            time.sleep(1) 
            
        print("\n🏁 Session Complete.")
        return {
            "total_turns": self.turn_count,
            "final_context": self.memory.get_context()
        }
