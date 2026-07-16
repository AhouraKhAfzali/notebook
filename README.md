# Notebook

> A Django-powered online teaching and learning platform built with Bootstrap.
>
> **🚧 Project Status: Under Active Development**

Notebook is a web-based educational platform designed to provide teachers and students with an organized environment for managing educational content, assignments, learning materials, and academic activities.

The project is currently under active development. Core features are being implemented and improved continuously, and some parts of the system are incomplete or subject to change.

---

## Features

Current and planned features include:

* User authentication
* Teacher dashboard
* Student dashboard
* Educational content management
* Course organization
* Assignment management
* Learning resources
* REST API
* Responsive Bootstrap interface
* Rich text editing
* Modular Django architecture

---

## Technology Stack

### Backend

* Python
* Django
* Django REST Framework

### Frontend

* Bootstrap 5
* HTML5
* CSS3
* JavaScript

### Database

* SQLite (development)

### Other Libraries

* CKEditor 5
* Pillow
* Additional packages listed in `requirements.txt`

---

## Project Structure

```
notebook/
│
├── accounts/
├── api/
├── dashboard/
├── domains/
│   ├── academia/
│   ├── contents/
│   ├── learning/
│   └── work/
├── home/
├── notebook/
├── static/
├── templates/
├── utils/
├── manage.py
└── requirements.txt
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/AhouraKhAfzali/notebook.git

cd notebook
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
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

The project follows Django's application-based architecture while organizing business logic into dedicated domain modules.

Major components include:

* Authentication
* Dashboard
* Educational domains
* API layer
* Shared utilities

This separation makes the project easier to maintain and extend as new educational features are introduced.

---

## Development Status

This project is **not yet production-ready**.

Some features are currently being implemented, while others may be redesigned as the architecture evolves.

Expect:

* New modules
* Database changes
* API changes
* UI improvements
* Performance optimizations

Breaking changes may occur until the first stable release.

---

## Contributing

Contributions, suggestions, and bug reports are welcome.

Before submitting a pull request, please:

* Follow Django best practices.
* Keep code well documented.
* Write clean and readable code.
* Test new functionality.

---

## License

This project currently has no license.

---

## Author

Developed by **Ahoura Khajeh Afzali**
