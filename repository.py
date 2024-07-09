from schemas import BookOut, Book
from sqldatabase import new_session, BookTable
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: Book) -> int:
        async with new_session() as session:
            task_dick = data.model_dump()
            task = BookTable(**task_dick)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[BookOut]:
        async with new_session() as session:
            query = select(BookTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [BookOut.model_validate(task_model) for task_model in task_models]
            return task_schemas
