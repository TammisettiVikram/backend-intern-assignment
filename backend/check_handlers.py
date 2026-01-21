"""Test by importing main and checking handlers"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import app.main

print(f"Root logger: {app.main.root_logger}")
print(f"Root logger handlers: {app.main.root_logger.handlers}")
print(f"Number of handlers: {len(app.main.root_logger.handlers)}")

for i, handler in enumerate(app.main.root_logger.handlers):
    print(f"Handler {i}: {handler}")
    if hasattr(handler, 'baseFilename'):
        print(f"  File: {handler.baseFilename}")

print("\nTesting logging...")
app.main.root_logger.info("Test message from imported logger")
app.main.app_logger.info("Test from app logger")

for handler in app.main.root_logger.handlers:
    handler.flush()
    
print("Done. Checking files...")
print(f"App.log exists: {os.path.exists(os.path.join(app.main.log_dir, 'app.log'))}")
print(f"Error.log exists: {os.path.exists(os.path.join(app.main.log_dir, 'error.log'))}")
