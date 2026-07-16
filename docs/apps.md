# Django Applications

## Overview

Notebook follows a modular application architecture where each Django application is responsible for a specific area of the system.

Instead of placing all functionality into one or two large applications, the project separates responsibilities into multiple independent apps. This organization improves maintainability, readability, scalability, and collaboration.

The project currently consists of three categories of applications:

- Core Applications
- Domain Applications
- Django Built-in Applications

---

# Application Structure

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
└── notebook/
```

Each application owns its own models, views, URLs, templates, forms, and administrative configuration whenever appropriate.

---

# Core Applications

Core applications provide infrastructure and common functionality used throughout the project.

---

# notebook

**Type**

Project Configuration

**Responsibilities**

- Global Django configuration
- Settings
- Root URL configuration
- WSGI configuration
- ASGI configuration
- Middleware configuration
- Installed applications
- Static and media configuration

This package contains the project's global configuration and should never contain business logic.

---

# home

**Purpose**

Public-facing pages.

Responsibilities include:

- Landing page
- Homepage
- Public navigation
- Static informational pages

This application serves as the public entry point of the platform.

---

# accounts

**Purpose**

Identity and authentication management.

Responsibilities include:

- Custom user model
- User registration
- Login
- Logout
- Password management
- User profile management
- Authentication
- Authorization

This application acts as the authentication provider for every other application.

No business-specific logic should be implemented here.

---

# dashboard

**Purpose**

Authenticated user workspace.

Responsibilities include:

- User dashboard
- Personal overview
- Statistics
- Quick actions
- Navigation hub

The dashboard aggregates information from multiple applications rather than owning the underlying data.

---

# api

**Purpose**

REST API.

The API application exposes functionality through Django REST Framework.

Responsibilities include:

- API routing
- Serializers
- ViewSets
- Authentication
- JWT integration
- Permissions
- JSON responses

The API should expose existing business functionality rather than implementing separate business rules.

---

# Domain Applications

The business logic of Notebook lives inside the **domains** package.

```
domains/

academia/

contents/

learning/

work/
```

Each domain represents a business concept rather than a technical layer.

This separation reduces coupling and simplifies future expansion.

---

# Academia

## Purpose

Educational organization.

Current and future responsibilities include:

- Academic entities
- Educational organization
- Courses
- Students
- Teachers
- Class relationships

Academia acts as the structural backbone of the educational platform.

---

# Learning

## Purpose

Learning workflow.

Responsibilities include:

- Learning process
- Lessons
- Educational progress
- Exercises
- Learning activities

Future versions may also include:

- Progress tracking
- Learning analytics
- Personalized recommendations

---

# Contents

## Purpose

Educational content management.

Responsibilities include:

- Notes
- Rich text content
- Articles
- Educational resources
- Uploaded materials

This application manages the educational resources consumed by learners.

---

# Work

## Purpose

Practical educational work.

Responsibilities include:

- Assignments
- Homework
- Activities
- Tasks
- Student submissions

The Work domain focuses on educational tasks rather than learning materials.

---

# Application Dependencies

The dependency direction should remain as follows:

```
                 notebook

                     │

     ┌───────────────┼───────────────┐

     ▼               ▼               ▼

 accounts        dashboard          api

                     │

                     ▼

             Domain Applications

      ┌──────────┬──────────┬──────────┐

      ▼          ▼          ▼          ▼

 academia   learning   contents    work
```

Business domains should not become tightly coupled to one another.

Whenever communication is required, it should occur through clearly defined interfaces.

---

# Communication Between Applications

Applications should communicate through:

- Django ORM relationships
- Service functions
- Shared utilities
- Signals (when appropriate)

Applications should avoid:

- Circular imports
- Direct dependencies on internal implementation details
- Cross-app template rendering
- Copying business logic

---

# URL Ownership

Every application has its own URL configuration.

```
accounts/

    urls.py

dashboard/

    urls.py

api/

    urls.py

learning/

    urls.py
```

The project URL configuration should only include application URLs.

---

# Templates

Applications should contain their own templates whenever those templates belong exclusively to that application.

Shared templates should reside inside the global templates directory.

Example:

```
templates/

accounts/

dashboard/

learning/

contents/
```

This organization keeps templates close to the business logic they represent.

---

# Static Files

Reusable assets should be placed inside the global static directory.

Examples include:

- CSS
- JavaScript
- Images
- Icons

Application-specific static files may also be used where appropriate.

---

# Models

Every application owns its own models.

Relationships between applications should remain meaningful and minimal.

A model should never exist simply because another application requires it.

Instead, models should represent real business entities.

---

# Forms

Forms belong to the application that owns the corresponding models.

- Registration forms → Accounts
- Content forms → Contents
- Assignment forms → Work

---

# Permissions

Permissions should remain close to the business domain.

Accounts

- Login
- Registration
- Password changes

Learning

- Lesson access
- Progress updates

Contents

- Content editing
- Content publishing

Work

- Assignment submission
- Task management

---

# Admin Integration

Each application registers its own models inside its own `admin.py`.

Administrative customizations remain inside the owning application.

---

# Design Principles

Every application should satisfy the following principles.

## Single Responsibility

Each application should solve one primary business problem.

---

## High Cohesion

Related functionality should remain together.

---

## Low Coupling

Applications should know as little as possible about one another.

---

## Reusability

Business logic should be reusable by:

- Django Views
- REST API
- Future CLI tools
- Background tasks

---

## Scalability

New domains should be added without requiring major architectural changes.

Future examples include:

```
domains/

exams/

notifications/

payments/

certificates/

messaging/

analytics/
```

---

# Future Application Roadmap

The current architecture allows additional applications to be introduced as the platform grows.

Possible future applications include:

| Application | Purpose |
|------------|---------|
| exams | Online examinations |
| messaging | User communication |
| notifications | Email and in-app notifications |
| analytics | Learning analytics |
| reports | Reporting system |
| grading | Assessment and grading |

---

# Summary

Notebook adopts a modular application architecture in which every Django application has a clearly defined responsibility.

This separation makes the project easier to understand, easier to test, easier to extend, and significantly more maintainable as the codebase grows.

As development continues, new functionality will be added by extending the existing architecture rather than increasing the responsibilities of existing applications.