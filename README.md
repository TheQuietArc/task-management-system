# Task Management System

A responsive administrative web portal built using Python, Flask, and MySQL. This system allows a preserved admin user to log in and update employee task completion states dynamically.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **Frontend:** HTML5, CSS3 (responsive UI), JavaScript (Fetch API)

## 📁 Repository Structure

- `app.py` — Core application file handling login routing, session management, and CRUD update actions via MySQL.
- `init_db.py` — Database initialization script that configures tables using `AUTO_INCREMENT` and seeds initial profiles.
- `static/style.css` — Modern, responsive CSS styling.
- `templates/login.html` — Administrative authentication interface.
- `templates/dashboard.html` — Interactive task table with reactive status dropdowns (updates via AJAX, no page reload).
- `requirements.txt` — Python dependencies.

## ⚙️ How to Run the Project Locally

### 1. Configure the MySQL Server

Make sure you have a running MySQL instance. Open `app.py` and `init_db.py` and replace the connection parameters (`host`, `user`, `password`) with your local credentials.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize the Database

```bash
python init_db.py
```

This creates the `task_management` database, the `admins`, `employees`, and `tasks` tables, and seeds a default admin account plus a few sample employees/tasks.

### 4. Launch the Server

```bash
python app.py
```

### 5. Access the App

Open your browser and go to: http://127.0.0.1:5000

## 🔐 Preserved Admin Credentials

- **Admin ID:** `admin`
- **Password:** `admin123`

> Note: credentials are stored in plain text here to keep the assignment simple. In a real production app, passwords should be hashed (e.g. with `werkzeug.security.generate_password_hash`).
