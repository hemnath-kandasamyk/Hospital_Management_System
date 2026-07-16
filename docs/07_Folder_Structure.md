# 📁 Project Folder Structure

# Hospital Management System (HMS)

---

# 1. Introduction

A well-organized folder structure is essential for developing scalable, maintainable, and production-ready software.

The Hospital Management System follows a **modular project architecture**, where each directory has a single responsibility. This separation improves code readability, simplifies debugging, and allows multiple developers to work on different modules simultaneously.

The project is organized according to modern Python and Flask development practices.

---

# 2. Complete Project Structure

```text
Hospital_Management_System/
│
├── app/
│   ├── __init__.py               # Flask Application Factory
│   ├── main.py                   # Application Entry (optional)
│   │
│   ├── models/                   # SQLAlchemy ORM Models
│   │   ├── user.py
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   ├── appointment.py
│   │   ├── billing.py
│   │   └── __init__.py
│   │
│   ├── services/                 # Business Logic
│   │   ├── auth_service.py
│   │   ├── patient_service.py
│   │   ├── doctor_service.py
│   │   ├── appointment_service.py
│   │   ├── billing_service.py
│   │   └── __init__.py
│   │
│   ├── repositories/             # Database Access Layer
│   │   ├── user_repository.py
│   │   ├── patient_repository.py
│   │   ├── doctor_repository.py
│   │   ├── appointment_repository.py
│   │   └── __init__.py
│   │
│   ├── routes/                   # Flask Blueprints / REST APIs
│   │   ├── auth_routes.py
│   │   ├── patient_routes.py
│   │   ├── doctor_routes.py
│   │   ├── appointment_routes.py
│   │   ├── billing_routes.py
│   │   └── __init__.py
│   │
│   ├── database/
│   │   ├── db.py                 # Database Configuration
│   │   ├── seed.py               # Sample Data
│   │   └── migrations/
│   │
│   ├── utils/                    # Utility Functions
│   │   ├── validators.py
│   │   ├── helpers.py
│   │   ├── constants.py
│   │   └── logger.py
│   │
│   ├── config/
│   │   ├── development.py
│   │   ├── production.py
│   │   ├── testing.py
│   │   └── __init__.py
│   │
│   ├── templates/                # HTML Templates
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── icons/
│   │
│   └── extensions.py             # Flask Extensions
│
├── docs/                         # Project Documentation
│   ├── images/
│   ├── diagrams/
│   └── *.md
│
├── tests/                        # Unit & Integration Tests
│   ├── test_auth.py
│   ├── test_patient.py
│   ├── test_doctor.py
│   ├── test_appointment.py
│   └── test_billing.py
│
├── instance/                     # Local Database (SQLite)
│
├── .env                          # Environment Variables
├── .gitignore
├── config.py                     # Global Configuration
├── requirements.txt              # Python Dependencies
├── run.py                        # Application Entry Point
├── README.md
└── LICENSE
```

---

# 3. Folder Responsibilities

## app/

The `app/` directory contains the entire application source code.

It includes:

* Models
* Services
* Routes
* Database configuration
* Utilities
* Templates
* Static assets

This is the core of the Hospital Management System.

---

## models/

The `models/` directory contains all SQLAlchemy model classes representing database entities.

Examples:

* User
* Patient
* Doctor
* Appointment
* Billing

Each model maps directly to a database table.

---

## services/

The `services/` directory contains the application's business logic.

Responsibilities include:

* Appointment scheduling
* Billing calculations
* Authentication
* Validation
* Report generation

The service layer acts as the bridge between API routes and the database.

---

## repositories/

The repository layer is responsible for database operations.

Responsibilities:

* Create records
* Read records
* Update records
* Delete records

This abstraction keeps SQLAlchemy queries out of the business logic.

---

## routes/

The `routes/` directory defines all REST API endpoints using Flask Blueprints.

Examples:

* Authentication APIs
* Patient APIs
* Doctor APIs
* Appointment APIs
* Billing APIs

Each route delegates business logic to the corresponding service.

---

## database/

The `database/` directory contains database-related components.

Includes:

* Database initialization
* SQLAlchemy configuration
* Database migrations
* Seed scripts

---

## utils/

The `utils/` directory stores reusable helper functions.

Examples:

* Input validation
* Logging
* Constants
* Utility methods
* Date formatting

---

## config/

This folder contains environment-specific configuration files.

Configurations include:

* Development
* Testing
* Production

This approach keeps configuration separate from application code.

---

## templates/

Contains all HTML templates rendered by Flask.

Examples:

* Login Page
* Dashboard
* Patient Registration
* Appointment Booking
* Billing

---

## static/

Stores static assets required by the frontend.

Includes:

* CSS
* JavaScript
* Images
* Icons
* Fonts

---

## docs/

Contains all project documentation.

Examples:

* Project Overview
* Software Requirements
* System Architecture
* API Documentation
* Database Design

This folder also stores diagrams and images referenced by the Markdown files.

---

## tests/

Contains automated tests for the application.

Types of tests include:

* Unit Tests
* Integration Tests
* API Tests

Testing helps ensure application reliability as the project grows.

---

# 4. Application Workflow

The application processes requests through the following flow.

```text
Browser
    │
    ▼
Flask Route
    │
    ▼
Service Layer
    │
    ▼
Repository Layer
    │
    ▼
Database
```

This layered workflow keeps responsibilities separated and simplifies maintenance.

---

# 5. Folder Structure Diagram

> Replace this placeholder with the folder structure diagram.

<p align="center">
    <img src="images/folder_structure.png" width="900">
</p>

<p align="center">
<b>Figure 7.1</b> – Project Folder Structure
</p>

---

# 6. Design Principles

The folder structure is designed according to the following principles:

* Separation of Concerns (SoC)
* Single Responsibility Principle (SRP)
* Modular Development
* Code Reusability
* Scalability
* Maintainability
* Testability

These principles ensure that each module has a clearly defined purpose and can evolve independently.

---

# 7. Benefits of This Structure

Using this project organization provides several advantages:

* Easy navigation through the codebase.
* Clear separation between presentation, business logic, and data access.
* Simplified debugging and testing.
* Improved collaboration in team environments.
* Easier integration of new modules.
* Better support for future deployment and scaling.

---

# 8. Future Expansion

The modular design allows new features to be added without major restructuring.

Planned future modules include:

* Pharmacy Management
* Laboratory Management
* Inventory Management
* Payment Gateway
* Notification Service
* AI Healthcare Assistant
* Analytics Dashboard
* Machine Learning Services
* Docker Configuration
* CI/CD Pipelines

---

# 9. Folder Structure Summary

The Hospital Management System follows a clean, modular, and production-ready folder structure based on modern Flask application architecture. Each directory has a clearly defined responsibility, making the project easier to understand, maintain, test, and extend.

This organization supports both individual learning and collaborative software development while providing a strong foundation for building enterprise-grade Python applications.
