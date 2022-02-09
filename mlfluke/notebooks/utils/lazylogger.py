import logging
import sys
from pathlib import Path

# logging paths
LOGS_DIR = Path(__file__).parent.parent / "data/logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)


# setting for stdout and file logging
logger = logging.getLogger(__name__)
stdout_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(f"{LOGS_DIR}/debug.log")

# logging levels
logger.setLevel(logging.DEBUG)
stdout_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# the formatters look
fmt_stdout = "%(message)s"
fmt_file = "[%(levelname)s] %(asctime)s | %(filename)s:%(funcName)s:%(lineno)d | %(message)s"

stdout_formatter = logging.Formatter(fmt_stdout)
file_formatter = logging.Formatter(fmt_file)

# set formatters
stdout_handler.setFormatter(stdout_formatter)
file_handler.setFormatter(file_formatter)

# add handlers
logger.addHandler(stdout_handler)
logger.addHandler(file_handler)