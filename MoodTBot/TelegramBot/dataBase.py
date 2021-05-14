import sqlite3

__connection = None

def ensure_connection(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('placelist.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return 0  # res
    return inner()


def ensure_connection_init_db(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('placelist.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return 0 #res
    return inner()

def ensure_connection_add_place(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('placelist.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return 0 #res
    return inner()

def ensure_connection_get_list(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('filmlist.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return 0 #res
    return inner()

def init_db(conn, force: bool = False):
    c = conn.commit()
    if force:
        c.execute('DROP TABLE IF EXISTS place')
    c.execute('''
    CREATE TABLE IF NOT EXISTS place (
       id           INTEGER PRIMARY KEY,
       category_id    INTEGER NOT NULL,
       name         TEXT NOT NULL,
       rating       TEXT,
       address       TEXT NOT NULL,
       link         TEXT  
    )
    ''')
    conn.commit()


def add_place(category_id: int, name: str, rating, link : str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO place (category_id, name, rating, link) VALUES (?, ?, ?)', (category_id, name, rating, link))
    conn.commit()


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
