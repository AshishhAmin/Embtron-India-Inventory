
# Embtron INDIA – Smart Inventory Management System

An efficient inventory management solution developed for **Embtron INDIA**, an electronics-based company. This Django-powered system is designed to streamline management of electronic components, user profiles, inventory tracking, and order processing to support business operations for electronic parts distribution.

## Table of Contents

- [Project Overview](#project-overview)
- [Technical Requirements](#technical-requirements)
- [Software Requirements](#software-requirements)
- [Functional Requirements](#functional-requirements)
- [Non-Functional Requirements](#non-functional-requirements)
- [Development Environment](#development-environment)
- [Testing Requirements](#testing-requirements)
- [Documentation](#documentation)
- [Getting Started](#getting-started)
- [Features](#features)
- [License](#license)
- [Acknowledgments](#acknowledgments)


## Project Overview

**Project Name:** Smart Inventory Management for Embtron INDIA

**Framework:** Django 5.1.3

**Purpose:**
Efficiently manage, track, and process electronic component inventory, supporting business needs such as order handling, user management, and accurate stock control for electrical parts.

## Technical Requirements

- **Python Version:** Python 3.x
- **Django Version:** 5.1.3
- **Database:** SQLite (default). Can be configured for PostgreSQL/MySQL.
- **Static Files:** For handling CSS, JavaScript, and images.
- **Media Files:** Manage uploads (e.g., datasheets or product images).


## Software Requirements

**Django Packages:**

- `django.contrib.admin` (Admin interface)
- `django.contrib.auth` (Authentication)
- `django.contrib.contenttypes`
- `django.contrib.sessions`
- `django.contrib.messages`
- `django.contrib.staticfiles`
- `crispy_forms` (Enhanced form rendering)
- `crispy_bootstrap4` (Bootstrap 4 integration)

**Frontend Libraries:**

- Bootstrap (responsive interface)
- Font Awesome (icons)
- Chart.js (data visualization)


## Functional Requirements

**User Management:**

- User registration, login, and logout.
- Profile management (view and update).

**Inventory Management:**

- Add, update, and delete electronic components.
- View product details (part number, category, quantity, price, supplier, etc.).
- Filter and search products by category, part type, or availability.
- Upload and manage images or datasheets for each part.

**Order Management:**

- Create and manage orders for components.
- View order history and order details.
- Update order quantities and manage corresponding stock levels.

**Admin Interface:**

- Dashboard to manage users, products, and orders.
- Display statistics and analytics about inventory.


## Non-Functional Requirements

- **Performance:** Efficient operations for large numbers of products and users.
- **Security:** Authentication, authorization, and secure data storage.
- **Responsiveness:** Works on mobile and desktop devices.
- **Reliability:** Data integrity is maintained during transactions.


## Development Environment

- **IDE/Text Editor:** Any (VSCode, PyCharm, etc.)
- **Version Control:** Git
- **Virtual Environment:** venv or virtualenv


## Testing Requirements

- Test all inventory, user, and order management workflows for accuracy and security.
- Check UI responsiveness and compatibility.


## Documentation

- Well-commented code and Python docstrings.
- User documentation: This README file.


## Getting Started

1. **Clone this repository:**

```
git clone https://github.com/AshishhAmin/Embtron-India-Inventory
```

2. **Set up your environment:**

```
cd Embtron-India-Inventory
python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate         # For Windows
pip install -r requirements.txt
```

3. **Configure your database (optional):**
Edit `settings.py` to use PostgreSQL or MySQL if desired.
4. **Run the application:**

```
python manage.py migrate
python manage.py runserver
```

5. **Access the system:**
Open http://127.0.0.1:8000/ in your web browser.

## Features

- **User Account Management:** Register, log in/out, and update user profiles.
- **Electronic Components Catalog:** Track, add, and search for electrical parts.
- **Order Processing:** Place, track, and manage orders.
- **Inventory Analytics:** Visual statistics using Chart.js.
- **Admin Dashboard:** Oversee users, products, orders.


## License

No explicit license provided. For usage rights and restrictions, please contact Embtron INDIA.

## Acknowledgments

- Developed for Embtron INDIA’s electronic components division.
- UI frameworks: Bootstrap, Font Awesome.
- Chart visualization: Chart.js.

