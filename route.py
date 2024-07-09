from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import Book, BookOut, BookID

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.post("")
async def add_book(
        item: Annotated[Book, Depends()],
) -> BookID:
    book_id = await TaskRepository.add_one(item)
    return {"ok": True, "book_id": book_id}


@router.get("")
async def get_books() -> list[BookOut]:
    books = await TaskRepository.get_all()
    return books
