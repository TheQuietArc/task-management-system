import mysql.connector

# ---------------------------------------------------------------------------
# Replace these with your local MySQL credentials
# ---------------------------------------------------------------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yourpassword'
}

DB_NAME = 'task_management'


def create_database():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    conn.close()
    print(f"Database '{DB_NAME}' ready.")


def create_tables_and_seed():
    conn = mysql.connector.connect(**DB_CONFIG, database=DB_NAME)
    cursor = conn.cursor()

    # Drop old tables from a previous schema version, if present.
    cursor.execute("DROP TABLE IF EXISTS tasks")
    cursor.execute("DROP TABLE IF EXISTS employees")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE tasks (
            task_id INT AUTO_INCREMENT PRIMARY KEY,
            employee_id INT NOT NULL,
            employee_name VARCHAR(100) NOT NULL,
            task_title VARCHAR(255) NOT NULL UNIQUE,
            completed VARCHAR(5) NOT NULL DEFAULT 'false'
        )
    """)

    # Seed the preserved admin account (assignment requirement).
    cursor.execute("SELECT COUNT(*) FROM admins")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO admins (username, password) VALUES (%s, %s)",
            ('admin', 'admin123')
        )
        print("Seeded default admin (admin / admin123).")

    # Seed sample tasks so the dashboard isn't empty.
    cursor.execute("SELECT COUNT(*) FROM tasks")
    if cursor.fetchone()[0] == 0:
        tasks = [
            (101, 'Aditi Sharma', 'Fix login page bug', 'false'),
            (101, 'Aditi Sharma', 'Write unit tests for API', 'false'),
            (102, 'Rohan Verma', 'Prepare Q3 campaign report', 'false'),
            (103, 'Priya Nair', 'Design new dashboard mockups', 'true'),
            (104, 'Karan Mehta', 'Follow up with client leads', 'false'),
        ]
        cursor.executemany(
            "INSERT INTO tasks (employee_id, employee_name, task_title, completed) VALUES (%s, %s, %s, %s)",
            tasks
        )
        print("Seeded sample tasks.")

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_database()
    create_tables_and_seed()
    print("Database initialization complete.")
