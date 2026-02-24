from db_connection import get_connection

def create_schema_and_tables():
    conn = get_connection()
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("CREATE SCHEMA IF NOT EXISTS office;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS office.department (
            dept_id SERIAL PRIMARY KEY,
            dept_name VARCHAR(100) UNIQUE NOT NULL,
            location VARCHAR(100)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS office.employee (
            emp_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            hire_date DATE NOT NULL,
            dept_id INT REFERENCES office.department(dept_id)
                ON DELETE SET NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS office.salary (
            salary_id SERIAL PRIMARY KEY,
            emp_id INT REFERENCES office.employee(emp_id)
                ON DELETE CASCADE,
            amount NUMERIC(12,2) NOT NULL,
            effective_from DATE NOT NULL,
            effective_to DATE
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS office.business (
            business_id SERIAL PRIMARY KEY,
            business_name VARCHAR(150) NOT NULL,
            industry VARCHAR(100),
            annual_revenue NUMERIC(15,2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    print("Schema and tables created successfully.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_schema_and_tables()