# 📦 Module Documentation

# Hospital Management System (HMS)

---

# 1. Introduction

The Hospital Management System is divided into independent modules, each responsible for a specific business function. This modular architecture improves maintainability, scalability, and code organization by separating concerns into well-defined components.

Each module consists of its own models, services, repositories, routes, and user interface components while interacting seamlessly with other modules through clearly defined APIs and business logic.

---

# 2. Module Overview

The Hospital Management System consists of the following core modules:

| Module                  | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| Authentication          | User login, registration, authorization, and security |
| User Management         | Manage users and role-based access                    |
| Patient Management      | Register and manage patient information               |
| Doctor Management       | Manage doctor profiles and schedules                  |
| Appointment Management  | Book, update, and cancel appointments                 |
| Medical Records         | Store consultation history and patient records        |
| Prescription Management | Generate and manage digital prescriptions             |
| Billing Management      | Generate invoices and manage payments                 |
| Dashboard & Reports     | Display analytics and generate reports                |
| Notification *(Future)* | Email, SMS, and in-app notifications                  |

---

# 3. Authentication Module

## Purpose

Provides secure authentication and authorization for all users.

### Responsibilities

* User Registration
* User Login
* Password Encryption
* JWT Token Generation
* Session Management
* Role-Based Access Control (RBAC)

### Components

* User Model
* Authentication Service
* Authentication Repository
* Authentication Routes

### APIs

* `POST /auth/register`
* `POST /auth/login`
* `POST /auth/logout`
* `GET /auth/profile`
* `PUT /auth/change-password`

---

# 4. User Management Module

## Purpose

Manages common user information shared across all user roles.

### Responsibilities

* User Profile Management
* Role Assignment
* Account Updates
* Password Changes
* User Search

### User Roles

* Administrator
* Doctor
* Patient
* Receptionist

---

# 5. Patient Management Module

## Purpose

Maintains patient information and healthcare history.

### Responsibilities

* Register Patient
* Update Patient Details
* Search Patients
* View Patient Profile
* Manage Medical History

### Main Classes

* Patient
* PatientService
* PatientRepository

### APIs

* `GET /patients`
* `GET /patients/{id}`
* `POST /patients`
* `PUT /patients/{id}`
* `DELETE /patients/{id}`

---

# 6. Doctor Management Module

## Purpose

Maintains doctor profiles, departments, and availability schedules.

### Responsibilities

* Add Doctor
* Update Doctor Information
* Manage Availability
* Assign Departments
* View Doctor Profile

### Main Classes

* Doctor
* DoctorService
* DoctorRepository

### APIs

* `GET /doctors`
* `POST /doctors`
* `PUT /doctors/{id}`
* `DELETE /doctors/{id}`

---

# 7. Appointment Management Module

## Purpose

Coordinates appointment scheduling between patients and doctors.

### Responsibilities

* Book Appointment
* Cancel Appointment
* Reschedule Appointment
* Approve Appointment
* Track Appointment Status

### Appointment Status

* Pending
* Confirmed
* Completed
* Cancelled

### Main Classes

* Appointment
* AppointmentService
* AvailabilityService

### APIs

* `GET /appointments`
* `POST /appointments`
* `PUT /appointments/{id}`
* `DELETE /appointments/{id}`

---

# 8. Medical Records Module

## Purpose

Maintains secure electronic health records (EHR) for every patient.

### Responsibilities

* Store Consultation Notes
* Maintain Medical History
* Link Prescriptions
* Record Diagnoses
* Upload Medical Documents *(Future)*

### Main Classes

* MedicalRecord
* MedicalRecordService

### APIs

* `GET /medical-records/{patient_id}`
* `POST /medical-records`
* `PUT /medical-records/{id}`

---

# 9. Prescription Management Module

## Purpose

Allows doctors to generate and manage digital prescriptions.

### Responsibilities

* Create Prescription
* Update Prescription
* View Prescription History
* Print Prescription

### Main Classes

* Prescription
* PrescriptionService

### APIs

* `POST /prescriptions`
* `GET /prescriptions/{id}`
* `PUT /prescriptions/{id}`

---

# 10. Billing Management Module

## Purpose

Automates invoice generation and payment tracking.

### Responsibilities

* Generate Invoice
* Calculate Consultation Charges
* Add Medicine Charges
* Track Payment Status
* Print Invoice

### Main Classes

* Bill
* BillingService

### APIs

* `GET /billing`
* `POST /billing`
* `PUT /billing/{id}`

---

# 11. Dashboard & Reporting Module

## Purpose

Provides role-specific dashboards and operational reports.

### Dashboards

### Administrator

* Total Patients
* Total Doctors
* Revenue Summary
* Daily Appointments

### Doctor

* Today's Schedule
* Assigned Patients
* Pending Consultations

### Patient

* Upcoming Appointments
* Medical History
* Billing History

### Reports

* Patient Reports
* Appointment Reports
* Revenue Reports
* Doctor Reports

---

# 12. Notification Module *(Future)*

## Purpose

Sends notifications to users about important system events.

### Notification Types

* Appointment Confirmation
* Appointment Reminder
* Prescription Ready
* Payment Confirmation
* Password Reset

### Delivery Channels

* Email
* SMS
* In-App Notifications

---

# 13. Module Dependencies

The modules communicate through clearly defined relationships.

```text
Authentication
       │
       ▼
User Management
       │
       ▼
Patient Management
       │
       ▼
Appointment Management
       │
       ▼
Medical Records
       │
       ▼
Prescription Management
       │
       ▼
Billing Management
       │
       ▼
Reports
```

---

# 14. Module Interaction Diagram

> Replace this placeholder with the final module interaction diagram.

<p align="center">
    <img src="images/module_interaction.png" width="900">
</p>

<p align="center">
<b>Figure 8.1</b> – Module Interaction Diagram
</p>

---

# 15. Module Design Principles

Each module follows the following software engineering principles:

* Single Responsibility Principle (SRP)
* Separation of Concerns (SoC)
* High Cohesion
* Low Coupling
* Object-Oriented Design
* Layered Architecture
* Code Reusability

These principles ensure that modules remain independent, maintainable, and easy to extend.

---

# 16. Future Modules

The modular architecture allows additional features to be integrated without major changes to the existing system.

Planned future modules include:

* Pharmacy Management
* Laboratory Management
* Inventory Management
* Insurance Management
* Payment Gateway Integration
* AI Healthcare Assistant
* Analytics Dashboard
* Telemedicine / Video Consultation
* Mobile Application Support

---

# 17. Module Summary

The Hospital Management System is organized into independent functional modules, each responsible for a specific aspect of hospital operations. This modular design simplifies development, testing, maintenance, and future expansion while ensuring that the system remains scalable and aligned with modern software engineering practices.

Each module is designed to work seamlessly with the others through well-defined APIs and shared business logic, providing a robust foundation for building a production-ready healthcare management application.
