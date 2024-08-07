import sqlite3

connection = sqlite3.connect("data.db")

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to the programming diary!"


def create_table():
    connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")
    connection.commit()


def close_connection():
    connection.close()


def prompt_new_entry():
    from database import add_entry
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


def add_entry(entry_content, entry_date):
    connection.execute("INSERT INTO entries (content, date) VALUES (?, ?);", (entry_content, entry_date))
    connection.commit()


def get_entries():
    cursor = connection.execute("SELECT content, date FROM entries;")
    return [{"content": row[0], "date": row[1]} for row in cursor]


print(welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        from database import get_entries
        
        view_entries(get_entries())

# This is only called when the while loop ends
close_connection()
