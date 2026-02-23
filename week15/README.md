# Week 13 - FastAPI 

This is a simple FastAPI project for managing users with basic CRUD operations.


## Files

- main.py         → main FastAPI app
- schema.py       → User models
- users.txt       → stores user data
- routes/         → contains user routes
- venv/           → virtual environment

## to run

1. Turn on virtual environment:
venv\Scripts\activate

2. Install packages:
pip install fastapi uvicorn

3. Start the server:
uvicorn main:app --reload

4. Open browser:
- Health check: http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs

Notes

- /users/search must be before /users/{id} in routes.
- Users are stored in users.txt.
- This version uses `UserStore` class to handle users instead of manual file operations.