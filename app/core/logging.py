import logging
import sys

# Create and configure logger
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  # Output logs to stdout
        logging.FileHandler('app.log')  # Log to a file named app.log
    ]
)

logger = logging.getLogger(__name__)  # Create a logger instance

# Example of logging
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')
