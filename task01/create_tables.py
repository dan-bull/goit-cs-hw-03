import psycopg2

# Параметри підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="pass",
    host="localhost",
    port="5432"
)

# Створення курсору для виконання SQL запитів
cur = conn.cursor()

# SQL запити для створення таблиць
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
"""

create_status_table = """
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
"""

create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER REFERENCES status(id),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
"""

# Виконання SQL запитів
try:
    cur.execute(create_users_table)
    cur.execute(create_status_table)
    cur.execute(create_tasks_table)
    conn.commit()  # Застосування змін до бази даних
    print("Таблиці успішно створено")
except Exception as e:
    print(f"Сталася помилка: {e}")
    conn.rollback()  # Відміна змін у разі помилки
finally:
    cur.close()
    conn.close()  # Закриття підключення до бази даних
