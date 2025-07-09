from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime

# Enums for roles and status
class RoleEnum(str, Enum):
    user = "user"
    admin = "admin"

class StatusEnum(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    archived = "archived"

# Shared config for ORM compatibility
class ORMBase(BaseModel):
    class Config:
        orm_mode = True

# --- User Schemas ---

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(ORMBase):
    id: int
    email: EmailStr
    role: RoleEnum

# --- Token Schema ---
class Token(BaseModel):
    access_token: str
    token_type: str

# --- Ticket Schemas ---

class TicketCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "low"

class TicketOut(ORMBase):
    id: int
    title: str
    description: Optional[str]
    priority: str
    status: StatusEnum
    created_at: datetime
    owner_id: int  # Useful for test assertions
