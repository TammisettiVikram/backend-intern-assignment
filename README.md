# Backend Developer Intern Assignment  
**Scalable REST API with Authentication & Role-Based Access**

---

## Project Overview

This project implements a **secure, scalable REST API** with **JWT-based authentication**, **role-based access control**, and **CRUD operations** on a secondary entity (**Tasks**).  
A **basic but functional React frontend** is included to demonstrate and interact with the APIs.

The project follows **industry best practices** in backend architecture, security, and API design, and is suitable for real-world extension.

---

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication (python-jose)
- bcrypt (password hashing)

### Frontend
- React 19
- React Router v7
- Axios
- Tailwind CSS

---

## Core Features Implemented

### Backend (Primary Focus)

- User registration & login with hashed passwords
- JWT authentication & authorization
- Role-based access control (user / admin)
- CRUD APIs for Tasks
- API versioning (`/api/v1`)
- Centralized error handling & validation
- Swagger API documentation
- PostgreSQL database integration

---

### Frontend (Supportive)

- Login & registration pages
- Protected dashboard (JWT required)
- Create, read, update, delete tasks
- API error & success handling
- Responsive UI with Tailwind CSS

---

### Security & Scalability

- Secure password hashing (bcrypt)
- JWT-based authentication
- Protected routes with dependency injection
- Modular, scalable project structure
- Easily extendable to Redis, Docker, or microservices

---

## Database Schema

### Users
- `id` (UUID, Primary Key)
- `email` (unique)
- `hashed_password`
- `role` (USER / ADMIN)
- `created_at`

---

### Admin Access
- at directory \backend
- python make_admin.py user@example.com
How to check
- By visiting
http://localhost:8000/docs
- And clicking Authorize
Giving credentials of a user to make that user as an admin (usually access token of that user)

---

### Tasks
- `id` (UUID, Primary Key)
- `title`
- `description`
- `owner_id` (Foreign Key → users.id)
- `created_at`

---

## How to Run Locally

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL
- Git

---

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

---

### Create .env file

DATABASE_URL=postgresql://<username>:<password>@localhost:5432/intern_assignment
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

---

### Run the backend:
python -m uvicorn app.main:app --reload

### Swagger documentation:
http://localhost:8000/docs

---

### Frontend Setup
cd frontend
npm install
npm start

### Frontend runs at:
http://localhost:3000

---

### API Endpoints
Authentication
- POST /api/v1/auth/register – Register new user
- POST /api/v1/auth/login – Login and receive JWT

Users
- GET /api/v1/users/me – Get current user
- GET /api/v1/users/ – List all users (admin only)

Tasks
- POST /api/v1/tasks – Create task
- GET /api/v1/tasks – Get user tasks
- PUT /api/v1/tasks/{id} – Update task
- DELETE /api/v1/tasks/{id} – Delete task

---

### Application log files are included in the repository under:
backend/logs/app.log

### Logs capture:
- Database initialization
- Authentication attempts
- Warnings and errors
- Health checks

---

### Scalability Notes
- Stateless Authentication: JWT-based auth enables horizontal scaling behind   load balancers.
- Modular Architecture: Separation of concerns (models, schemas, services APIs) allows easy feature expansion.
- Future Enhancements:
- Redis caching for frequently accessed data
- Microservice separation (Auth, Tasks)
- Containerization using Docker
- Centralized logging and monitoring

---

### Deliverables Covered

- Backend REST APIs with authentication and full CRUD

- Role-based access control

- PostgreSQL database schema

- Swagger API documentation

- Basic React frontend connected to APIs

- Application logs included

- Scalability considerations documented

---

### Conclusion
This project fulfills all the requirements of the Backend Developer Intern assignment by focusing on secure API design, clean architecture, and scalability, while providing a minimal frontend to demonstrate functionality.
