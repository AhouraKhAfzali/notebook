# Architecture

## Overview

Notebook is designed as a modular educational platform built on top of Django. Rather than concentrating all functionality into a few large Django applications, the project separates business logic into independent domains. This architecture promotes maintainability, scalability, and clear separation of responsibilities.

The project currently combines:

- Traditional server-rendered Django applications
- Django REST Framework APIs
- Bootstrap-based frontend
- JWT authentication
- Custom authentication system
- Modular domain organization

The architecture has been designed with future expansion in mind. Although the project is still under active development, the current structure already provides a strong foundation for additional educational modules and services.

---

# Project Status

> **⚠️ Active Development**

Notebook is currently under active development.

The architecture documented in this file represents the current implementation but should not be considered final. New applications, services, APIs, and database models will continue to be introduced as the project evolves.

Some modules currently contain placeholder implementations intended for future expansion.

---

# High-Level Architecture

```
                    ┌────────────────────┐
                    │      Browser       │
                    └─────────┬──────────┘
                              │
                    HTTP / HTTPS Requests
                              │
                              ▼
                 ┌─────────────────────────┐
                 │      Django Project      │
                 └─────────┬───────────────┘
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼
 Template Views        REST API           Authentication
 (Bootstrap)        (DRF + JWT)         Custom User Model
      │                    │
      └────────────┬───────┘
                   ▼
          Domain Applications
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
 Academia      Learning     Contents
                   │
                   ▼
                Work
                   │
                   ▼
              Database
```

---

# Architectural Philosophy

The project follows several architectural principles.

## Domain Separation

Instead of grouping code by technical components (models, views, forms), Notebook groups functionality by business domain.

Example:

```
Domains

Academia
Learning
Contents
Work
```

Each domain owns its own:

- Models
- Views
- URLs
- Templates
- Forms
- Business rules

This minimizes coupling between unrelated parts of the application.

---

## Modular Design

Each Django application should solve one specific problem.

For example:

- Accounts handles authentication.
- Dashboard handles the user dashboard.
- API exposes REST endpoints.
- Learning manages educational workflows.
- Contents manages learning materials.

No application should become responsible for unrelated functionality.

---

## Separation of Concerns

Responsibilities are intentionally separated.

```
Presentation Layer
        │
        ▼
Django Views / API Views
        │
        ▼
Business Logic
        │
        ▼
Database Models
```

Templates should contain presentation logic only.

Business rules belong in Python code.

Database models should represent data rather than user interface behavior.

---

# Project Structure

```
notebook/

├── accounts/
├── api/
├── dashboard/
├── home/
│
├── domains/
│   ├── academia/
│   ├── contents/
│   ├── learning/
│   └── work/
│
├── notebook/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── templates/
├── static/
├── utils/
└── manage.py
```

---

# Application Responsibilities

## notebook

Contains the global project configuration.

Responsibilities include:

- Django settings
- URL routing
- WSGI/ASGI configuration
- Static and media configuration
- Installed applications
- Middleware configuration

This package should never contain business logic.

---

## home

Acts as the public entry point of the project.

Typical responsibilities include:

- Landing pages
- Homepage
- Public information
- Navigation

---

## accounts

Responsible for identity management.

Responsibilities include:

- Custom user model
- Authentication
- Login
- Logout
- Registration
- Password management

This application acts as the authentication provider for the rest of the project.

---

## dashboard

Provides authenticated users with their personal workspace.

Typical responsibilities include:

- User dashboard
- Statistics
- Shortcuts
- User-specific information

---

## api

Contains REST endpoints exposed through Django REST Framework.

Responsibilities include:

- API routing
- Serializers
- Authentication
- JWT integration
- API permissions

The API layer should expose business functionality without duplicating business logic.

---

# Domain Applications

The core business logic of Notebook resides inside the **domains** package.

```
domains/

academia/
learning/
contents/
work/
```

This organization reflects business concepts rather than technical implementation.

Future domains can be added without affecting existing applications.

---

## Academia

Responsible for educational organization.

