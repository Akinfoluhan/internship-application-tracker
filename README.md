# Internship Application Tracker

A full-stack web application for tracking and managing job and internship applications throughout the recruiting process.

Built with a focus on backend development, database design, authentication, and RESTful APIs.

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Authentication:** JWT, Argon2 password hashing
- **Planned Frontend:** React, TypeScript
- **Planned Extension:** Chrome Extension (Manifest V3)

## Features

**Currently implemented:**

- RESTful CRUD APIs for job applications
- Persistent PostgreSQL storage
- User registration and login
- Secure password hashing using Argon2
- JWT-based access token generation
- Database schema migrations with Alembic
- User and application database relationships

**In Progress / Planned:**

- Protected API endpoints and user-specific application management
- Application search and filtering
- Dashboard for tracking application progress
- React and TypeScript frontend
- Chrome extension for saving job postings directly from websites
- Automated testing and deployment

## Running Locally

The backend is located in the `backend/` directory.

Configure the PostgreSQL connection and JWT secret in a `.env` file using the `DATABASE_URL` and `JWT_SECRET_KEY` variables.

With the Python dependencies installed, run the database migrations using `alembic upgrade head`.

Start the development server using:

`uvicorn app.main:app --reload`

The interactive API documentation is available at:

`http://127.0.0.1:8000/docs`

## Project Status

Actively under development. The core backend, database integration, and user authentication flows are implemented. Currently working on authenticated API access and user-specific data management.
