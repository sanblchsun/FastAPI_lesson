from typing import Optional

from pydantic import BaseModel, validator, Field, ConfigDict


class Book(BaseModel):
    name: str = None
    description: Optional[str] = None


class BookOut(Book):
    id: int
    model_config = ConfigDict(from_attributes=True)


class BookID(BaseModel):
    ok: bool = True
    book_id: int
