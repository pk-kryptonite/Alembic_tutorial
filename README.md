# SQLAlchemy Models and Alembic Migrations

This guide provides instructions for setting up SQLAlchemy models and managing database migrations using Alembic. It covers the initialisation, upgrading, downgrading, and rolling back of migrations.
Hopefully this helps someone who needs a quick tutorial on alembic.

## Prerequisites

- Python 3.x
- SQLAlchemy
- Alembic
- MariaDB (or MySQL) with `mysqlclient` or `mysql-connector-python`

## Setup

### 1. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```
### 2. run migrations

create migration environment:

```bash
alembic init migrations
```

Configure Alembic:

[alembic]
sqlalchemy.url = mysql+mysqlclient://user:password@localhost/dbname

create init migrations:

```bash
alembic revision --autogenerate -m "Initial migration"

```

apply migrations:

```bash
alembic upgrade head
```

Downgrade or Roll Back Migrations:

```bash
alembic downgrade <revision>
alembic downgrade -1 (NB: relative identify from current migration)
```
