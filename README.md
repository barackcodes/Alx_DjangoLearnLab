Social Media API: Project Setup & User Authentication
1. Overview

Week 1 focuses on setting up the Django project, integrating Django REST Framework, and implementing a user authentication system using a custom user model and token-based authentication.

2. #Setup Instructions
Install dependencies
pip install django djangorestframework djangorestframework-authtoken

Create project and app
django-admin startproject social_media_api
cd social_media_api
python manage.py startapp accounts

Add installed apps

rest_framework
rest_framework.authtoken
accounts

Apply migrations
python manage.py makemigrations
python manage.py migrate

3. #User Model

A custom user model CustomUser extends Django’s AbstractUser and includes:
bio
profile_picture
followers (ManyToMany self relationship)

4. #Authentication
Implemented using DRF Token Authentication.
Available endpoints:

Endpoint	Method	Description
/api/accounts/register/	POST	Register user + return token
/api/accounts/login/	POST	Login + return token
/api/accounts/profile/	GET	View authenticated user

5. #Testing
Use Postman to test:
Registration
Login
Token retrieval
