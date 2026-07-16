# 🌐 REST API Documentation

# Hospital Management System (HMS)

---

# 1. Introduction

The Hospital Management System exposes a RESTful API that allows clients (web applications, mobile applications, and third-party services) to securely interact with the system.

The API follows REST architectural principles and exchanges data using the **JSON** format.

---

# 2. Base URL

```text
/api/v1
```

Example:

```text
http://localhost:5000/api/v1
```

---

# 3. API Standards

* RESTful Architecture
* JSON Request & Response
* HTTP Status Codes
* JWT Authentication
* Role-Based Access Control (RBAC)
* Stateless Communication

---

# 4. Authentication

Protected endpoints require a valid JWT access token.

Example Header:

```http
Authorization: Bearer <JWT_TOKEN>
```

---

# 5. HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 409  | Conflict              |
| 500  | Internal Server Error |

---

# 6. Authentication APIs

| Method | Endpoint                | Description                      | Authentication |
| ------ | ----------------------- | -------------------------------- | -------------- |
| POST   | `/auth/register`        | Register a new user              | No             |
| POST   | `/auth/login`           | Authenticate user and return JWT | No             |
| POST   | `/auth/logout`          | Logout current user              | Yes            |
| GET    | `/auth/profile`         | Get logged-in user profile       | Yes            |
| PUT    | `/auth/profile`         | Update profile                   | Yes            |
| PUT    | `/auth/change-password` | Change password                  | Yes            |

---

# 7. Patient APIs

| Method | Endpoint         | Description            | Authentication       |
| ------ | ---------------- | ---------------------- | -------------------- |
| GET    | `/patients`      | List all patients      | Admin / Receptionist |
| GET    | `/patients/{id}` | View patient details   | Yes                  |
| POST   | `/patients`      | Register a patient     | Receptionist         |
| PUT    | `/patients/{id}` | Update patient details | Receptionist         |
| DELETE | `/patients/{id}` | Delete patient record  | Admin                |

---

# 8. Doctor APIs

| Method | Endpoint        | Description         | Authentication |
| ------ | --------------- | ------------------- | -------------- |
| GET    | `/doctors`      | List all doctors    | Yes            |
| GET    | `/doctors/{id}` | View doctor profile | Yes            |
| POST   | `/doctors`      | Add doctor          | Admin          |
| PUT    | `/doctors/{id}` | Update doctor       | Admin          |
| DELETE | `/doctors/{id}` | Remove doctor       | Admin          |

---

# 9. Appointment APIs

| Method | Endpoint             | Description        | Authentication   |
| ------ | -------------------- | ------------------ | ---------------- |
| GET    | `/appointments`      | List appointments  | Yes (Role-Based) |
| GET    | `/appointments/{id}` | View appointment   | Yes              |
| POST   | `/appointments`      | Create appointment | Patient          |
| PUT    | `/appointments/{id}` | Update appointment | Receptionist     |
| DELETE | `/appointments/{id}` | Cancel appointment | Patient / Admin  |

---

# 10. Billing APIs

| Method | Endpoint        | Description           | Authentication |
| ------ | --------------- | --------------------- | -------------- |
| GET    | `/billing`      | List invoices         | Admin          |
| GET    | `/billing/{id}` | View invoice          | Yes            |
| POST   | `/billing`      | Generate invoice      | Receptionist   |
| PUT    | `/billing/{id}` | Update payment status | Admin          |
| DELETE | `/billing/{id}` | Remove invoice        | Admin          |

---

# 11. Medical Record APIs

| Method | Endpoint                        | Description           | Authentication   |
| ------ | ------------------------------- | --------------------- | ---------------- |
| GET    | `/medical-records/{patient_id}` | View medical records  | Doctor / Patient |
| POST   | `/medical-records`              | Create medical record | Doctor           |
| PUT    | `/medical-records/{id}`         | Update medical record | Doctor           |
| DELETE | `/medical-records/{id}`         | Delete record         | Admin            |

---

# 12. Dashboard APIs

| Method | Endpoint             | Description             | Authentication |
| ------ | -------------------- | ----------------------- | -------------- |
| GET    | `/dashboard/admin`   | Administrator dashboard | Admin          |
| GET    | `/dashboard/doctor`  | Doctor dashboard        | Doctor         |
| GET    | `/dashboard/patient` | Patient dashboard       | Patient        |

---

# 13. Reports APIs

| Method | Endpoint            | Description    | Authentication |
| ------ | ------------------- | -------------- | -------------- |
| GET    | `/reports/patients` | Patient report | Admin          |
| GET    | `/reports/doctors`  | Doctor report  | Admin          |
| GET    | `/reports/revenue`  | Revenue report | Admin          |

---

# 14. Standard API Response Format

## Success Response

```json
{
    "status": "success",
    "message": "Appointment booked successfully.",
    "data": {
        "appointment_id": 101,
        "status": "Confirmed"
    }
}
```

---

## Error Response

```json
{
    "status": "error",
    "message": "Appointment not found.",
    "error_code": 404
}
```

---

## Validation Error

```json
{
    "status": "fail",
    "message": "Validation failed.",
    "errors": {
        "email": "Invalid email address.",
        "password": "Password must contain at least 8 characters."
    }
}
```

---

# 15. Request Example

## Login Request

```http
POST /api/v1/auth/login
```

```json
{
    "username": "john_doe",
    "password": "SecurePassword123"
}
```

---

# 16. Response Example

```json
{
    "status": "success",
    "message": "Login successful.",
    "token": "<JWT_TOKEN>",
    "user": {
        "id": 1,
        "username": "john_doe",
        "role": "DOCTOR"
    }
}
```

---

# 17. Authentication Flow

```text
User Login
      │
      ▼
POST /auth/login
      │
      ▼
Validate Credentials
      │
      ▼
Generate JWT Token
      │
      ▼
Return Token
      │
      ▼
Client Stores Token
      │
      ▼
Protected API Requests
```

---

## Authentication Flow Diagram

> Replace this placeholder with the authentication flow diagram.

<p align="center">
    <img src="images/authentication_flow.png" width="850">
</p>

<p align="center">
<b>Figure 6.1</b> – JWT Authentication Flow
</p>

---

# 18. API Security

The API follows several security best practices:

* JWT Authentication
* Role-Based Access Control (RBAC)
* Password Hashing (Bcrypt)
* Input Validation
* SQL Injection Prevention
* Cross-Site Scripting (XSS) Protection
* Secure Session Management
* HTTPS Support (Production)

---

# 19. API Versioning

To support future enhancements without breaking existing clients, the API uses versioning.

Current Version:

```text
/api/v1
```

Future Versions:

```text
/api/v2
/api/v3
```

---

# 20. Future API Enhancements

Planned API additions include:

* Pharmacy APIs
* Laboratory APIs
* Notification APIs
* Payment Gateway APIs
* File Upload APIs
* AI Chatbot APIs
* Analytics APIs
* Mobile Application APIs

---

# 21. API Documentation Summary

The Hospital Management System REST API provides a secure, scalable, and standardized interface for communication between the frontend and backend. Following REST principles, JWT authentication, and consistent JSON responses ensures that the application is maintainable, extensible, and ready for future integration with web, mobile, and third-party systems.
