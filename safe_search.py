from sqlalchemy import text, create_engine

search_input = input("Enter a year: ")

params = {"search": search_input}

engine = create_engine('sqlite:///data/textbook.sqlite3')

with engine.connect() as connection:
    query = 'SELECT title FROM books WHERE publication_year = :search'
    results = connection.execute(text(query), params)
    rows = results.fetchall()
    
    print(f"Returned {len(rows)} results")
    
    for row in rows:
        print(f'{row.title}')
