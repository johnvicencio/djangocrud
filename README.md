# Django Notes
Shows list of employees where you can add, edit / update, and remove / delete an employee (also called "CRUD" functions: create, read, update, delete)

## Requirements 
- Django framework
- Python
- Bootstrap (HTML, CSS, JavaScript)
- SQLite

## Setting Up Environment 
1. Open Terminal
2. Install latest Python
3. Install virtualenv: pip install virtualenv
4. Create a virtual environment: python -m venv env
5. Install django: pip install django
6. Create a folder for your project: mkdir djangocrud
7. Create a project: django-admin startproject main .
8. See instruction below for running the app

## Features
- Admin login (Django default feature)
- Show list of employees
- Create a new employee record details (name, email, contact, role, and salary)
- Edit or update an existing employee record
- Delete or remove an existing employee record
- Form validation

## Instruction
1. Download the repository
2. Open Terminal 
3. Go to the djangocrud directory: cd djangocrud
4. Run server: python manage.py runserver
5. Open browser and enter url: http://127.0.0.1:8000/