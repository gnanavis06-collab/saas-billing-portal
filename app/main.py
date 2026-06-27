from .routers import auth
from fastapi import FastAPI

from .database import engine, Base
from . import models

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="SaaS Billing Portal API",
    version="1.0.0"
)
app.include_router(auth.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to SaaS Billing Portal 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }