from sqlalchemy import (
    Column, Integer, String, Date, Numeric,
    ForeignKey, TIMESTAMP
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Department(Base):
    __tablename__ = "department"
    __table_args__ = {"schema": "office"}

    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), unique=True, nullable=False)
    location = Column(String(100))

    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employee"
    __table_args__ = {"schema": "office"}

    emp_id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    hire_date = Column(Date, nullable=False)
    dept_id = Column(Integer, ForeignKey("office.department.dept_id"))

    department = relationship("Department", back_populates="employees")


class Salary(Base):
    __tablename__ = "salary"
    __table_args__ = {"schema": "office"}

    salary_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey("office.employee.emp_id"))
    amount = Column(Numeric(12, 2), nullable=False)
    effective_from = Column(Date, nullable=False)
    effective_to = Column(Date)


class Business(Base):
    __tablename__ = "business"
    __table_args__ = {"schema": "office"}

    business_id = Column(Integer, primary_key=True)
    business_name = Column(String(150), nullable=False)
    industry = Column(String(100))
    annual_revenue = Column(Numeric(15, 2))
    created_at = Column(TIMESTAMP, server_default=func.now())