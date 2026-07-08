%%writefile core/controller.py
from core.config import ILRTConfig
from core.session import RedTeamSession
from core.logger import setup_logger

class ILRTController:
    """Orchestrates the setup and execution of the Infinity Loop."""
    
    def __init__(self, config: ILRTConfig = None):
        # Use provided config or load the default one
        self.config = config or ILRTConfig()
        # Initialize our global logger
        self.logger = setup_logger(self.config.output_dir)
        self.logger.info("ILRT Controller initialized.")
        
    def run_session(self, target, brain, evaluator, memory):
        """Assembles the components and triggers the session."""
        self.logger.info(f"Preparing session against target: {self.config.target_model_name}")
        
        session = RedTeamSession(
            config=self.config,
            target=target,
            brain=brain,
            evaluator=evaluator,
            memory=memory
        )
        
        try:
            results = session.run()
            self.logger.info(f"Session completed successfully. Total turns: {results['total_turns']}")
            return results
        except Exception as e:
            self.logger.error(f"Session failed with error: {str(e)}")
            raise e
