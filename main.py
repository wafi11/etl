from scrapper import scrape 
from transform import transform
from db.db import create_table,get_connection

def main():
  create_table()  
  df_row =scrape()
  df_clean= transform(df_row)
  conn = get_connection()

  conn.execute("""
    INSERT OR IGNORE INTO articles (id, title, url, source, published_at, scraped_at)
    SELECT id, title, url, source, published_at, scraped_at
    FROM df_clean
    """)
  conn.close()

  print(f"Inserted {len(df_clean)} rows!")
  
if __name__ == "__main__":
    main()
