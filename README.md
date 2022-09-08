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
3. Install virtualenv: <code>pip install virtualenv</code>
4. Create a virtual environment: <code>python -m venv env</code>
5. Install django: <code>pip install django</code>
6. Create a folder for your project: <code>mkdir djangocrud</code>
7. Go to the project folder: <code>cd djangocrud</code>
8. Create a project: <code>django-admin startproject main .</code>
9. See instruction below for running the app

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