Potential responsibilities include:

- Courses
- Academic structures
- Teachers
- Students
- Class organization

---

## Learning

Responsible for learning workflows.

Possible responsibilities include:

- Lessons
- Learning progress
- Exercises
- Educational activities
- Completion tracking

---

## Contents

Responsible for educational resources.

Examples include:

- Notes
- Articles
- Files
- Media

---

## Work

Responsible for practical educational work.

Potential responsibilities include:

- Assignments
- Tasks
- Homework
- Activities
- Submissions

---

# URL Architecture

The project follows a simple routing hierarchy.

```
/

├── admin/
├── auth/
├── dashboard/
├── api/
└── ...
```

Each Django application owns its own URL configuration.

This avoids a large centralized routing file.

---

# Request Flow

A typical request follows this sequence.

```
Browser

    │

    ▼

URL Dispatcher

    │

    ▼

View

    │

    ▼

Business Logic

    │

    ▼

Model

    │

    ▼

Database

    │

    ▼

Response

    │

    ▼

Browser
```

REST requests follow the same flow but return JSON instead of rendered HTML.

---

# Authentication Architecture

Notebook uses a custom Django user model.

```
Client

   │

Login

   │

   ▼

Authentication

   │

   ▼

Custom User Model

   │

   ▼

Permissions
```

For API requests:

```
Client

   │

JWT Token

   │

   ▼

REST Framework Authentication

   │

   ▼

Authenticated Request
```

This allows both browser-based sessions and API authentication to coexist.

---

# Frontend Architecture

The frontend currently follows Django's traditional template system.

```
Template

↓

Bootstrap Components

↓

CSS

↓

JavaScript
```

Rendering occurs on the server.

Future frontend frameworks can be integrated through the REST API without changing business logic.

---

# Static Assets

Static resources are separated from application logic.

```
static/

CSS

JavaScript

Images

Icons
```

Templates should reference static assets through Django's static file system.

---

# Media Files

Uploaded files are stored separately from application code.

```
media/

Uploaded Images

Documents

Attachments
```

This separation simplifies deployment and backups.

---

# Database Layer

The project currently uses SQLite during development.

The architecture is designed to support PostgreSQL in production without requiring significant application changes.

Database access is performed exclusively through Django's ORM.

Direct SQL should only be used when absolutely necessary.

---

# REST API Architecture

The API is built using Django REST Framework.

Responsibilities include:

- Serialization
- Authentication
- Validation
- Permissions
- JSON responses

The API should remain independent from template rendering.

Business logic should be shared whenever possible instead of duplicated.

---

# Security Architecture

Current security mechanisms include:

- Django Authentication
- CSRF Protection
- Session Management
- Password Validation
- JWT Authentication
- Django Middleware

Additional security improvements planned include:

- Rate limiting
- API throttling
- Object-level permissions
- Audit logging

---

# Scalability Considerations

Notebook has been structured to accommodate future growth.

Design decisions supporting scalability include:

- Modular applications
- Domain separation
- REST API
- Custom authentication
- Independent URL configurations
- Reusable templates

Future architectural improvements may include:

- Service layer
- Background task processing
- Caching
- Docker deployment
- Microservices (if justified)

---

# Architectural Goals

The long-term architecture aims to achieve:

- High maintainability
- Low coupling
- High cohesion
- Reusable components
- Clear boundaries between domains
- Easy onboarding for contributors
- Production readiness
- Long-term extensibility

---

# Future Improvements

The architecture is expected to evolve with features such as:

- Notification service
- Messaging system
- Activity logging
- Analytics
- Object storage integration
- Background workers
- Email service abstraction
- Full test architecture
- API versioning

---

# Conclusion

Notebook adopts a modular, domain-oriented architecture that prioritizes maintainability over short-term convenience. By separating functionality into independent Django applications and business domains, the project establishes a foundation that can continue to grow without becoming a monolithic codebase.

Although the project is still under active development, the current architectural direction reflects a commitment to clean software design, scalability, and long-term sustainability.