from typing import Optional

from pydantic import BaseModel, validator, Field


class Book(BaseModel):
    name: str = None
    description: Optional[str] = None


class BookOut(Book):
    id: int


class BookID(BaseModel):
    ok: bool = True
    book_id: int
