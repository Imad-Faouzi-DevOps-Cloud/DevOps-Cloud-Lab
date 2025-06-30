# app/routes/tickets.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import SessionLocal
from app.deps import get_current_user

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a ticket
@router.post("/",status_code=201, response_model=schemas.TicketOut)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_ticket = models.Ticket(**ticket.dict(), owner_id=current_user.id)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

# List all tickets for current user
@router.get("/", response_model=List[schemas.TicketOut])
def get_my_tickets(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Ticket).filter(models.Ticket.owner_id == current_user.id).all()
