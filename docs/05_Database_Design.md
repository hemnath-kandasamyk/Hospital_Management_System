# 🗄️ Database Design

# Hospital Management System (HMS)

---

# 1. Introduction

The database is the backbone of the Hospital Management System. It is responsible for storing, organizing, and managing all hospital-related information, including users, patients, doctors, appointments, medical records, prescriptions, and billing information.

The database is designed following **Normalization Principles**, ensuring data consistency, integrity, and minimal redundancy.

During development, **SQLite** will be used as the primary database. The architecture is designed to allow seamless migration to **PostgreSQL** for production deployments without major code changes.

---

# 2. Database Objectives

The primary objectives of the database design are:

* Store hospital information securely.
* Maintain relationships between entities.
* Prevent duplicate data.
* Ensure data integrity using constraints.
* Support future scalability.
* Enable efficient querying.
* Simplify maintenance and backups.

---

# 3. Database Management System (DBMS)

| Environment | Database   |
| ----------- | ---------- |
| Development | SQLite     |
| Production  | PostgreSQL |

The application uses **SQLAlchemy ORM**, allowing the business logic to remain independent of the underlying database engine.

---

# 4. Database Architecture

The Hospital Management System consists of multiple interconnected tables.

Major entities include:

* Users
* Patients
* Doctors
* Appointments
* Medical Records
* Prescriptions
* Bills
* Departments

---

## Database Architecture Diagram

> Replace this placeholder with the actual database architecture diagram.

<p align="center">
    <img src="images/database_architecture.png" width="850">
</p>

<p align="center">
<b>Figure 5.1</b> – Database Architecture
</p>

---

# 5. Entity Relationship (ER) Design

The Entity Relationship model defines how different entities interact within the system.

### Relationship Summary

| Entity                   | Relationship |
| ------------------------ | ------------ |
| User → Patient           | One-to-One   |
| User → Doctor            | One-to-One   |
| Patient → Appointment    | One-to-Many  |
| Doctor → Appointment     | One-to-Many  |
| Appointment → Bill       | One-to-One   |
| Patient → Medical Record | One-to-Many  |
| Patient → Prescription   | One-to-Many  |

---

## ER Diagram

> Replace this placeholder with the final ER diagram.

<p align="center">
    <img src="images/er_diagram.png" width="900">
</p>

<p align="center">
<b>Figure 5.2</b> – Entity Relationship Diagram
</p>

---

# 6. Database Tables

---

## 6.1 Users

The `users` table stores authentication and common profile information for all system users.

| Column        | Data Type    | Description                             |
| ------------- | ------------ | --------------------------------------- |
| id            | INTEGER      | Primary Key                             |
| username      | VARCHAR(50)  | Unique username                         |
| email         | VARCHAR(100) | User email                              |
| password_hash | TEXT         | Encrypted password                      |
| role          | VARCHAR(20)  | ADMIN / DOCTOR / PATIENT / RECEPTIONIST |
| created_at    | TIMESTAMP    | Account creation time                   |

---

## 6.2 Patients

Stores patient-specific information.

| Column          | Data Type   | Description              |
| --------------- | ----------- | ------------------------ |
| patient_id      | INTEGER     | Primary Key              |
| user_id         | INTEGER     | Foreign Key → users.id   |
| blood_group     | VARCHAR(5)  | Blood group              |
| date_of_birth   | DATE        | DOB                      |
| contact_number  | VARCHAR(20) | Phone number             |
| address         | TEXT        | Address                  |
| medical_history | TEXT        | Previous medical history |

---

## 6.3 Doctors

Stores doctor information.

| Column         | Data Type    | Description            |
| -------------- | ------------ | ---------------------- |
| doctor_id      | INTEGER      | Primary Key            |
| user_id        | INTEGER      | Foreign Key → users.id |
| specialization | VARCHAR(100) | Medical specialization |
| license_number | VARCHAR(50)  | Medical license        |
| department     | VARCHAR(100) | Assigned department    |
| availability   | TEXT         | Consultation schedule  |

---

## 6.4 Appointments

Stores appointment details.

| Column           | Data Type   | Description                                |
| ---------------- | ----------- | ------------------------------------------ |
| appointment_id   | INTEGER     | Primary Key                                |
| patient_id       | INTEGER     | FK → patients.patient_id                   |
| doctor_id        | INTEGER     | FK → doctors.doctor_id                     |
| appointment_date | DATE        | Appointment date                           |
| appointment_time | TIME        | Appointment time                           |
| status           | VARCHAR(20) | Pending / Approved / Completed / Cancelled |

---

## 6.5 Bills

Stores billing information.

| Column           | Data Type   | Description                      |
| ---------------- | ----------- | -------------------------------- |
| bill_id          | INTEGER     | Primary Key                      |
| appointment_id   | INTEGER     | FK → appointments.appointment_id |
| consultation_fee | DECIMAL     | Consultation charge              |
| medicine_fee     | DECIMAL     | Medicine charge                  |
| total_amount     | DECIMAL     | Final bill                       |
| payment_status   | VARCHAR(20) | Paid / Pending                   |

---

# 7. Database Relationships

The following relationships exist between tables.

```text
Users
 │
 ├──────── Patient (1 : 1)
 │
 └──────── Doctor (1 : 1)

Patient
 │
 ├──────── Appointments (1 : N)
 │
 ├──────── Medical Records (1 : N)
 │
 └──────── Prescriptions (1 : N)

Doctor
 │
 └──────── Appointments (1 : N)

Appointment
 │
 └──────── Bill (1 : 1)
```

---

# 8. Sample Database Schema (SQL)

## Users Table

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Patients Table

```sql
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    blood_group VARCHAR(5),
    date_of_birth DATE,
    contact_number VARCHAR(20),
    address TEXT,
    medical_history TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
```

---

## Doctors Table

```sql
CREATE TABLE doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    specialization VARCHAR(100),
    license_number VARCHAR(50),
    department VARCHAR(100),
    availability TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
```

---

## Appointments Table

```sql
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'PENDING',
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
);
```

---

## Bills Table

```sql
CREATE TABLE bills (
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER UNIQUE NOT NULL,
    consultation_fee DECIMAL(10,2),
    medicine_fee DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    payment_status VARCHAR(20) DEFAULT 'PENDING',
    FOREIGN KEY(appointment_id) REFERENCES appointments(appointment_id)
);
```

---

# 9. Database Constraints

The following constraints are enforced:

* Primary Keys for unique identification.
* Foreign Keys for referential integrity.
* UNIQUE constraints for usernames and emails.
* NOT NULL constraints for mandatory fields.
* Default values for status fields.
* Cascading updates/deletes (where appropriate).

---

# 10. Future Database Enhancements

Future versions of the system may introduce additional tables such as:

* Departments
* Pharmacy
* Laboratory
* Inventory
* Notifications
* Audit Logs
* Insurance Claims
* Online Payments

The schema has been designed to support these modules with minimal structural changes.

---

# 11. Database Design Summary

The Hospital Management System database follows a normalized, relational design that ensures data consistency, scalability, and maintainability. By using SQLAlchemy as the ORM layer, the application remains database-independent, allowing easy migration from SQLite to PostgreSQL while preserving the same object-oriented business logic.
