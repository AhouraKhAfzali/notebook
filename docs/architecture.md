# Architecture

## Overview

Notebook follows a **domain-oriented architecture** inspired by the principles of Domain-Driven Design (DDD). Rather than organizing the project around technical layers alone, the application is organized around business domains that encapsulate the platform's academic functionality.

Each business domain owns its models, business rules, and services. User-facing applications such as the teacher dashboard, student dashboard, public website, and REST API act primarily as presentation layers that consume those services instead of implementing business logic themselves.

Although the project is still under active development, this architectural approach establishes clear boundaries between the user interface and the business layer, making the system easier to maintain and extend over time.

---

# Architectural Goals

Notebook's architecture is designed around several long-term goals:

* High cohesion within each domain
* Low coupling between applications
* Reusable business logic
* Clear separation of responsibilities
* Easier testing
* Independent feature development
* Long-term maintainability

---

# High-Level Architecture

```
                 ┌────────────────────┐
                 │       Client       │
                 └─────────┬──────────┘
                           │
                      HTTP / HTTPS
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼
  Students             Teachers                Home
  Dashboard            Dashboard                │
      │                    │                    │
      │                    │                    │
      └────────────────────┼────────────────────┘
                 Service Requests Only
                           │
                           ▼
              ┌──────────────────────────┐
              │      Domain Services     │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │      Domain Models       │
              └────────────┬─────────────┘
                           │
                           ▼
                       Databases
```

---

# Domain-Oriented Design

The central architectural concept in Notebook is the **domain application**.

A domain application represents a business area of the platform rather than a technical component. Examples include course management, learning content, assignments, and academic administration.

Each domain is responsible for implementing the complete business behavior related to its own responsibilities.

A domain contains:

* Database models
* Business services
* Validation rules
* Domain-specific utilities
* Signals
* Forms (when required)
* Internal APIs

---

# Service Layer

The preferred way of interacting with a domain is through its **service layer**.

Services expose the operations that other applications are allowed to perform while hiding the implementation details.

Instead of this:



This provides several important benefits:

* Business rules exist in one location.
* Multiple applications can reuse the same functionality.
* Changes to the database schema affect fewer parts of the project.
* Views remain small and focused on handling requests.

---

# Separation Between Presentation and Domain

Presentation applications are intentionally lightweight.

Their responsibilities include:

* Handling HTTP requests
* Rendering templates
* Processing forms
* Returning API responses
* Performing authentication and permission checks
* Calling domain services

They **should not**:

* Contain business rules
* Manipulate domain models directly
* Duplicate validation logic
* Reimplement workflows already provided by a domain service

This separation keeps presentation code independent of the business implementation.

---

# Request Flow

A typical request moves through the application in the following order:

```
Client
    │
    ▼
URL Dispatcher
    │
    ▼
Home / Dashboards
    │
    ▼
Domain Service
    │
    ▼
Domain Models
    │
    ▼
Database
    │
    ▼
Response
```

The important characteristic is that **the presentation layer communicates with the service layer—not directly with the models**.

---

# Why This Architecture?

This architecture was chosen because educational systems naturally grow in complexity.

As new modules such as grading, attendance, messaging, notifications, examinations, certificates, or analytics are introduced, a service-oriented domain architecture helps prevent the codebase from becoming tightly coupled and difficult to maintain.

By keeping business logic centralized inside domain applications, new interfaces—including REST APIs, administrative tools, background tasks, or future mobile applications—can reuse the same functionality without duplicating logic.

---

# Future Evolution

Notebook is still under active development, and its architecture will continue to evolve.

Future improvements may include:

* More comprehensive domain services
* Background task processing
* Event-driven communication
* Caching strategies
* Additional domain modules
* Improved testing infrastructure

The overall architectural philosophy, however, is expected to remain centered on **domain ownership, service-oriented communication, and clear separation between presentation and business logic**.
