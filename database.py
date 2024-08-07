import sqlite3

connection = sqlite3.connect("data/data.db")


def create_table():
    connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")
    connection.commit()


def add_entry(entry_content, entry_date):
    connection.execute("INSERT INTO entries (content, date) VALUES (?, ?);", (entry_content, entry_date))
    connection.commit()


def get_entries():
    cursor = connection.execute("SELECT content, date FROM entries;")
    entries = []
    for row in cursor:
        entries.append({"content": row[0], "date": row[1]})
    return entries


def close_connection():
    connection.close()
