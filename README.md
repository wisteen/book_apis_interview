# FastAPI Book Management API

This is a simple book management API built using FastAPI. The API allows you to create, read, update, and delete book records. It supports basic operations to manage a collection of books in an in-memory data store.


## Features

- Add new books
- Retrieve a list of all books
- Get details of a specific book
- Update book information
- Delete a book
- Serve a static homepage


## Installation

To set up this project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/wisteen/book_apis_interview.git
    cd book_apis_interview
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000` to see the homepage.


## Usage

### Adding a New Book

To add a new book, send a POST request to `/books` with the following JSON body:

```json
{
  "title": "New Book Title",
  "author": "Author Name",
  "published_year": 2022
}
```

Retrieving All Books
Send a GET request to /books to retrieve a list of all books.

Retrieving a Specific Book
Send a GET request to /books/{book_id} to retrieve details of a specific book.

Updating a Book
Send a PUT request to /books/{book_id} with the updated book information.

Deleting a Book
Send a DELETE request to /books/{book_id} to delete a book.



## Testing

Tests are written using `pytest`. To run the tests, use the following command:

```bash
pytest test.py
```



#### **5. API Endpoints**

List and describe the available API endpoints with example requests and responses.

```markdown
## API Endpoints

### GET /books

- **Description**: Retrieve a list of all books.
- **Response**: A JSON array of book objects.

### GET /books/{book_id}

- **Description**: Retrieve details of a specific book by ID.
- **Response**: A JSON object with book details.

### POST /books

- **Description**: Add a new book.
- **Request Body**:

    ```json
    {
      "title": "New Book Title",
      "author": "Author Name",
      "published_year": 2022
    }
    ```
- **Response**: The created book object with an assigned ID.

### PUT /books/{book_id}

- **Description**: Update the details of a specific book.
- **Request Body**:

    ```json
    {
      "title": "Updated Book Title",
      "author": "Updated Author Name",
      "published_year": 2022
    }
    ```
- **Response**: The updated book object.

### DELETE /books/{book_id}

- **Description**: Delete a specific book by ID.
- **Response**: Status 204 No Content.



