
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Manager")


# Temporary storage
books = {
    1: {"id": 1, "title": "Clean Code", "author": "Robert Martin"},
    2: {"id": 2, "title": "Python Crash Course", "author": "Eric Matthes"},
}


# Input model
class BookCreate(BaseModel):
    title: str
    author: str


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None


# Get all books
@app.get("/books")
def get_books():
    return list(books.values())

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return books[book_id]



@app.patch("/books/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    update_data = book_update.model_dump(exclude_unset=True)

    books[book_id].update(update_data)

    return books[book_id]



@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    deleted_book = books.pop(book_id)

    return {
        "message": "Book deleted successfully",
        "book": deleted_book
    }





# Create a new book
@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    new_id = max(books.keys(), default=0) + 1

    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author,
    }

    books[new_id] = new_book

    return new_book
