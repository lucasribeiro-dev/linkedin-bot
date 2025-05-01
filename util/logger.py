import logging
import os
from datetime import datetime


def setup_logger():
    """Configura o sistema de logs"""
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    logger = logging.getLogger('linkedin_bot')
    logger.setLevel(logging.INFO)
    
    # Handler para arquivo
    log_file = f'logs/linkedin_bot_{datetime.now().strftime("%Y%m%d")}.log'
    file_handler = logging.FileHandler(log_file)
    
    # Handler para console
    console_handler = logging.StreamHandler()
    
    # Formato do log
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger