import sqlite3

__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('placelist.db')
    return __connection


def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS place')

    c.execute('''
    CREATE TABLE IF NOT EXISTS place (
       id           INTEGER PRIMARY KEY,
       category_id    INTEGER NOT NULL,
       name         TEXT NOT NULL,
       rating       DOUBLE, 
       address       TEXT NOT NULL, 
       site_link       TEXT 
    )
    ''')
    conn.commit()


def add_place(category_id: int, name: str, rating):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO place (category_id, name, rating) VALUES (?, ?, ?)', (category_id, name, rating))
    get_connection().commit()


def get_list_of_places(category_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT name, rating FROM place WHERE category_id = ?', (category_id,))
    return c.fetchall()


if __name__ == '__main__':
    init_db(force=True)
    add_place(category_id=1, name='Птичка', rating=4.3)
    add_place(category_id=1, name='Мама, я дома', rating=5.0)

    print(get_list_of_places(1))
