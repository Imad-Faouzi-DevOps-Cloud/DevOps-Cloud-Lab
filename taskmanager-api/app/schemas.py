# app/schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime

class RoleEnum(str, Enum):
    user = "user"
    admin = "admin"

class StatusEnum(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    archived = "archived"

# User schema
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: RoleEnum

    class Config:
        orm_mode = True

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str

# Ticket creation
class TicketCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "low"

# Ticket display
class TicketOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    status: StatusEnum
    created_at: datetime

    class Config:
        orm_mode = True
