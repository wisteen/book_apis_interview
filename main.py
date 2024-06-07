from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()



# In-memory data 
books = {}
book_id_counter = 1


# Create a model
class Book(BaseModel):
	title: str
	author: str
	published_year: int = Field(..., gt=0, le=datetime.now().year)


class BookResponse(Book):
	id: int


# This if for displaying list of data in the in memory data store
@app.get("/books", response_model=List[BookResponse])
def get_books():
	return list(books.values())


# get just a specific book
@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
	book = books.get(book_id)
	if not book:
		raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
	return book

# This is for creating new information in our data store
@app.post("/books", response_model=BookResponse)
def create_book(book: Book):
	global book_id_counter
	global books
	book_id = book_id_counter
	book_id_counter += 1

	book_data = book.dict()
	book_data['id'] = book_id
	books[book_id] = book_data
	return book_data




# This is for updating already stored data
@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated_book: Book):
	book = books.get(book_id)
	if not book:
		raise HTTPException(status_code=404, detail="Book not found!")
	book_data = updated_book.dict()
	book_data['id'] = book_id
	books[book_id] = book_data
	return book_data


# to delete a book
@app.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int):
	if book_id not in books:
		raise HTTPException(status_code=404, detail="Book not found!")
	# del books[book_id]
	book_data = books.pop(book_id)
	return book_data



# Home page
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
def read_root():
    return FileResponse("static/index.html")