# Budget App

A full-stack application for tracking personal finances and budget management.

## Project Structure

- `ios/` - SwiftUI iOS application
- `backend/` - Python FastAPI backend

## Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up MySQL database:
   ```
   # Create a MySQL database
   mysql -u root -p
   CREATE DATABASE budgetdb;
   EXIT;
   ```

5. Configure database in .env file:
   ```
   DATABASE_URL=mysql+pymysql://username:password@localhost/budgetdb
   ```

6. Run the server:
   ```
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

7. Access the API documentation:
   ```
   http://localhost:8000/docs
   ```

## Features

- Track income and expenses
- Categorize transactions
- View spending summaries and reports
- Budget planning and management

## API Endpoints

- `/api/transactions/` - Manage transactions
- `/api/categories/` - Manage categories
- `/api/summary/` - Get financial summaries

