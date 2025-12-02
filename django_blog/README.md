# Django Blog Authentication System

## Overview

This project implements a complete authentication system for a Django Blog application. It includes user registration, login, logout, and profile management. The goal is to create a secure and user-friendly authentication workflow.

---

## Features

### User Registration

* Custom registration form using Django's `UserCreationForm`.
* Additional fields such as email included.
* Validation and error handling.

### User Login & Logout

* Uses Django's built-in authentication views.
* Session-based login.
* Secure logout handling.

### Profile Management

* Authenticated users can view and edit their profile.
* Supports updating username and email.
* Optional profile picture and bio support.

### Security

* Password hashing handled by Django.
* CSRF protection enabled on all forms.
* Validation protection against common attacks.

###  Templates & UI

* Fully functional HTML templates using `base.html` layout.
* Static CSS and JavaScript integrated.

---

## Project Structure

```
django_blog/
 ├── blog/
 │    ├── templates/blog/
 │    │    ├── base.html
 │    │    ├── login.html
 │    │    ├── register.html
 │    │    ├── profile.html
 │    │    └── logout.html
 │    ├── static/
 │    │    ├── css/styles.css
 │    │    └── js/scripts.js
 │    ├── forms.py
 │    ├── views.py
 │    └── urls.py
 │
 ├── django_blog/
 │    ├── urls.py
 │    └── settings.py
 │
 └── media/  ← created automatically for uploaded files
```

---

## Setup Instructions

### 1. Install Dependencies

```
pip install django
```

### 2. Apply Migrations

```
python manage.py migrate
```

### 3. Run Development Server

```
python manage.py runserver
```

---

## URL Configuration

### **Project-level (`django_blog/urls.py`):**

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### App-level (`blog/urls.py`)

```
path('login/', LoginView.as_view(template_name='blog/login.html'), name='login')
path('logout/', LogoutView.as_view(), name='logout')
path('register/', views.register, name='register')
path('profile/', views.profile, name='profile')
```

---

## Static Files Setup

In `settings.py`:

```
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## Templates

All templates are stored in:

```
blog/templates/blog/
```

Main template: `base.html`

---

## Forms (`forms.py`)

* Custom registration form.
* User profile update form.

---

## Testing Checklist

* [ ] Register a new user.
* [ ] Login with registered user.
* [ ] Logout successfully.
* [ ] Access profile page only when logged in.
* [ ] Update profile information.
* [ ] Confirm CSRF tokens exist in forms.
* [ ] Ensure media files load correctly.

---

## Documentation Summary

This README explains:

* Project purpose
* Authentication features
* Directory structure
* Setup guides
* URL routing
* Static & media configuration
* Template usage
* Testing steps

You now have a complete authentication system ready to use or expand with blog post functionality.

---

## Author

Created for training and project building in **Alx_DjangoLearnLab**.
