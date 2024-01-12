import logging
from datetime import datetime

# Set up the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.basicConfig()
sql_logger = logging.getLogger("sqlalchemy.engine")
sql_logger.setLevel(logging.INFO)

# Create a FileHandler with a dynamically generated filename
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_path = f"../backend/logs/log_{current_datetime}.log"
handler = logging.FileHandler(log_file_path)
handler.setLevel(logging.DEBUG)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)
sql_logger.addHandler(handler)
