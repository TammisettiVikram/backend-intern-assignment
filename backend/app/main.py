import logging
import logging.handlers
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, tasks, users
from app.db.base import Base
from app.db.session import engine

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(backend_dir, 'logs')
os.makedirs(log_dir, exist_ok=True)

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
root_logger.addHandler(console_handler)

app_log_path = os.path.join(log_dir, 'app.log')
try:
    app_handler = logging.handlers.RotatingFileHandler(
        app_log_path,
        maxBytes=10485760,
        backupCount=5
    )
    app_handler.setLevel(logging.DEBUG)
    app_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    root_logger.addHandler(app_handler)
except Exception as e:
    print(f"Error creating app log handler: {e}")

error_log_path = os.path.join(log_dir, 'error.log')
try:
    error_handler = logging.handlers.RotatingFileHandler(
        error_log_path,
        maxBytes=10485760,
        backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    root_logger.addHandler(error_handler)
except Exception as e:
    print(f"Error creating error log handler: {e}")

app_logger = logging.getLogger('app')
app_logger.setLevel(logging.INFO)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scalable Intern API", version="1.0.0")

app_logger.info("Starting Scalable Intern API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

@app.get("/")
def health_check():
    app_logger.info("Health check endpoint accessed")
    return {"status": "active", "version": "v1.0.0"}

@app.on_event("shutdown")
def shutdown_event():
    """Flush all logging handlers on shutdown"""
    app_logger.info("Application shutting down")
    for handler in root_logger.handlers:
        handler.flush()
    root_logger.info("Logging handlers flushed")