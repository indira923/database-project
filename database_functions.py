import sqlite3

database = './static/data/db-project.db'

def delete_post(rowid):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("DELETE FROM Posts WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()

def update_post(name, type, location, rowid):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("UPDATE Pokemon name = ?, type = ?, location = ?, WHERE rowid = ?", (name, type, location, rowid))
    conn.commit()
    conn.close()


def add_post(name, type, location):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("INSERT INTO Pokemon (name, type, location) VALUES (?, ?, ?)", (name, type, location))
    conn.commit()
    conn.close()

def get_all_posts():
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM Pokemon")
    posts = []
    for row in result: 
        post = {
            'name': row[1],
            'type': row[2],
            'location': row[3],
            'rowid' : row[0]

        }
        post.append(post)
        conn.close()
    return posts
