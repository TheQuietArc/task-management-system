# Task Management System

A responsive administrative web portal built using Python, Flask, and MySQL. A preserved admin user logs in and updates individual employee task completion states through a simple task-selector form.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **Frontend:** HTML5, CSS3 (responsive UI), JavaScript

## 📁 Repository Structure

- `app.py` — Core application file handling login routing, session management, and task update logic via MySQL.
- `init_db.py` — Database initialization script that creates the `admins` and `tasks` tables and seeds sample data.
- `static/style.css` — Card-based, responsive CSS styling.
- `templates/login.html` — Administrative authentication interface.
- `templates/dashboard.html` — Task management form: pick a task from a dropdown, view its employee details, and toggle its completed status.
- `requirements.txt` — Python dependencies.

## 🗂️ Database Schema

**admins**
| Column | Type |
|---|---|
| id | INT, AUTO_INCREMENT, PK |
| username | VARCHAR(50), UNIQUE |
| password | VARCHAR(255) |

**tasks**
| Column | Type |
|---|---|
| task_id | INT, AUTO_INCREMENT, PK |
| employee_id | INT |
| employee_name | VARCHAR(100) |
| task_title | VARCHAR(255), UNIQUE |
| completed | VARCHAR(5) — `'true'` or `'false'` |

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

This creates the `task_management` database, the `admins` and `tasks` tables, and seeds a default admin account plus a few sample tasks. Re-running this script is safe — it drops and recreates the `tasks` table each time.

### 4. Launch the Server

```bash
python app.py
```

### 5. Access the App

Open your browser and go to: http://127.0.0.1:5000

## 🖥️ How It Works

1. Log in with the admin credentials below.
2. The dashboard shows one task at a time: its Task ID, the assigned employee's name and ID, a **Task Title** dropdown to switch between tasks, and a **Completed** dropdown (`true`/`false`).
3. Selecting a different task in the dropdown updates the displayed details instantly (client-side, no page reload).
4. Changing **Completed** and clicking **Submit** sends the update to the server, which persists it in MySQL and shows a success message.

## 🔐 Preserved Admin Credentials

- **Admin ID:** `admin`
- **Password:** `admin123`

> Note: credentials are stored in plain text here to keep the assignment simple. In a real production app, passwords should be hashed (e.g. with `werkzeug.security.generate_password_hash`).
