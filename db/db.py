import duckdb

DB_PATH = "./detik.duckdb"

def get_connection():
    return duckdb.connect(DB_PATH)


def create_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id           BIGINT PRIMARY KEY,
            title        VARCHAR,
            url          VARCHAR UNIQUE,
            source       VARCHAR,
            published_at TIMESTAMP,
            scraped_at   TIMESTAMP
        )
    """)
    conn.close()
    print("Table created!")