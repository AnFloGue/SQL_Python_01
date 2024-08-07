import sqlalchemy
from sqlalchemy import text

connection_string = 'sqlite:///data/textbook.sqlite3'
engine = sqlalchemy.create_engine(connection_string)

with engine.connect() as connection:
    # Run an SQL query
    results = connection.execute(text('SELECT * FROM books WHERE title = "The Hobbit" '))
    rows = results.fetchall()
    
    # Print results
    # first_row = rows[0]._mapping
    # for key, value in first_row.items():
    #     print(f"{key}: {value}")
    
    # print(first_row.id)
    
    for row in rows:
        print(row)