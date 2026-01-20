from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from dotenv import load_dotenv
import logging

from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.security_test import router as security_test_router
from app.db.init_db import init_db

load_dotenv()

app = FastAPI(
    title="Backend Intern Assignment",
    version="1.0.0"
)

# ✅ REGISTER ALL ROUTERS
app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")          # 👈 ADD THIS
app.include_router(security_test_router, prefix="/api/v1")  # 👈 ADD THIS

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.on_event("startup")
def on_startup():
    init_db()
    logging.info("Database initialized")

@app.get("/")
def root():
    logging.info("Root endpoint accessed")
    return {"message": "Backend is running"}
