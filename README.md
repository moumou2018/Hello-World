# Clinic Management System

A web application for managing a gynecology clinic, built with Python and Django.

## Features Implemented So Far

This project currently includes the following features:

*   **Core Modules:**
    *   Patient Management
    *   Appointment Scheduling
    *   Prescription Management
    *   Consultation Records
    *   Financial Invoicing
*   **Basic CRUD Operations:** For each module, users can Create, Read, Update, and Delete records.
*   **Navigation:** A basic navigation bar allows access to each module.
*   **Search and Filtering:**
    *   **Patients:** Search by first or last name.
    *   **Appointments:** Filter by patient name, doctor name, or status.
    *   **Prescriptions:** Filter by patient name, medication name, or issuing doctor.
    *   **Invoices:** Filter by patient name or payment status.

## Technology Stack

*   **Backend:** Python 3, Django
*   **Database:** SQLite (default for Django development, can be configured for others)

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory_name>
    # (Replace <repository_url> and <repository_directory_name> with actual values)
    # For this environment, the project is likely already cloned in /app.
    # The main project directory is /app/clinic_management
    ```

2.  **Navigate to the Django project directory:**
    ```bash
    cd clinic_management
    # (If you cloned, this would be inside your <repository_directory_name>)
    ```

3.  **Set up a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4.  **Install dependencies:**
    Currently, the main dependency is Django. If a `requirements.txt` file is added later, you would use:
    ```bash
    # pip install -r requirements.txt
    # For now, just Django:
    pip install django
    ```
    *(Note: In the current development environment, Django was installed globally during initial setup as venv creation failed. For local setup, venv is preferred.)*

5.  **Apply database migrations:**
    This will create the necessary database tables.
    ```bash
    python3 manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python3 manage.py runserver
    ```
    The application will typically be accessible at \`http://127.0.0.1:8000/\`. You can then navigate to the different modules (e.g., \`/patients/\`, \`/appointments/\`).

## Further Development

Planned next steps include:
*   User authentication and authorization.
*   Improved frontend design and user experience.
*   More advanced module-specific features.
*   Comprehensive testing.
