# Library Management System 📚

## Introduction
The **Library Management System** is a web-based application built using **Django** and **Django Rest Framework (DRF)**. It allows administrators to manage books efficiently, including adding, updating, and deleting book records. The system also includes **user authentication, CSRF protection, and validation mechanisms** to ensure secure and reliable data management.

## Technologies Used 🛠️
- **Backend:** Django, Django Rest Framework (DRF), Python
- **Frontend:** HTML, CSS, JavaScript (if applicable)
- **Database:** SQLite/MySQL
- **Authentication:** Django's built-in User Model
- **Security Features:** CSRF Protection, Form Validation

## Features ✅
- **User Authentication:** Signup, Login, Logout
- **Book Management:** Add, Update, Delete, View Books
- **Validation Mechanisms:**
  - Required fields validation
  - Password match validation
  - Unique email validation for admin signup
- **Security:**
  - CSRF tokens for secure data transmission
  - Django's built-in authentication
- **REST API Implementation (DRF)**

## Installation and Setup 🚀
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Admin Access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the project at **http://127.0.0.1:8000/**

## API Endpoints (if using DRF) 🌐
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/signup/` | POST | Register a new admin |
| `/login/` | POST | Authenticate admin |
| `/logout/` | GET | Logout admin |
| `/bookentry/` | POST | Add a new book |
| `/updatebook/` | GET | View all books |
| `/delete/<bid>/` | DELETE | Delete a book |
| `/update/<bid>/` | PUT | Update book details |

## Project Explanation 📝
This system is designed to **simplify library book management** by enabling admins to efficiently manage books through a web-based interface. The project uses **Django's authentication system** to ensure only authorized users can make changes. All forms include **CSRF tokens** for protection against cross-site request forgery attacks. Additionally, **Django Rest Framework (DRF)** allows for **API-based interactions** for potential integration with other systems.

## Contributing 🤝
Feel free to contribute by forking the repository and submitting a pull request!

## License 📜
This project is licensed under the **MIT License**.

---
Let me know if you need any modifications! 🚀

