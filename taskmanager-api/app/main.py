# app/main.py

from fastapi import FastAPI
from app.routes import auth, tickets

# Initialize FastAPI app
app = FastAPI(title="Support Ticket API")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tickets.router, prefix="/tickets", tags=["tickets"])

@app.get("/")
def root():
    return {"message": "Support Ticket API is running."}

@app.get("/health")
def health():
    return {"status": "ok"}

