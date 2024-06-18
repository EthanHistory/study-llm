import logging
from colorama import init, Fore, Style

# Initialize colorama to work on Windows
init(autoreset=True)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a console handler and set the logging level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter with colored output
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_format = f"{Fore.GREEN}{record.msg}{Style.RESET_ALL}"
        return log_format

formatter = ColoredFormatter()

# Add the formatter to the handler
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)