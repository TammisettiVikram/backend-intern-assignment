from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class TaskCreate(TaskBase):
    pass

# New Schema for Updates
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class TaskOut(TaskBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True