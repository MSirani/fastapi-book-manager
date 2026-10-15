# FastAPI Book Manager

A simple book management REST API built with FastAPI. This project was created as a learning assignment to practice HTTP methods, request validation, and CRUD operations.

## Features

- Retrieve all books
- Add a new book
- Retrieve a book by ID
- Partially update a book
- Delete a book
- Validate request data using Pydantic
- Handle errors for books that do not exist

## Technologies

- Python
- FastAPI
- Uvicorn
- Pydantic

## Requirements

- Python 3.10 or newer
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MSirani/fastapi-book-manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-book-manager
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment.

   On Windows CMD:

   ```bat
   .venv\Scripts\activate.bat
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the Application

Start the development server:

```bash
python -m uvicorn app:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/books` | Retrieve all books |
| POST | `/books` | Add a new book |
| GET | `/books/{book_id}` | Retrieve a book by ID |
| PATCH | `/books/{book_id}` | Partially update a book |
| DELETE | `/books/{book_id}` | Delete a book |

## Example Request

Create a new book using `POST /books`:

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin"
}
```

## Data Storage

This project uses an in-memory Python dictionary instead of a database. Changes are temporary and are lost when the application restarts.

## License

This project was created for educational purposes.