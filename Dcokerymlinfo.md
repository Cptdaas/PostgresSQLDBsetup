# Docker Compose + PostgreSQL + DBeaver (Simplified Guide with Architecture)

---

# 1. What is `docker-compose.yml`?

`docker-compose.yml` is a configuration file that defines your entire container-based system in one place.

Instead of running long Docker commands manually, you describe your infrastructure in a readable YAML file.

This approach is called:

**Infrastructure as Code (IaC)**

It allows you to:

* Recreate the same setup anytime
* Share configuration with teammates
* Version control your infrastructure
* Start or stop entire systems with one command

---

# 2. Local Development Architecture

## Visual Architecture

![Local Docker PostgreSQL Architecture](https://miro.medium.com/max/1400/1*JrYqF9Xqk9u5lHppZArYDQ.png)

### Flow Explanation

DBeaver (Client)
↓
localhost:5432 (Port Mapping)
↓
Docker Container (PostgreSQL Server)
↓
Docker Volume (Persistent Storage)

Even on localhost, this follows a real client–server architecture.

---

# 3. Updated `docker-compose.yml` (Your Configuration)

```yaml
version: '3.9'

services:
  postgres:
    image: postgres:15
    container_name: cptdaas-postgres
    environment:
      POSTGRES_USER: cptdaas
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

# 4. Line-by-Line Explanation (Based on Your YAML)

## version: '3.9'

Defines the Docker Compose configuration schema version.

---

## services:

Each service represents one container.

Here you define one service:

`postgres`

Later you can extend this with additional services like backend, redis, or pgadmin.

---

## image: postgres:15

Pulls official PostgreSQL version 15 from Docker Hub.

---

## container_name: cptdaas-postgres

Gives your container a clear, custom name.

Instead of random container IDs, Docker will use:

`cptdaas-postgres`

This makes container management cleaner.

---

## environment:

These variables initialize PostgreSQL when the container starts for the first time.

* POSTGRES_USER → cptdaas
* POSTGRES_PASSWORD → 1234
* POSTGRES_DB → mydb

These credentials will be used when connecting from DBeaver.

---

## ports:

"5432:5432"

Format:
HostPort : ContainerPort

This maps:

localhost:5432 → PostgreSQL inside container

This allows DBeaver to connect using localhost.

---

## volumes:

postgres_data:/var/lib/postgresql/data

PostgreSQL stores its internal data at:

/var/lib/postgresql/data

The named volume `postgres_data` ensures:

* Data persists even if container is removed
* Storage is separated from container lifecycle
* Your database is not deleted accidentally

---

# 5. How to Start the System

Navigate to your project directory and run:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

You should see:

`cptdaas-postgres` running on port 5432

---

# 6. Connect Using DBeaver

![DBeaver PostgreSQL Connection](https://dbeaver.com/docs/wiki/images/Database-Connection-Dialog.png)

Connection Settings:

Host: localhost
Port: 5432
Database: mydb
Username: cptdaas
Password: 1234

Click Test Connection → Finish.

---

# 7. Stop or Remove the System

Stop container:

```bash
docker compose down
```

Remove container + delete database permanently:

```bash
docker compose down -v
```

Be careful with `-v` because it deletes the `postgres_data` volume.

---

# 8. Summary

Your updated setup now:

* Uses container name: `cptdaas-postgres`
* Uses user: `cptdaas`
* Uses database: `mydb`
* Uses volume: `postgres_data`

This file acts as a blueprint of your database infrastructure.

With one command, you can recreate your PostgreSQL server anytime.

You are not just running a database.

You are defining infrastructure in a reproducible, controlled way.

---

End of Updated Document.
