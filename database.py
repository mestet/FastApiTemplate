import psycopg2
from contextlib import contextmanager


# TODO: read creds from env variable
@contextmanager
def get_cursor():
    """Yields a database cursor and ensures the connection and cursor are closed after use."""
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="secret",
            host="localhost",
            port="5432"
        )
        with conn.cursor() as cur:
            yield cur
        conn.commit()  # Commit the transaction if everything runs smoothly
    except psycopg2.Error as e:
        print(f"Database operation error: {e}")
        if conn:
            conn.rollback()  # Rollback in case of an error
        raise
    finally:
        if conn:
            conn.close()
