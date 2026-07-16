# 📋 Software Requirements Specification (SRS)

# Hospital Management System (HMS)

---

# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the **Hospital Management System (HMS)**.

The purpose of this document is to provide a clear understanding of the system's capabilities, expected behavior, constraints, and quality requirements before implementation begins.

This document serves as a reference for developers, testers, project contributors, and future maintainers.

---

## 1.2 Project Scope

The Hospital Management System is designed to digitize and automate hospital operations, replacing manual paperwork with a secure and centralized software platform.

The system manages the complete patient lifecycle including:

* Patient Registration
* Doctor Management
* Appointment Scheduling
* Consultation Management
* Medical Records
* Billing
* Authentication
* Administrative Operations
* Reporting

The application is designed using Python Object-Oriented Programming principles and follows a modular software architecture to support future expansion.

---

# 2. Functional Requirements (FR)

Functional requirements describe the features and services provided by the system.

---

## FR-1 User Authentication & Authorization

The system shall provide secure user authentication and role-based authorization.

### Features

* User Registration
* Secure Login
* Logout
* Password Encryption
* Forgot Password (Future Enhancement)
* Role-Based Access Control (RBAC)
* Session Management

### Supported Roles

* Administrator
* Doctor
* Receptionist
* Patient

---

## FR-2 Patient Management

The system shall allow hospital staff to manage patient information.

### Features

* Register New Patient
* View Patient Details
* Update Patient Information
* Delete Patient Record
* Search Patients
* Patient Medical History
* Patient Profile Management

---

## FR-3 Doctor Management

The system shall manage doctor information and availability.

### Features

* Add Doctor
* Update Doctor Profile
* Remove Doctor
* View Doctor Information
* Manage Doctor Schedule
* View Assigned Patients

---

## FR-4 Appointment Management

The system shall manage appointments between patients and doctors.

### Features

* Book Appointment
* Cancel Appointment
* Reschedule Appointment
* View Appointment Status
* Doctor Approval
* Appointment History

---

## FR-5 Consultation Management

The system shall allow doctors to record consultation details.

### Features

* Record Diagnosis
* Add Clinical Notes
* Upload Medical Observations
* Record Follow-up Recommendations

---

## FR-6 Prescription Management

Doctors shall be able to create digital prescriptions.

### Features

* Generate Prescription
* Update Prescription
* View Prescription History
* Print Prescription

---

## FR-7 Electronic Health Records (EHR)

The system shall maintain secure electronic medical records.

### Features

* Store Patient History
* Consultation Records
* Diagnoses
* Prescriptions
* Laboratory Reports (Future)
* Medical Documents

---

## FR-8 Billing System

The system shall generate patient invoices automatically.

### Features

* Generate Invoice
* Service-Based Billing
* Medicine Charges
* Consultation Charges
* Payment Status
* Billing History
* Invoice Download

---

## FR-9 Dashboard

The system shall provide dashboards for different users.

### Administrator Dashboard

* Total Patients
* Total Doctors
* Today's Appointments
* Revenue Overview

### Doctor Dashboard

* Today's Appointments
* Assigned Patients
* Consultation Summary

### Reception Dashboard

* Patient Queue
* Appointment Schedule
* Billing Status

---

## FR-10 Reports

The system shall generate reports.

Examples include:

* Patient Reports
* Doctor Reports
* Revenue Reports
* Appointment Reports
* Daily Reports
* Monthly Reports

---

# 3. Non-Functional Requirements (NFR)

Non-functional requirements define the quality attributes of the system.

---

## NFR-1 Performance

The system should provide fast response times.

Requirements:

* API response time below **200 milliseconds** for standard operations.
* Database queries optimized using indexing.
* Efficient memory utilization.

---

## NFR-2 Scalability

The architecture should support future growth.

Requirements:

* Modular application design.
* Easy migration from SQLite to PostgreSQL.
* Support for REST APIs.
* Future cloud deployment compatibility.

---

## NFR-3 Security

The system shall protect sensitive healthcare information.

Requirements:

* Password hashing using **Bcrypt**
* Secure authentication
* Role-Based Access Control (RBAC)
* Input validation
* SQL Injection prevention
* Cross-Site Scripting (XSS) prevention
* Secure session management

Future Enhancements:

* Multi-factor Authentication (MFA)
* JWT Authentication
* OAuth Integration

---

## NFR-4 Reliability

The system should be dependable.

Requirements:

* Target availability of **99.9% uptime**
* Automatic error handling
* Transaction consistency
* Data integrity

---

## NFR-5 Maintainability

The project shall follow clean software engineering practices.

Requirements:

* Modular architecture
* Clean folder structure
* Object-Oriented Programming
* Reusable components
* Comprehensive documentation
* Unit testing support

---

## NFR-6 Usability

The application should provide an intuitive user experience.

Requirements:

* Simple navigation
* Responsive interface
* Easy appointment booking
* Minimal learning curve
* Clear error messages

---

## NFR-7 Compatibility

The application should operate across modern platforms.

Supported Platforms:

* Windows
* Linux
* macOS

Supported Browsers:

* Google Chrome
* Microsoft Edge
* Mozilla Firefox
* Safari

---

## NFR-8 Availability

The application should remain accessible whenever required.

Requirements:

* Continuous service availability
* Reliable database access
* Backup and recovery support

---

# 4. System Constraints

The first release of the project will operate under the following constraints.

* SQLite will be used as the primary database.
* Flask will serve as the backend framework.
* The frontend will be developed using HTML, CSS, and JavaScript.
* Internet connectivity is required for web deployment.
* User authentication is mandatory for accessing protected modules.

---

# 5. Assumptions

The following assumptions are considered during development.

* Users possess valid login credentials.
* Doctors maintain accurate schedules.
* Patients provide correct personal information.
* Hospital staff are trained to use the application.
* The database server remains available during normal operations.

---

# 6. Future Requirements

Future versions of the Hospital Management System may include:

* Pharmacy Management
* Laboratory Management
* Inventory Management
* Online Payments
* Email Notifications
* SMS Notifications
* Video Consultation
* AI Healthcare Assistant
* Machine Learning Disease Prediction
* Analytics Dashboard
* Mobile Application
* Cloud Database Support
* Multi-Hospital Management

---

# 7. Success Criteria

The Hospital Management System will be considered successful if it achieves the following:

* Efficient patient registration and management.
* Secure authentication and authorization.
* Accurate appointment scheduling.
* Reliable medical record management.
* Automated billing and invoice generation.
* Scalable and maintainable software architecture.
* Clean, reusable Object-Oriented code.
* Complete project documentation.
* Portfolio-ready GitHub repository demonstrating professional software engineering practices.
