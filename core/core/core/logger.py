%%writefile core/logger.py
import logging
import os
from datetime import datetime

def setup_logger(output_dir: str = "outputs") -> logging.Logger:
    """Sets up a customized logger for the ILRT framework."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a unique log file for each run based on the exact time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(output_dir, f"ilrt_session_{timestamp}.log")
    
    # Configure the global ILRT logger
    logger = logging.getLogger("ILRT")
    logger.setLevel(logging.DEBUG)
    
    # Prevent duplicate logs if this cell is run multiple times
    if not logger.handlers:
        # 1. File Handler (saves EVERYTHING, including deep debug data)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(file_formatter)
        
        # 2. Console Handler (keeps your Colab screen clean and readable)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(message)s') 
        ch.setFormatter(console_formatter)
        
        logger.addHandler(fh)
        logger.addHandler(ch)
        
    return logger
