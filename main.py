from database import add_entry, close_connection, get_entries
import datetime

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to the programming diary!"


def main():
    def prompt_new_entry():
        entry_content = input("What have you learned today? ")
        while True:
            entry_date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(entry_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Incorrect date format, should be YYYY-MM-DD")
        add_entry(entry_content, entry_date)
    
    def view_entries(entries):
        for entry in entries:
            print(f"{entry[1]}\n{entry[0]}\n\n")
    
    print(welcome)
    
    while (user_input := input(menu)) != "3":
        if user_input == "1":
            prompt_new_entry()
        elif user_input == "2":
            view_entries(get_entries())
    
    close_connection()


if __name__ == "__main__":
    main()
