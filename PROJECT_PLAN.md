# Internship/Application Tracker Project Plan

## 1. Project Summary

A full-stack internship and job application tracker that helps users manage applications, statuses, deadlines, notes, contacts, and job posting details, with a future Chrome extension for saving jobs directly from supported job boards.

## 2. Problem Statement

Students and new grads often apply to many internships and jobs across different websites. It becomes hard to remember which roles they applied to, who they contacted, what stage each application is in, and when to follow up. This app organizes the application process in one dashboard.

## 3. Target User

- College students applying for internships
- New grads applying for full-time jobs
- Career switchers tracking many applications

## 4. MVP Features

- [ ] User signup
- [ ] User login/logout
- [ ] Add application manually
- [ ] View all applications
- [ ] View one application in detail
- [ ] Edit application
- [ ] Delete application
- [ ] Update status
- [ ] Add notes
- [ ] Add recruiter/contact information
- [ ] Search applications
- [ ] Filter by status
- [ ] Dashboard summary

## 5. Stretch Features

- [ ] Chrome extension
- [ ] Resume version tracking
- [ ] Interview tracking
- [ ] Email reminders
- [ ] Analytics charts
- [ ] Export to CSV

## 6. Application Statuses

- Saved
- Applied
- Online Assessment
- Interviewing
- Offer
- Rejected
- Withdrawn
- Ghosted

## 7. User Flow

1. User signs up or logs in.
2. User lands on dashboard.
3. User adds a new application manually.
4. User views all applications.
5. User filters/searches applications.
6. User opens application detail page.
7. User updates status, notes, and contacts.
8. Later, user can save jobs through Chrome extension.

## 8. Pages

Public:

- Landing
- Login
- Signup

Protected:

- Dashboard
- Applications List
- Add Application
- Application Detail
- Edit Application
- Settings

## 9. Database Tables

### users

- id
- name
- email
- hashed_password
- created_at
- updated_at

### applications

- id
- user_id
- company
- role_title
- location
- job_url
- source
- status
- employment_type
- salary_range
- date_applied
- deadline
- description
- created_at
- updated_at

### notes

- id
- application_id
- content
- created_at
- updated_at

### contacts

- id
- application_id
- name
- email
- linkedin_url
- role
- notes
- created_at
- updated_at

## 10. API Routes

### Auth

- POST /api/auth/signup
- POST /api/auth/login
- GET /api/auth/me

### Applications

- GET /api/applications
- POST /api/applications
- GET /api/applications/{id}
- PATCH /api/applications/{id}
- DELETE /api/applications/{id}

### Notes

- GET /api/applications/{id}/notes
- POST /api/applications/{id}/notes
- PATCH /api/notes/{id}
- DELETE /api/notes/{id}

### Contacts

- GET /api/applications/{id}/contacts
- POST /api/applications/{id}/contacts
- PATCH /api/contacts/{id}
- DELETE /api/contacts/{id}

### Dashboard

- GET /api/dashboard/summary

### Extension Later

- POST /api/extension/save-job

## 11. Build Milestones

### Milestone 1: Backend Foundation

- [ ] FastAPI app runs
- [ ] PostgreSQL connected
- [ ] Health check route works
- [ ] Alembic migrations work

### Milestone 2: Auth

- [ ] Signup works
- [ ] Login works
- [ ] JWT auth works
- [ ] Protected routes work

### Milestone 3: Application CRUD

- [ ] Create application
- [ ] View applications
- [ ] Update application
- [ ] Delete application
- [ ] User data is protected

### Milestone 4: Frontend MVP

- [ ] Login/signup UI
- [ ] Dashboard
- [ ] Application list
- [ ] Add/edit/detail pages

### Milestone 5: Chrome Extension

- [ ] Extension popup opens
- [ ] Token storage works
- [ ] Job info extraction works
- [ ] Save to backend works

## 12. Learning Checklist

### Backend

- [ ] FastAPI routes
- [ ] Request bodies
- [ ] Response models
- [ ] Pydantic schemas
- [ ] CORS
- [ ] JWT authentication

### Database

- [ ] PostgreSQL basics
- [ ] SQLAlchemy models
- [ ] Relationships
- [ ] Sessions
- [ ] Alembic migrations

### Frontend

- [ ] React components
- [ ] TypeScript basics
- [ ] React Router
- [ ] Forms
- [ ] API calls
- [ ] Auth state
- [ ] Protected routes

### Chrome Extension

- [ ] Manifest V3
- [ ] Popup UI
- [ ] Content scripts
- [ ] Chrome storage
- [ ] Message passing
