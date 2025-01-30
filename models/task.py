from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Task(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed: bool = Field(default=False)
