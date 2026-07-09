from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from mysql.connector import Error
from functools import wraps

app = Flask(__name__)
app.secret_key = 'change-this-secret-key-in-production'

# ---------------------------------------------------------------------------
# Database configuration - replace these with your local MySQL credentials
# ---------------------------------------------------------------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yourpassword',
    'database': 'task_management'
}


def get_db_connection():
    """Open a new MySQL connection. Returns None on failure."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Database connection error: {e}")
        return None


def login_required(f):
    """Redirect to the login page if there is no active admin session."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'admin_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        admin_id = request.form.get('admin_id', '').strip()
        password = request.form.get('password', '').strip()

        conn = get_db_connection()
        if conn is None:
            error = "Could not connect to the database. Please try again later."
            return render_template('login.html', error=error)

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM admins WHERE username = %s AND password = %s",
                (admin_id, password)
            )
            admin = cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

        if admin:
            session['admin_id'] = admin['id']
            session['admin_username'] = admin['username']
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid Admin ID or Password."

    return render_template('login.html', error=error)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    conn = get_db_connection()
    tasks = []
    selected_title = None

    if conn is None:
        flash('Could not connect to the database.', 'error')
        return render_template('dashboard.html', tasks=tasks, current_task=None, admin=session.get('admin_username'))

    try:
        cursor = conn.cursor(dictionary=True)

        if request.method == 'POST':
            selected_title = request.form.get('task_title')
            completed = request.form.get('completed')

            cursor.execute(
                "UPDATE tasks SET completed = %s WHERE task_title = %s",
                (completed, selected_title)
            )
            conn.commit()
            flash('Task updated successfully.', 'success')

        cursor.execute("SELECT * FROM tasks ORDER BY task_id")
        tasks = cursor.fetchall()
    except Error as e:
        flash(f'Database error: {e}', 'error')
    finally:
        cursor.close()
        conn.close()

    current_task = None
    if tasks:
        if selected_title:
            current_task = next((t for t in tasks if t['task_title'] == selected_title), tasks[0])
        else:
            current_task = tasks[0]

    return render_template('dashboard.html', tasks=tasks, current_task=current_task, admin=session.get('admin_username'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
