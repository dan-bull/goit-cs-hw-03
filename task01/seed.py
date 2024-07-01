import psycopg2
from faker import Faker

# Підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="pass",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Ініціалізація Faker
fake = Faker()

# Заповнення таблиці status
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (status,))

# Заповнення таблиці users
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Отримання списку статусів і користувачів
cursor.execute("SELECT id FROM status")
status_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM users")
user_ids = [row[0] for row in cursor.fetchall()]

# Заповнення таблиці tasks
for _ in range(20):
    title = fake.sentence(nb_words=6)
    description = fake.text()
    status_id = fake.random_element(elements=status_ids)
    user_id = fake.random_element(elements=user_ids)
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                   (title, description, status_id, user_id))

# Коміт та закриття з'єднання
conn.commit()
cursor.close()
conn.close()
