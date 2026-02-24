import random
from faker import Faker
from db_connection import get_connection

fake = Faker()

def load_sample_data():
    conn = get_connection()
    cursor = conn.cursor()

    # -------------------------
    # 1️⃣ Insert Departments (100)
    # -------------------------
    departments = []

    for _ in range(100):
        dept_name = fake.unique.company()
        location = fake.city()

        cursor.execute("""
            INSERT INTO office.department (dept_name, location)
            VALUES (%s, %s)
            ON CONFLICT (dept_name) DO NOTHING
            RETURNING dept_id;
        """, (dept_name, location))

        result = cursor.fetchone()
        if result:
            departments.append(result[0])

    # Fetch all department IDs (in case some existed)
    cursor.execute("SELECT dept_id FROM office.department;")
    departments = [row[0] for row in cursor.fetchall()]

    # -------------------------
    # 2️⃣ Insert Employees (100)
    # -------------------------
    employees = []

    for _ in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        dept_id = random.choice(departments)

        cursor.execute("""
            INSERT INTO office.employee
            (first_name, last_name, email, hire_date, dept_id)
            VALUES (%s, %s, %s, CURRENT_DATE, %s)
            ON CONFLICT (email) DO NOTHING
            RETURNING emp_id;
        """, (first_name, last_name, email, dept_id))

        result = cursor.fetchone()
        if result:
            employees.append(result[0])

    # Fetch all employee IDs
    cursor.execute("SELECT emp_id FROM office.employee;")
    employees = [row[0] for row in cursor.fetchall()]

    # -------------------------
    # 3️⃣ Insert Salary Records (100)
    # -------------------------
    for _ in range(100):
        emp_id = random.choice(employees)
        amount = round(random.uniform(30000, 150000), 2)

        cursor.execute("""
            INSERT INTO office.salary
            (emp_id, amount, effective_from)
            VALUES (%s, %s, CURRENT_DATE);
        """, (emp_id, amount))

    # -------------------------
    # 4️⃣ Insert Business Records (100)
    # -------------------------
    for _ in range(100):
        business_name = fake.company()
        industry = fake.job()
        revenue = round(random.uniform(1_000_000, 50_000_000), 2)

        cursor.execute("""
            INSERT INTO office.business
            (business_name, industry, annual_revenue)
            VALUES (%s, %s, %s);
        """, (business_name, industry, revenue))

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ 100 dummy rows inserted into each table successfully.")


if __name__ == "__main__":
    load_sample_data()