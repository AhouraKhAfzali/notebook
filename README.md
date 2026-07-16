# Notebook

> A modern learning management and educational platform built with Django, Django REST Framework, Bootstrap 5, and PostgreSQL.

> **⚠️ Project Status:** This project is currently under active development. Features, APIs, database schema, and user interfaces are continuously evolving and may change without notice. The project is **not yet production-ready**.

---

## Overview

Notebook is a modular educational platform designed to simplify the management of educational content, courses, learning materials, and user interaction.

Instead of being implemented as a single monolithic Django application, Notebook follows a modular architecture where each business domain is isolated into its own Django application. This approach improves maintainability, scalability, and long-term development.

The project contains both traditional server-rendered pages and a RESTful API, allowing future integration with mobile applications, desktop clients, or modern JavaScript frontends.

---

## Features

Current and planned features include:

- User authentication
- JWT Authentication for APIs
- Student and instructor accounts
- Educational content management
- Learning resources
- Course organization
- Dashboard
- Administrative panel
- REST API
- Responsive Bootstrap 5 interface
- Modular domain-based architecture
- Scalable project structure

More features are continuously being developed.

---

## Technology Stack

### Backend

- Python
- Django
- Django REST Framework
- JWT Authentication

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Database

- SQLite (development)

### Other Technologies

- Pillow
- Django Filters
- Whitenoise
- Gunicorn (deployment)

---

## Project Structure

The project follows a modular architecture.

```
notebook/
│
├── accounts/
├── api/
├── dashboard/
│
├── domains/
│   ├── academia/
│   ├── contents/
│   ├── learning/
│   └── work/
│
├── core/
├── templates/
├── static/
├── media/
└── docs/
```

Each domain is responsible for a specific part of the system and remains as independent as possible.

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

## Getting Started

Clone the repository.

```bash
git clone https://github.com/AhouraKhAfzali/notebook.git
```

Move into the project.

```bash
cd notebook
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run migrations.

```bash
python manage.py migrate
```

Start the development server.

```bash
python manage.py runserver
```

---

## Architecture

Notebook is designed around domain separation rather than feature accumulation.

Instead of placing every model inside a single application, related functionality is grouped into dedicated domains.

Example:

```
Domains
│
├── Academia
│      ├── Courses
│      ├── Teachers
│      └── Students
│
├── Learning
│      ├── Lessons
│      ├── Exercises
│      └── Progress
│
├── Contents
│      ├── Notes
│      ├── Articles
│      └── Files
│
└── Work
       ├── Tasks
       ├── Assignments
       └── Activities
```

This organization makes future expansion significantly easier while reducing coupling between components.

---

## REST API

The project exposes a REST API powered by Django REST Framework.

Authentication is handled using JSON Web Tokens (JWT).

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

This project currently does not specify a license.

---

## Author

**Ahoura Khajeh Afzali**

Backend developer and data science enthusiast

---

## Acknowledgements

This project is being developed as a long-term educational platform and serves as both a learning project and a foundation for future production-ready educational systems.
