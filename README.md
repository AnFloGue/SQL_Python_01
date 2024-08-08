___
![SQL Logo](https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png)
___

# Programming Diary

This project is a simple command-line application for managing a programming diary. Users can add entries about what they have learned each day and view past entries. The application uses SQLite for data storage.

## Features

- Add new entries with a date and content.
- View all entries.

## Requirements

- Python 3.x
- SQLite

## Setup

1. Clone the repository:
    ```sh
    git clone REPOSITORY_URL
    cd <repository-directory>
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the application:
    ```sh
    python main.py
    ```

## Usage

When you run the application, you will be presented with a menu of options:

## Menu Options

### Adding a New Entry

1. Select option 1.
2. Enter what you have learned today.
3. Enter the date in the format `YYYY-MM-DD`.

### Viewing Entries

1. Select option 2 to view all entries.

### Exiting the Application

1. Select option 3 to exit the application.

## Database Schema

The application uses an SQLite database with the following table:

- `entries`: Stores entry information (content, date).

## License

This project is licensed under the MIT License.
