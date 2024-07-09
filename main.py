from fastapi import FastAPI
from contextlib import asynccontextmanager
from route import router as book_router
from sqldatabase import delete_tables, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Баз очищена")
    await create_tables()
    print("Баз готова")
    yield
    print("выход")


app = FastAPI(lifespan=lifespan)
app.include_router(book_router)




#
#
# @app.get('/')
# def main():
#     return {'key': "Hello"}
#
#
# @app.get("/{pk}")
# def get_item(pk: int, q: int = None):
#     return {'key': pk, 'q': q}
#
#
# @app.get("/users/{pk}/items/{item}")
# def get_user(pk: int, item: str):
#     return {"user": pk, "item": item}
#


# @app.post('/author')
# def post_request_author(author: Author = Body(..., embed=True)):
#     return {'author': author}
#
# @app.post("/book")
# def post_request(item: Book, author: Author, quantity: int = Body(...)):
#     return {'item': item, 'author': author, "quantity": quantity}
#
#
# @app.get("/book")
# def get_book(q: List[datetime] = Query(..., description='samething_description')):
#     return q
#
#
# @app.get('/book/{pk}')
# def get_single_book(pk: int = Path(..., gt=2), pages: int = Query(None, gt=4, le=10)):
#     return {"pk": pk, "pages": pages}

# lst = []
#
#
# @app.post('/book', response_model=Book, response_model_exclude_unset=False)
# def post_request(item: Annotated[Book, Depends()]):
#     return item
#
#
# @app.post('/book1', response_model=Book, response_model_exclude={'pages', 'date'})
# def post_request(item: Book):
#     return item
#
#
# @app.post('/book2', response_model=Book, response_model_include={'pages', 'date'})
# def post_request(item: Book):
#     return item
#
#
# @app.post('/book3', response_model=BookOut)
# def post_request(item: Book):
#     # book = item.dict()
#     # book['id'] = 3
#     # return book
#     return BookOut(**item.dict(), id=3)
