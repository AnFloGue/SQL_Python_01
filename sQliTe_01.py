import sqlite3

connection = sqlite3.connect('data/data.db')


def create_table():
    connection.execute('CREATE TABLE IF NOT EXISTS entries (content TEXT, title TEXT, author TEXT)')


def add_entry(content, title, author):
    connection.execute('INSERT INTO entries (content, title, author) VALUES (?, ?, ?)', (content, title, author))
    connection.commit()


def get_entries():
    cursor = connection.execute('SELECT content, title, author FROM entries')
    return cursor.fetchall()


def close_connection():
    connection.close()


create_table()
content = input('Enter your content: ')
title = input('Enter your title: ')
author = input('Enter your author: ')
add_entry(content, title, author)
entries = get_entries()

print(entries)
close_connection()
