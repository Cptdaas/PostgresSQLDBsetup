# PostgreSQL Docker Setup with Python Schema Management

## 📌 Project Overview

This project demonstrates how to:

* Run PostgreSQL using Docker Compose
* Connect using DBeaver (DB client)
* Create schema and tables using Python
* Load dummy relational data
* Maintain clean project structure with virtual environment support

The setup follows Infrastructure as Code principles and modular Python design.

---

## 🏗 Architecture

Local Development Flow:

DBeaver (Client)
→ localhost:5432
→ Docker Container (PostgreSQL 15)
→ Docker Volume (Persistent Storage)

Database Structure:

Database: `mydb`
Schema: `office`
Tables:

* department
* employee
* salary
* business

---

## 📂 Project Structure

```
PostgresSQLDBsetup/
│
├── docker-compose.yml
├── config.py
├── db_connection.py
├── create_schema.py
├── load_data.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🐳 Docker Setup

### 1️⃣ Start PostgreSQL

```bash
docker compose up -d
```

### 2️⃣ Check Running Container

```bash
docker ps
```

Container Name:

```
cptdaas-postgres
```

### 3️⃣ Stop Container

```bash
docker compose down
```

Remove container and volume (Deletes all data):

```bash
docker compose down -v
```

---

## 🔌 Database Connection (DBeaver)

Connection Configuration:

Host: `localhost`
Port: `5432`
Database: `mydb`
Username: `cptdaas`
Password: `1234`

---

## 🐍 Python Setup

### 1️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not created yet:

```bash
pip freeze > requirements.txt
```

---

## 🏗 Create Schema and Tables

```bash
python create_schema.py
```

Creates:

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

## 📊 Load Dummy Data (100 Rows Each)

```bash
python load_data.py
```

Populates:

* 100 departments
* 100 employees
* 100 salary records
* 100 business records

---

## 🧪 Verify Data

Run in DBeaver:

```sql
SELECT COUNT(*) FROM office.department;
SELECT COUNT(*) FROM office.employee;
SELECT COUNT(*) FROM office.salary;
SELECT COUNT(*) FROM office.business;
```

---

## 🧠 Technology Stack

* PostgreSQL 15
* Docker & Docker Compose
* Python 3
* psycopg2
* Faker (dummy data generation)
* DBeaver

---

## 🚀 Future Enhancements

* SQLAlchemy ORM integration
* Alembic database migrations
* FastAPI backend integration
* AWS deployment (EC2 or RDS)
* CI/CD automation

---

## 📌 Notes

* Docker handles database isolation.
* Virtual environment isolates Python dependencies.
* Schema is modular and safe to re-run.
* Volume ensures persistent database storage.

---

## ✅ Status

Local PostgreSQL containerized environment successfully running with schema management


<!-- file name :mydb - mydb - office.png -->
