# DRF-Level-2

## Description

DRF-Level-2 is a simple Django Rest Framework (DRF) application designed for managing quotes. The application allows for
browsing, adding, updating, and deleting quotes. Access to create, update, and delete quotes is restricted to admin
users, while browsing quotes is available to all users. The application employs pagination, splitting the list of quotes
into pages with 3 quotes each.

## Requirements

- Python (3.8 or newer)
- Django (5.0.2)
- Django Rest Framework (3.14.0)

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment:
   `python -m venv venv`
3. Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:
`pip install -r requirements.txt`  


## Requirements.txt Content

Ensure your `requirements.txt` file includes the following dependencies:

```
asgiref==3.7.2
Django==5.0.2
djangorestframework==3.14.0
pytz==2024.1
sqlparse==0.4.4
typing_extensions==4.9.0
```


## Running the Application

1. Navigate to the project directory.
2. Run migrations to create the database schema:
`python manage.py migrate`
3. Create an admin user:
`python manage.py createsuperuser`
4. Run the development server:
`python manage.py runserver`
  
### Enjoy managing your quotes with DRF-Level-2!
