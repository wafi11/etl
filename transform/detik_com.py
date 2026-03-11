# transform/cleaner.py
import pandas as pd
from datetime import datetime
import re


def transform(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Drop duplikat
    df = df.drop_duplicates(subset=["url"])

    # 2. Drop row yang title-nya kosong
    df = df.dropna(subset=["title"])

    # 3. Bersihin title dari whitespace berlebih
    df["title"] = df["title"].str.strip()

    # 4. Convert published_at ke datetime
    df["published_at"] = df["published_at"].apply(parse_date)

    # 5. Extract sumber berita dari URL
    df["source"] = df["url"].apply(extract_source)

    # 6. Tambah kolom id unik
    df["id"] = df["url"].apply(lambda x: abs(hash(x)) % 10**8)

    print(df)

    return df


def parse_date(date_str: str) -> datetime:
    try:
        clean = re.sub(r"^\w+,\s", "", date_str)
        clean = clean.replace(" WIB", "").replace(" WITA", "").replace(" WIT", "").strip()
        return datetime.strptime(clean, "%d %b %Y %H:%M")
    except Exception as e:
        print(f"ERROR: {e}")
        return None


def extract_source(url: str) -> str:
    try:
        # https://news.detik.com → news
        match = re.search(r'https?://(\w+)\.detik\.com', url)
        return match.group(1) if match else "unknown"
    except:
        return "unknown"
