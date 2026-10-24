import sqlite3


def make_connection(dbname):
    try:
        return sqlite3.connect(dbname)
    except Exception as e:
        print(f"Error: {e}")
        raise

def create_book_table(connection):
    """
    Creates book table in readquest database
    """

    query = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        page_count INTEGER NOT NULL,
        pages_read INTEGER
    )
    """
    try:
        with connection:
            connection.execute(query)
            print("Book table was created!")
    except Exception as e:
        print(e)

def insert_book(connection, title: str, author: str, page_count: int, pages_read: int):
    query = "INSERT INTO books (title, author, page_count, pages_read) VALUES (?, ?, ?, ?)"

    try:
        with connection:
            connection.execute(query, (title, author, page_count, pages_read))
            print(f"Book: {title} was added to your database")
    except Exception as e:
        print(e)

def create_reading_session_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS reading_sessions (
    id INTEGER PRIMARY KEY,
    book_id INTEGER NOT NULL,
    session_date TEXT NOT NULL,
    pages_read INTEGER NOT NULL,
    minutes_read INTEGER NOT NULL
    )
    """
    try:
        with connection:
            connection.execute(query)
            print("Reading session table was created!")
    except Exception as e:
        print(e)

def add_reading_session(connection, book_id: int, session_date: str, pages_read: int, minutes_read: int):
    query = "INSERT INTO reading_sessions (book_id, session_date, pages_read, minutes_read) VALUES (?, ?, ?, ?)"

    try:
        with connection:
            connection.execute(query, (book_id, session_date, pages_read, minutes_read))
            print("Reading session added")
    except Exception as e:
        print(e)

def search_books(connection, condition):
    query = f"SELECT * from books "
    if condition:
        query += f"WHERE {condition} "
    try:
        with connection:
            result = connection.execute(query).fetchall()
            return result
    except Exception as e:
        print(e)

def search_reading_sessions(connection, condition):
    query = "SELECT * FROM reading_sessions "

    if condition:
        query += f"WHERE {condition}"
    try:
        with connection:
            result = connection.execute(query).findall()
            return result
    except Exception as e:
        print(e)

def user_continue():
    user_input = input("Do you wish to continue? (T/F)")
    if(user_input == "T"):
        return True 
    else:
        return False






def main():
    connection = make_connection("ReadQuest.db")
    try:
        create_book_table(connection)
        create_reading_session_table(connection)
        cont = True 
        while cont == True:
            table = input("Enter table (books, reading_sessions): ").lower()
            start = input("Enter option (Add, Delete, Update, Search, Add Many): ").lower()
            if table == "books":
                if start == "add":
                    title = input("Enter title: ")
                    author = input("Enter author: ")
                    page_count = int(input("Enter page count: "))
                    pages_read = int(input("Enter pages read: "))
                    insert_book(connection, title, author, page_count, pages_read)
                    if not user_continue():
                        cont = False                  
                elif start == "search":
                    condition = input("Enter a condition (To list all press enter): ")
                    print(search_books(connection, condition))
                    if not user_continue():
                        cont = False
            elif table == "reading_sessions":
                if start == "add":
                    book_id = int(input("Enter book id (If unknown use search with books table): "))
                    session_date = input("Enter session date: ")
                    pages_read = int(input("Enter pages read: "))
                    minutes_read = int(input("Enter minutes read: "))
                    add_reading_session(connection, book_id, session_date, pages_read, minutes_read)
                    if not user_continue():
                        cont = False
                elif start == "search":
                    condition = input("Enter a condition (To list all press enter): ")
                    print(search_reading_sessions(connection, condition))
                    if not user_continue():
                        cont = False
    finally:
        connection.close()


if __name__ == "__main__":
    main()