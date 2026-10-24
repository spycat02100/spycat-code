import sqlite3




def make_connection(dbname):
    try:
        return sqlite3.connect(dbname)
    except Exception as e:
        print(f"Error: {e}")
        raise


def create_table(connection):
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
    query = "INSERT INTO books (title, author, page_count, pages_read) VALUES (?, ?, ?)"

    try:
        with connection:
            connection.execute(query, (title, author, page_count, pages_read))
            print(f"Book: {title} was added to your database")
    except Exception as e:
        print(e)



def main():
    connection = make_connection("ReadQuest.db")

    create_table(connection)


if __name__ == "__main__":
    main()