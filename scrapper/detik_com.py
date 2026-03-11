import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv
import os


BASE_URL = "https://www.detik.com/terpopuler"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

csv_path = "./data/detik_com.csv"
def scrape() -> pd.DataFrame:
    response = requests.get(BASE_URL, headers=HEADERS)
    soup     = BeautifulSoup(response.text, "html.parser")

    articles = []

    for item in soup.select("article.list-content__item"):
        title    = item.select_one("h3.media__title")
        link     = item.select_one("a")
        date     = item.select_one("div.media__date span[d-time]")



        articles.append({
            "title"       : title.get_text(strip=True)    if title    else None,
            "url"         : link["href"]                  if link     else None,
            "published_at": date["title"]                  if date     else None,
            "scraped_at"  : datetime.now().isoformat()
        })

    # Pakai DictWriter biar bisa tulis dict langsung
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["title", "url", "published_at", "scraped_at"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(articles) 

    return pd.DataFrame(articles)
