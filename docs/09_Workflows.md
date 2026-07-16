# 🔄 System Workflows

# Hospital Management System (HMS)

---

# 1. Introduction

This document describes the major workflows of the Hospital Management System (HMS). A workflow represents the sequence of actions performed by users and the system to accomplish a specific task.

These workflows serve as a blueprint for implementing the application's business logic and ensure that every module follows a consistent process.

---

# 2. Workflow Overview

The Hospital Management System consists of several interconnected workflows.

Core workflows include:

* User Authentication
* Patient Registration
* Doctor Management
* Appointment Booking
* Consultation Process
* Prescription Generation
* Medical Record Management
* Billing Process
* Report Generation

---

# 3. User Authentication Workflow

This workflow authenticates users before they access the system.

### Steps

1. User opens the login page.
2. User enters username and password.
3. System validates the credentials.
4. Password hash is verified.
5. JWT access token is generated.
6. User is redirected to the appropriate dashboard based on their role.

### Workflow Diagram

```text id="5cjlwm"
User
 │
 ▼
Login Page
 │
 ▼
Enter Credentials
 │
 ▼
Authentication Service
 │
 ▼
Generate JWT Token
 │
 ▼
Dashboard
```

---

# 4. Patient Registration Workflow

Receptionists or administrators register new patients in the system.

### Steps

1. Receptionist opens the patient registration form.
2. Patient information is entered.
3. Input validation is performed.
4. User account and patient profile are created.
5. Patient receives a unique patient ID.
6. Registration is completed successfully.

### Workflow Diagram

```text id="2t5kfo"
Receptionist
 │
 ▼
Registration Form
 │
 ▼
Validation
 │
 ▼
Create User
 │
 ▼
Create Patient Profile
 │
 ▼
Database
```

---

# 5. Doctor Management Workflow

Administrators manage doctor information and availability.

### Steps

1. Administrator logs into the system.
2. Doctor details are entered or updated.
3. Specialization and department are assigned.
4. Availability schedule is configured.
5. Information is stored in the database.

---

# 6. Appointment Booking Workflow

Patients can book appointments with doctors based on specialization and availability.

### Steps

1. Patient logs into the system.
2. Patient selects a medical specialization.
3. The system displays available doctors.
4. Patient selects a doctor and preferred time slot.
5. The system checks availability using the **Availability Service**.
6. If available, an appointment record is created with a **PENDING** status.
7. The doctor receives the appointment request.
8. The doctor approves or declines the request.
9. If approved, the appointment status changes to **CONFIRMED**.
10. The patient receives confirmation.

### Workflow Diagram

```text id="ljlwm4"
Patient
 │
 ▼
Select Doctor
 │
 ▼
Availability Service
 │
 ▼
Doctor Available?
 │
 ├──────── No
 │         │
 │         ▼
 │   Select Another Slot
 │
 └──────── Yes
           │
           ▼
Create Appointment
           │
           ▼
Status = PENDING
           │
           ▼
Doctor Review
           │
           ▼
Approve / Reject
           │
           ▼
Status = CONFIRMED
```

---

# 7. Consultation Workflow

Doctors record patient consultation details after an appointment.

### Steps

1. Doctor views today's appointments.
2. Patient arrives for consultation.
3. Doctor records diagnosis.
4. Clinical notes are entered.
5. Prescription is generated.
6. Medical record is updated.
7. Appointment status changes to **COMPLETED**.

---

# 8. Prescription Workflow

Doctors create digital prescriptions during consultations.

### Steps

1. Open patient record.
2. Enter diagnosis.
3. Select medicines.
4. Add dosage instructions.
5. Save prescription.
6. Patient can view or print the prescription.

---

# 9. Medical Record Workflow

Medical records maintain the complete healthcare history of each patient.

### Steps

1. Patient completes consultation.
2. Doctor updates medical history.
3. Prescription is linked to the consultation.
4. Medical record is stored securely.
5. Future consultations can access previous records.

---

# 10. Billing Workflow

The billing process generates invoices based on consultation and medical services.

### Steps

1. Consultation is completed.
2. System calculates consultation fee.
3. Medicine charges are added.
4. Additional service charges are included.
5. Total amount is calculated.
6. Invoice is generated.
7. Payment status is recorded.
8. Receipt is issued to the patient.

### Workflow Diagram

```text id="e4jicd"
Consultation Completed
 │
 ▼
Calculate Charges
 │
 ▼
Generate Invoice
 │
 ▼
Payment
 │
 ▼
Payment Successful
 │
 ▼
Receipt Generated
```

---

# 11. Report Generation Workflow

Administrators generate reports for hospital operations.

### Available Reports

* Patient Reports
* Doctor Reports
* Appointment Reports
* Revenue Reports
* Daily Reports
* Monthly Reports

### Steps

1. Administrator selects report type.
2. System retrieves data.
3. Report is generated.
4. Report can be viewed, downloaded, or printed.

---

# 12. Notification Workflow (Future Enhancement)

The system will notify users about important events.

Examples include:

* Appointment confirmation
* Appointment cancellation
* Prescription ready
* Payment successful
* Password reset
* New doctor availability

Notification methods:

* Email
* SMS
* In-app notifications

---

# 13. Overall System Workflow

The complete application workflow can be summarized as follows:

```text id="kx7msu"
User Login
      │
      ▼
Authentication
      │
      ▼
Dashboard
      │
      ▼
Patient Registration
      │
      ▼
Appointment Booking
      │
      ▼
Doctor Consultation
      │
      ▼
Prescription
      │
      ▼
Medical Record Update
      │
      ▼
Billing
      │
      ▼
Payment
      │
      ▼
Reports & History
```

---

# 14. Workflow Diagrams

> Replace the following placeholders with workflow diagrams as they are created.

<p align="center">
    <img src="images/appointment_workflow.png" width="850">
</p>

<p align="center">
<b>Figure 9.1</b> – Appointment Booking Workflow
</p>

<p align="center">
    <img src="images/billing_workflow.png" width="850">
</p>

<p align="center">
<b>Figure 9.2</b> – Billing Workflow
</p>

<p align="center">
    <img src="images/authentication_workflow.png" width="850">
</p>

<p align="center">
<b>Figure 9.3</b> – Authentication Workflow
</p>

---

# 15. Workflow Summary

The Hospital Management System is designed around well-defined business workflows that automate hospital operations while ensuring accuracy, security, and efficiency. These workflows establish a clear sequence of interactions between users, business logic, and the database, providing a solid foundation for implementation and future enhancements.
