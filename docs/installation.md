# Installation

This document explains how to set up a local development environment for the Notebook project.

> **Project Status**
>
> Notebook is currently under active development. Installation steps may change as the project evolves. Always refer to the latest version of this document when setting up a new development environment.

---

# Table of Contents

- Prerequisites
- Supported Platforms
- Clone the Repository
- Create a Virtual Environment
- Install Dependencies
- Configure Environment Variables
- Database Configuration
- Apply Database Migrations
- Create a Superuser
- Collect Static Files
- Run the Development Server
- Verify Installation
- Common Development Commands
- Troubleshooting

---

# Prerequisites

Before installing Notebook, ensure the following software is available on your system.

| Software | Recommended Version |
|------------|--------------------|
| Python | 3.12+ |
| pip | Latest |
| Git | Latest |
| PostgreSQL | 16+ (Recommended) |
| SQLite | Built into Python (Development Only) |

Optional:

- Docker
- Redis (future support)
- Nginx (production)
- Gunicorn (production)

---

# Supported Platforms

Notebook is primarily developed on Linux but also supports:

- Linux
- Windows
- macOS

---

# Clone the Repository

Clone the repository using Git.

```bash
git clone https://github.com/AhouraKhAfzali/notebook.git
```

Navigate into the project.

```bash
cd notebook
```

---

# Create a Virtual Environment

Creating an isolated Python environment is highly recommended.

```bash
python -m venv .venv
```

Activate it.

### Linux

```bash
source .venv/bin/activate
```

### macOS

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

---

# Install Dependencies

Upgrade pip.

```bash
python -m pip install --upgrade pip
```

Install project dependencies.

```bash
pip install -r requirements.txt
```

Depending on the current project version, additional development packages may also be installed.

---

# Configure Environment Variables

Notebook uses environment variables for sensitive configuration.

Create a new file in the project root.

```
.env
```

Example configuration:

```env
SECRET_KEY=your-secret-key

DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

DATABASE_ENGINE=django.db.backends.sqlite3

DATABASE_NAME=db.sqlite3

DATABASE_USER=

DATABASE_PASSWORD=

DATABASE_HOST=

DATABASE_PORT=
```

For PostgreSQL:

```env
DATABASE_ENGINE=django.db.backends.postgresql

DATABASE_NAME=notebook

DATABASE_USER=postgres

DATABASE_PASSWORD=your_password

DATABASE_HOST=localhost

DATABASE_PORT=5432
```

---

# Database Configuration

## SQLite

SQLite is recommended for local development.

No additional setup is required.

---

## PostgreSQL

Create a database.

```sql
CREATE DATABASE notebook;
```

Create a user.

```sql
CREATE USER notebook_user WITH PASSWORD 'your_password';
```

Grant privileges.

```sql
GRANT ALL PRIVILEGES ON DATABASE notebook TO notebook_user;
```

Update your `.env` accordingly.

---

# Apply Database Migrations

Run Django migrations.

```bash
python manage.py migrate
```

This will create all required database tables.

---

# Create an Administrator Account

Create a superuser.

```bash
python manage.py createsuperuser
```

Follow the interactive prompts.

---

# Collect Static Files

Although not required during development, static files should be collected before production deployment.

```bash
python manage.py collectstatic
```

---

# Run the Development Server

Start Django.

```bash
python manage.py runserver
```

The development server will be available at:

```
http://127.0.0.1:8000/
```

---

# Verify Installation

After starting the server, verify that:

- The homepage loads correctly.
- Static files are served.
- The admin panel is accessible.
- Authentication functions correctly.
- Database migrations completed successfully.

Access the Django administration panel.

```
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials created earlier.

---

# Common Development Commands

Run migrations.

```bash
python manage.py migrate
```

Create new migrations.

```bash
python manage.py makemigrations
```

Create a superuser.

```bash
python manage.py createsuperuser
```

Run the development server.

```bash
python manage.py runserver
```

Collect static files.

```bash
python manage.py collectstatic
```

Run Django shell.

```bash
python manage.py shell
```

Run tests.

```bash
python manage.py test
```

---

# Recommended Development Workflow

1. Pull the latest changes.

```bash
git pull
```

2. Activate the virtual environment.

3. Install any new dependencies.

```bash
pip install -r requirements.txt
```

4. Apply database migrations.

```bash
python manage.py migrate
```

5. Start the development server.

---

# Troubleshooting

### ModuleNotFoundError

Install project dependencies.

```bash
pip install -r requirements.txt
```

---

### Migration Errors

Delete unapplied migration files only if you understand the consequences.

Then execute:

```bash
python manage.py makemigrations

python manage.py migrate
```

---

### Static Files Not Loading

Verify:

- `STATIC_URL`
- `STATICFILES_DIRS`
- `collectstatic`
- Browser cache

---

### Database Connection Failed

Check:

- Database server is running.
- Credentials in `.env`.
- PostgreSQL permissions.
- Database name.

---

### SECRET_KEY Error

Ensure the `.env` file exists and contains a valid secret key.

---

### Port Already in Use

Run Django on another port.

```bash
python manage.py runserver 8001
```

---

# Updating an Existing Installation

Pull the latest changes.

```bash
git pull
```

Install updated dependencies.

```bash
pip install -r requirements.txt
```

Apply migrations.

```bash
python manage.py migrate
```

Restart the development server.

---

# Next Steps

After successfully installing Notebook, continue with the following documentation:

- `architecture.md`
- `apps.md`