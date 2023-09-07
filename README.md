# Django Todo App

This is a small Todo web application built using Django. It allows users to create, update, and manage their tasks or to-do items. This README provides a brief overview of how to set up and run the application.

## Prerequisites

Before you can run the application, you need to have the following software installed on your system:

- Python 3.x
- Django (latest version recommended)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Change into the project directory:

   ```bash
   cd django-todo-app
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment (Linux/Mac):

   ```bash
   source venv/bin/activate
   ```

   Activate the virtual environment (Windows):

   ```bash
   venv\Scripts\activate
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. Create the initial database schema by running the following commands:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Create a superuser account to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up your admin account.

## Running the Application

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The application should now be accessible at `http://localhost:8000/`.

2. Access the admin panel by navigating to `http://localhost:8000/admin/` and log in with the superuser account you created earlier.

## Usage

You can now use the Todo app by navigating to `http://localhost:8000/`. Here, you can create, update, and manage your tasks.
