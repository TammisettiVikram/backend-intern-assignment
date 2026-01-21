"""Test logging configuration"""
import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))

from app.main import app_logger, root_logger

print("Testing logging...")
root_logger.info("Test INFO message from root logger")
root_logger.warning("Test WARNING message from root logger")
root_logger.error("Test ERROR message from root logger")
app_logger.info("Test INFO from app logger")

for handler in root_logger.handlers:
    handler.flush()

time.sleep(1)
print("Logging test complete. Check the log files.")

