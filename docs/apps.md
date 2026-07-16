# Django Applications

## Overview

Notebook is organized as a collection of independent Django applications, each responsible for a specific part of the platform. Rather than concentrating all functionality in a few large applications, Notebook separates responsibilities into smaller, focused modules.

Applications fall into three categories:

* **Core applications**, which provide infrastructure and user-facing interfaces.
* **Domain applications**, which implement the platform's business logic.
* **Third-party and Django applications**, which provide framework functionality and external integrations.

This modular organization makes the project easier to maintain, test, and extend while keeping responsibilities clearly defined.

> **Project Status:** 🚧 Active Development
>
> The application structure documented here reflects the current implementation. New applications and domains may be introduced as Notebook evolves.

---

# Application Structure

```text
notebook/
│
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

---

# Core Applications

Core applications provide the infrastructure and user interfaces that make up the platform. While they coordinate requests and render responses, they generally avoid containing business logic themselves.

## notebook

The `notebook` package is the Django project configuration.

It contains the global project settings, root URL configuration, middleware, WSGI/ASGI entry points, and other project-level configuration. It serves as the application's bootstrap layer and should never contain business logic.

---

## home

The `home` application provides the public-facing portion of Notebook.

Typical responsibilities include:

* Landing pages
* Homepage
* Public information
* General navigation

This application is intended for unauthenticated visitors and acts as the entry point into the platform.

---

## accounts

The `accounts` application manages user identities and authentication.

Its responsibilities include:

* Custom user model
* Authentication
* Authorization
* Registration
* Login and logout
* Password management
* User profile management

The application provides identity management only. Academic business rules remain inside the appropriate domain applications.

---

## dashboard

The `dashboard` application provides authenticated users with their workspace inside Notebook.

Unlike traditional Django applications, the dashboard does **not own** academic data. Instead, it presents information obtained from the domain layer.

Notebook currently provides two primary dashboard experiences.

### Teacher Dashboard

The teacher dashboard is designed for instructors and academic staff.

It provides interfaces for managing educational resources such as courses, learning materials, assignments, and other academic entities through the services exposed by the domain applications.

### Student Dashboard

The student dashboard focuses on the learning experience.

Students can access their enrolled courses, educational content, assignments, and other resources made available to them.

Although both dashboards may interact with similar business entities, each one provides workflows tailored to its users.

---

## api

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

The `domains` package contains the core business logic of Notebook.

Each domain represents a business area of the educational platform and is responsible for implementing its own data models, business rules, validation, and services.

Unlike the presentation applications, domain applications own the academic data and define how that data behaves.

Presentation applications interact with domains through their public services rather than manipulating models directly.

---

## academia

The **Academia** domain represents the academic structure of the platform.

It manages the entities that define an educational institution, including courses, teachers, students, enrollments, and other organizational relationships.

As the project evolves, this domain will continue to serve as the foundation upon which the rest of the platform is built.

---

## contents

The **Contents** domain manages educational resources delivered to learners.

This includes rich-text materials, notes, documents, media, and other learning resources associated with courses.

The domain focuses on the creation, organization, and delivery of educational content rather than the learning process itself.

---

## learning

The **Learning** domain represents the learning process.

It is responsible for the workflows that connect students with educational resources and track their progress through learning activities.

As Notebook grows, additional functionality such as progress tracking, learning analytics, and personalized learning experiences may become part of this domain.

---

## work

The **Work** domain manages academic work completed by students.

Typical responsibilities include assignments, homework, tasks, submissions, deadlines, and grading-related workflows.

Its primary focus is the lifecycle of academic work rather than educational content.

---

# Design Principles

Every application in Notebook is expected to follow several core principles:

* Maintain a single, well-defined responsibility.
* Keep business logic close to the domain that owns it.
* Minimize coupling between applications.
* Expose reusable functionality through well-defined services.
* Remain extensible as the platform grows.

These principles help ensure that new functionality can be added without increasing the complexity of existing applications.

---

# Future Expansion

The modular structure of Notebook allows additional applications to be introduced without significantly affecting the existing architecture.

Examples of future domain applications include:

* Examinations
* Grading
* Notifications
* Messaging
* Reports
* Analytics

The architecture is intentionally designed to support this gradual expansion while preserving clear boundaries between business domains.

---

# Summary

Notebook organizes its functionality into independent Django applications with clearly defined responsibilities.

Core applications provide the user interface and infrastructure, while domain applications implement the business logic that powers the educational platform.

This separation encourages maintainability, code reuse, and long-term scalability as Notebook continues to evolve.
