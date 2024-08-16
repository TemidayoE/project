Movie Management API

An API that manages movies, users creations and comments

## Features

- Create Users
- List, Delete and Update Movies
- Create comments f

## Dependencies

- Python 3.12+
- FastAPI
- PostgreSQL
- Any other dependencies (refer to the requirements.txt file)


## Step-by-step instructions to set up the project locally.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/movie_API.git
   cd repo


2. **Create and activate a virtual environment**:
   **On macOS/Linux**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

   **On Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate

3. **Install the required dependencies**:
   ```bash
  pip install -r requirements.txt

4. **Run the FastAPI server**:

   ```bash
   uvicorn app.main:app --reload