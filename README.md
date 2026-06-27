SaaS Billing Portal

A backend REST API for a **SaaS Billing Portal** developed using **FastAPI**. This project demonstrates user authentication, JWT-based authorization, secure password hashing, and database management using SQLAlchemy and SQLite.


 Project Overview

The SaaS Billing Portal is designed to provide a secure backend for Software-as-a-Service (SaaS) applications. It allows users to register, log in securely, and access protected resources using JSON Web Tokens (JWT).

This project follows REST API principles and is built with a modular architecture, making it easy to extend with additional features such as subscription management, payment gateways, invoices, and role-based access control.


 Features

- User Registration
- User Login
- Password Hashing using bcrypt
- JWT Authentication
- Protected API Routes
- SQLite Database Integration
- SQLAlchemy ORM
- FastAPI Framework
- Pydantic Validation
- Modular Project Structure
- RESTful API Design

Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| SQLAlchemy | ORM |
| SQLite | Database |
| JWT | Authentication |
| Passlib (bcrypt) | Password Hashing |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |
| Git & GitHub | Version Control |


Project Structure

```
backend/
│
├── app/
│   ├── routers/
│   │   └── auth.py
│   │
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   ├── main.py
│   └── __init__.py
│
├── requirements.txt
├── .gitignore
└── README.md


Move into the project

```bash
cd backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment
 
  Windows

bash
venv\Scripts\activate


Linux / macOS

bash
source venv/bin/activate


Install the required packages

bash
pip install -r requirements.txt


Run the server

bash
uvicorn app.main:app --reload
```

The application will start at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

API Endpoints

Authentication

--Register User

```
POST /register
```

--Login User

```
POST /login
```

-- Get Current User Profile

```
GET /profile
```

-- Health Check

```
GET /health
```



 Authentication Flow

1. Register a new account.
2. Login using your email and password.
3. Receive a JWT access token.
4. Use the JWT token to access protected endpoints.
5. The backend validates the token before granting access.



Database

Current Database:

- SQLite

ORM:

- SQLAlchemy



Future Enhancements

- Role-Based Access Control (Admin & Customer)
- Subscription Management
- Stripe Payment Integration
- Billing Dashboard
- Invoice Generation
- Email Verification
- Password Reset
- PostgreSQL Support
- Docker Deployment
- React Frontend



 Learning Outcomes

This project demonstrates practical knowledge of:

- REST API Development
- FastAPI
- SQLAlchemy ORM
- JWT Authentication
- Password Hashing
- Dependency Injection
- API Security
- CRUD Operations
- Database Integration
- Git & GitHub



Backend Developer

GitHub:
https://github.com/gnanavis06-collab



 License

This project is created for learning and educational purposes.