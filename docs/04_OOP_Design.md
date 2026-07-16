# 🏛️ Object-Oriented Design (OOD)

# Hospital Management System (HMS)

---

# 1. Introduction

The Hospital Management System is designed using **Object-Oriented Programming (OOP)** principles to create a modular, maintainable, and scalable application.

Each real-world entity within the hospital is represented as an independent Python class. These classes encapsulate both the data (attributes) and the behavior (methods) associated with the entity.

The design emphasizes code reusability, separation of concerns, and extensibility, allowing new modules and features to be added with minimal changes to the existing codebase.

---

# 2. Object-Oriented Design Goals

The primary goals of the object-oriented design are:

* Represent real-world hospital entities as Python objects.
* Promote reusable and maintainable code.
* Separate business logic from presentation and data access layers.
* Reduce code duplication through inheritance.
* Protect sensitive information using encapsulation.
* Provide a flexible architecture for future enhancements.

---

# 3. Class Hierarchy

The Hospital Management System follows a hierarchical class structure where common functionality is inherited from a base class while specialized classes implement additional behaviors.

```text
                        User
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
     Patient                           Doctor
        │
        │
    Appointment
```

The design uses:

* **Inheritance** for common user functionality.
* **Composition** for relationships between entities such as appointments, prescriptions, and billing records.

---

# 4. Core Classes

## 4.1 User (Base Class)

The `User` class serves as the foundation for all authenticated users in the system.

### Responsibilities

* User authentication
* Profile management
* Common user information
* Role management

### Attributes

| Attribute     | Description                                      |
| ------------- | ------------------------------------------------ |
| id            | Unique user identifier                           |
| username      | Login username                                   |
| password_hash | Encrypted password                               |
| email         | Registered email address                         |
| role          | User role (Admin, Doctor, Patient, Receptionist) |

### Methods

| Method            | Description                      |
| ----------------- | -------------------------------- |
| verify_password() | Validates user credentials       |
| get_profile()     | Returns user profile information |
| update_profile()  | Updates user information         |
| change_password() | Changes the user's password      |

---

## 4.2 Patient (Inherits User)

The `Patient` class represents hospital patients.

### Responsibilities

* Store patient information
* Maintain medical history
* Track appointments
* Manage prescriptions

### Attributes

| Attribute       | Description              |
| --------------- | ------------------------ |
| blood_group     | Patient blood type       |
| dob             | Date of birth            |
| medical_history | Previous medical records |
| contact_number  | Patient phone number     |
| address         | Residential address      |

### Methods

| Method                 | Description               |
| ---------------------- | ------------------------- |
| view_medical_history() | Displays patient history  |
| book_appointment()     | Creates a new appointment |
| cancel_appointment()   | Cancels an appointment    |
| view_prescriptions()   | Displays prescriptions    |

---

## 4.3 Doctor (Inherits User)

The `Doctor` class represents healthcare professionals.

### Responsibilities

* Manage consultations
* Handle appointments
* Generate prescriptions
* Record diagnoses

### Attributes

| Attribute      | Description                     |
| -------------- | ------------------------------- |
| specialization | Medical specialization          |
| license_no     | Medical license number          |
| availability   | Available consultation schedule |
| department     | Assigned department             |
| experience     | Years of experience             |

### Methods

| Method                  | Description                  |
| ----------------------- | ---------------------------- |
| approve_appointment()   | Accept appointment request   |
| reject_appointment()    | Reject appointment           |
| generate_prescription() | Create prescription          |
| update_availability()   | Modify consultation schedule |

---

## 4.4 Appointment

The `Appointment` class manages interactions between patients and doctors.

### Responsibilities

* Appointment scheduling
* Appointment tracking
* Appointment status management

### Attributes

| Attribute        | Description                             |
| ---------------- | --------------------------------------- |
| appointment_id   | Unique appointment ID                   |
| patient_id       | Linked patient                          |
| doctor_id        | Assigned doctor                         |
| appointment_date | Date of appointment                     |
| appointment_time | Time slot                               |
| status           | Pending, Approved, Completed, Cancelled |

### Methods

| Method       | Description                    |
| ------------ | ------------------------------ |
| schedule()   | Creates appointment            |
| reschedule() | Changes appointment date/time  |
| cancel()     | Cancels appointment            |
| complete()   | Marks appointment as completed |

---

# 5. Future Core Classes

The following classes will be introduced as the project evolves:

* Prescription
* MedicalRecord
* Billing
* Invoice
* Department
* Hospital
* Authentication
* Report
* Notification
* Pharmacy
* Laboratory

Each class will follow the same object-oriented design principles and integrate seamlessly into the existing architecture.

---

# 6. Object Relationships

The Hospital Management System models relationships between objects using association and composition.

```text
Patient
   │
   │ books
   ▼
Appointment
   ▲
   │ assigned to
Doctor
```

Future relationships:

```text
Patient
   │
   ├──────── MedicalRecord
   │
   ├──────── Prescription
   │
   └──────── Billing
```

---

# 7. OOP Principles Used

## 7.1 Encapsulation

Sensitive data is protected by restricting direct access to class attributes.

Examples:

* Password Hash
* Medical History
* Billing Information

Private attributes are accessed through controlled methods such as getters and setters.

Example:

```python
self.__password_hash
```

Benefits:

* Data security
* Controlled modification
* Better maintainability

---

## 7.2 Inheritance

Inheritance enables child classes to reuse common functionality from the base `User` class.

```text
User
├── Patient
├── Doctor
├── Admin
└── Receptionist
```

Benefits:

* Code reusability
* Reduced duplication
* Easier maintenance

---

## 7.3 Abstraction

Abstraction hides implementation details while exposing only the required functionality.

Examples:

* Authentication
* Billing
* Report Generation
* Database Operations

Users interact with methods without needing to understand the underlying implementation.

---

## 7.4 Polymorphism

The same method can perform different actions depending on the object.

Example:

```text
generate_report()

Doctor
↓

Patient Report

-------------------------

Admin
↓

Hospital Report
```

This enables flexible and extensible system behavior.

---

## 7.5 Composition

Complex entities are created by combining multiple objects.

Example:

```text
Patient
    │
    ├── MedicalRecord
    ├── Appointment
    ├── Prescription
    └── Billing
```

Composition promotes modularity and allows related components to evolve independently.

---

# 8. Design Benefits

The object-oriented design provides several advantages:

* High code reusability
* Clear separation of responsibilities
* Modular architecture
* Improved readability
* Simplified maintenance
* Easier testing
* Future scalability
* Cleaner project structure

---

# 9. Future Enhancements

The object model is designed to support future expansion without significant architectural changes.

Planned enhancements include:

* Multi-Hospital Support
* AI Healthcare Assistant
* Electronic Health Record Integration
* Machine Learning Predictions
* Video Consultation
* Online Payment Gateway
* Notification System
* Cloud Database Integration

---

# 10. Summary

The Hospital Management System adopts a structured Object-Oriented Design that models real-world healthcare entities as Python classes. By applying the principles of **Encapsulation**, **Inheritance**, **Abstraction**, **Polymorphism**, and **Composition**, the system remains maintainable, scalable, and easy to extend.

This design serves as the blueprint for implementing the backend modules and ensures that the application follows modern software engineering and Python development best practices.
