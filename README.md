# FastAPI Project with PostgreSQL and Layered Architecture

## Description
TBD


## Project Structure
```
project/
│
├── main.py                   # Entry point for the FastAPI application
├── controllers/              # Contains route definitions
│
├── services/                 # Business logic for the application
│
├── repositories/             # Database access using raw SQL
│
├── database.py               # Database connection setup
├── models.py                 # Pydantic models for request validation
└── requirements.txt          # Project dependencies
```


## Prerequisites
- Python 3.10+
- PostgreSQL database
- `pip` (Python package installer)

## Installation and Running the Project

### Step 0: Clone the Repository
```bash
git clone https://github.com/user/project.git
```

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Database
Set up a database and provide correct connection to it in database.py

### Step 4: Run the FastAPI Server
```bash
uvicorn main:app --reload
```

### Step 5: Access the API Documentation
Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
to view the OpenAPI documentation (Swagger UI).

## Common Commands
- **Start server**: `uvicorn main:app --reload`
- **Install dependencies**: `pip install -r requirements.txt`
- **Access API docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## License
TBD