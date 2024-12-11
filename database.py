import pyodbc
# Замените значения на свои
SERVER = 'DESKTOP-9LNU1S0\SQLEXPRESS'  # Имя вашего SQL Server
DATABASE = 'devops'  # Имя вашей базы данных
DRIVER = '{ODBC Driver 17 for SQL Server}'  # Название ODBC драйвера (может отличаться)

def get_db_connection():
    conn = None
    try:
        # Используем Trusted_Connection=yes для Windows Authentication
        conn = pyodbc.connect(f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes')
        return conn
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Ошибка подключения к базе данных: {sqlstate}")
        return None

def get_all_items():
    conn = get_db_connection()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    columns = [column[0] for column in cursor.description]
    items = []
    for row in cursor.fetchall():
        items.append(dict(zip(columns, row)))
    conn.close()
    return items

def add_item(name, description):
    conn = get_db_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", name, description)
    conn.commit()
    conn.close()