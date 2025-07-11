from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app import models, schemas
from app.deps import get_db, get_current_user  # centralized async dependencies

router = APIRouter()

@router.post("/", status_code=201, response_model=schemas.TicketOut)
async def create_ticket(
    ticket: schemas.TicketCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    # Create new ticket owned by current user
    new_ticket = models.Ticket(**ticket.dict(), owner_id=current_user.id)

    # Add, commit, and refresh sequentially to avoid session conflicts
    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)

    return new_ticket

@router.get("/", response_model=List[schemas.TicketOut])
async def get_my_tickets(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    # Fetch all tickets owned by current user
    result = await db.execute(
        select(models.Ticket).where(models.Ticket.owner_id == current_user.id)
    )
    tickets = result.scalars().all()
    return tickets
