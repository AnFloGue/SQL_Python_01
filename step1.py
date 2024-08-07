from sqlalchemy import create_engine, text, Table, Column, Integer, String, MetaData

# Create an engine that connects to a SQLite database file named "textbook.sqlite3"
engine = create_engine('sqlite:///data/textbook.sqlite3')

# Define metadata
metadata = MetaData()

# Define the table schema
table_name = Table('table_name', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String),
                   Column('value', String))

# Create the table if it does not exist
metadata.create_all(engine)

with engine.connect() as connection:
    # Run an SQL query
    results = connection.execute(text('SELECT * FROM table_name'))
    rows = results.fetchall()

    # Print results
    for row in rows:
        print(row)