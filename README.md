# Notebook

**Notebook** is an open-source teaching and learning management platform built with **Django** and **Bootstrap**. It enables educational institutions and teachers to manage academic activities through a modern web interface, providing dedicated workspaces for both teachers and students.

> **⚠️ Project Status:** This project is currently under active development. Features, architecture, APIs, and database models may change as the project evolves. The documentation is updated alongside development but may occasionally lag behind the latest implementation.. The project is **not yet production-ready**.

---

## Overview

Notebook is designed around the idea of separating business logic from presentation. Rather than allowing user-facing applications to directly interact with domain models, the project follows a service-oriented domain architecture where business logic is encapsulated inside domain applications.

The platform currently focuses on providing tools for managing educational workflows such as courses, assignments, learning materials, students, teachers, and other academic resources while maintaining a clean separation between the user interface and the underlying business logic.

---

## Features

* Course organization
* Assignment management
* Educational content management
* Student management
* Teacher management
* Authentication and authorization
* Separate dashboards for teachers and students
* Responsive Bootstrap interface
* Service-oriented domain architecture
* Extensible modular application structure
* User authentication
* Learning resources

As development continues, additional academic features will be introduced.

---

## Architecture

Notebook follows a modular architecture inspired by **Domain-Driven Design (DDD)** principles.

The project is divided into multiple Django applications with clearly defined responsibilities.

Business rules and domain logic live inside dedicated **domain applications**, while presentation applications such as dashboards consume services exposed by those domains.

This separation helps keep the codebase maintainable, reusable, and easier to extend.

A complete explanation of the architecture is available in **architecture.md**.

---

## Dashboards

Notebook currently provides two primary user dashboards.

## Teacher Dashboard

The teacher dashboard contains functionality related to course administration and academic management, including creating and managing educational resources.

Examples include:

* Managing courses
* Creating assignments
* Managing educational content
* Managing students
* Monitoring academic activities

## Student Dashboard

The student dashboard focuses on learning activities and provides students with access to educational resources relevant to their enrolled courses.

Examples include:

* Viewing courses
* Accessing course content
* Viewing assignments
* Tracking academic progress

Although both dashboards may interact with similar business entities, each one has its own workflows and use cases.

---

## Design Principles

Notebook is built around several core principles:

* Separation of business logic from presentation
* Modular Django applications
* Reusable domain services
* Maintainable project structure
* Scalable architecture for future expansion
* Clear responsibility boundaries between applications

One important architectural rule is that presentation applications (such as the dashboards and home application) **do not communicate directly with domain models or databases**. Instead, they access business functionality through services provided by the corresponding domain applications.

---

## Technology Stack

* Python
* Django
* Django REST Framework
* Bootstrap
* HTML
* CSS
* JavaScript
* SQLite (development)
* CKEditor 5

Additional technologies may be introduced as the project evolves.

---

## Documentation

Detailed documentation is available inside the **docs/** directory.

| Document | Description |
|-----------|-------------|
| architecture.md | Project architecture and design decisions |
| installation.md | Installation guide |
| apps.md | Django applications |

More documentations will be added in the future.

---

## Development Status

The project is under continuous development.

Current priorities include:

- Expanding educational modules
- Completing REST API endpoints
- Improving user experience
- Performance optimization
- Documentation

Some modules may currently be incomplete or serve as placeholders for future functionality.

---

## Roadmap

Planned improvements include:

- Complete course management
- Assignment workflow
- Notifications
- Messaging system
- Activity tracking
- Analytics dashboard
- Docker support
- Comprehensive unit testing

---

## Contributing

Contributions, suggestions, and issue reports are welcome.

---

## License

Project currently does not have a license.

---

## Author

**Ahoura Khajeh Afzali**

Backend developer and data science enthusiast

---

## Acknowledgements

This project is being developed as a long-term educational platform and serves as both a learning project and a foundation for future production-ready educational systems.
