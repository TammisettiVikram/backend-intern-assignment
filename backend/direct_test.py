"""Direct logging test"""
import logging
import logging.handlers
import os

log_dir = 'c:\\Users\\vikra\\backend-intern-assignment\\backend\\logs'
os.makedirs(log_dir, exist_ok=True)

handler = logging.handlers.RotatingFileHandler(
    os.path.join(log_dir, 'direct_test.log'),
    maxBytes=10485760,
    backupCount=5
)

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

print(f"Handler created: {handler}")
print(f"File: {handler.baseFilename}")
print(f"Stream: {handler.stream}")

logger.info("This is a test message")
handler.flush()
print("Message logged and flushed")

print(f"File exists: {os.path.exists(os.path.join(log_dir, 'direct_test.log'))}")
