# Alembic Database Migration Setup

## Overview

This branch introduces **Alembic-based database migrations** using SQLAlchemy models.

The goal is to replace manual schema creation scripts with a version-controlled, production-ready migration workflow.

Alembic enables controlled schema evolution without dropping or recreating tables.

---

## Why Alembic?

Manual schema scripts are suitable for initial setup, but they do not handle:

* Incremental schema changes
* Version tracking
* Safe production upgrades
* Team-based development workflows

Alembic solves this by:

* Tracking schema versions
* Generating migration scripts
* Applying upgrades and downgrades safely
* Maintaining a migration history table (`alembic_version`)

---

## Project Structure (Migration-Based)

```
PostgresSQLDBsetup/
│
├── alembic/
│   ├── env.py
│   ├── versions/
│   └── script.py.mako
│
├── alembic.ini
├── models.py
├── config.py
├── docker-compose.yml
├── requirements.txt
└── README_Alembic_Migrations.md
```

---

## Prerequisites

Activate virtual environment:

```
source venv/bin/activate
```

Install dependencies:

```
pip install sqlalchemy alembic psycopg2-binary
```

---

## Database Connection Configuration

Update `alembic.ini`:

```
sqlalchemy.url = postgresql+psycopg2://cptdaas:1234@localhost:5432/mydb
```

For production use, environment variables are recommended instead of hardcoded credentials.

---

## Link Alembic to SQLAlchemy Models

In `alembic/env.py`, ensure:

```python
from models import Base

target_metadata = Base.metadata
```

If using custom schema (e.g., `office`), update configuration:

```python
context.configure(
    connection=connection,
    target_metadata=target_metadata,
    include_schemas=True,
    compare_type=True,
    compare_server_default=True
)
```

---

## Initial Migration

Generate first migration:

```
alembic revision --autogenerate -m "Initial schema"
```

Apply migration:

```
alembic upgrade head
```

This creates all tables defined in `models.py`.

---

## Applying Schema Changes

1. Modify `models.py`
2. Generate migration:

```
alembic revision --autogenerate -m "Describe change"
```

3. Apply migration:

```
alembic upgrade head
```

---

## Downgrading

Revert last migration:

```
alembic downgrade -1
```

Downgrade to specific version:

```
alembic downgrade <revision_id>
```

---

## Checking Migration History

View current version applied in database:

```
alembic current
```

View migration history:

```
alembic history
```

---

## Migration Flow Summary

1. Define schema in `models.py`
2. Autogenerate migration script
3. Review generated migration file
4. Apply migration to database
5. Version tracked in `alembic_version` table

---

## When to Use Alembic

Recommended for:

* Production systems
* API backends
* Multi-developer environments
* Evolving schemas
* CI/CD deployment pipelines

Not necessary for:

* One-time experimental scripts
* Static databases

---

## Future Improvements

* Integrate with FastAPI
* Use environment-based configuration
* Add CI pipeline to run migrations automatically
* Deploy with AWS RDS

---

## Status

Alembic successfully integrated for controlled schema versioning and production-grade database management.



* Schema: `office`
* Tables:

  * department
  * employee
  * salary
  * business

---
<p align="center">
  <img src="mydb - mydb - office.png" 
       alt="Hierarchical Navigable Small World (HNSW) Diagram" 
       width="800"
       height="500"/>
</p>
